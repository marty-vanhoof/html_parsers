from collections import defaultdict
from bs4 import BeautifulSoup
import pandas as pd
import requests

# put the URL for the site here
URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_past_and_future_population'

def get_table_html(url):
    '''Parse the html on the webpage and get the html corresponding
    to the tables that we want.'''
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    tables = [t for t in soup.find_all('table', 'sortable wikitable')]
    
    return tables
    
def coerce_to_int(s):
    '''Coerce string to integer.'''
    
    try:
        return int(s)
    except ValueError:
        return s

def parse_table(table_html):
    '''Parse the html data from a table into a list of Python dictionaries.
    Each dict represents a row of the table data, where the dict keys are 
    the column names.'''
    
    # extract the table headers text from the <th> tags and coerce them to ints
    headers = [coerce_to_int( th.text ) for th in table_html.find('tr') if th != '\n']
    # extract the table rows from the <tr> tags
    rows_html = table_html.find_all('tr')[1:]
    
    # table_data will be populated and returned as a list of dictionaries
    table_data = []
    for row in rows_html:
        row_dict = defaultdict()
        # for each row, make a list of data values from the <td> tags
        row_list = [td.text for td in row.find_all('td')]
        # loop over the headers and populate row_dict with the relevant data
        for i, header in enumerate(headers):
            row_dict[ headers[i] ] = row_list[i].replace(u'\xa0', u'')
            
        table_data.append(row_dict)
        
    # remove the '%' keys and values
    for row in table_data:
        for key in list(row):
            if key == '%':
                row.pop(key)
                
    # Python doesn't like numbers with commas in them
    for row in table_data:
        for key in row.keys():
            row[key] = row[key].replace(',', '')
            row[key] = coerce_to_int(row[key])
        
    return table_data
        
def merge_table_data(tables_html):
    '''Merge the data from the separate tables into one data structure.
    Returns a list of dictionaries where each dict represents a row of
    data values in the new table and the dict keys are the column names.'''
        
    tables_data = [ parse_table(t) for t in tables_html ]
    grouped_data = []
    # loop over the rows of each table in tables_data
    for j in range( len(tables_data[0]) ):
        # for each row of each table, put the relevant dicts into a single list
        row_dicts = [ tables_data[i][j] for i in range(len(tables_data)) ]
        grouped_data.append(row_dicts)
    
    # now for each list in grouped_data, merge the dicts into a single dict
    merged_data = []
    for row in grouped_data:
        result = {}
        # merge the dictionaries in each row
        for d in row:
            result.update(d)
        merged_data.append(result)
        
    return merged_data
    
def make_dataframe(tables_data):

    df = pd.DataFrame.from_dict(tables_data)

    # move the country column to the front and rename it 'country/territory'
    countries = df['Country (or dependent territory)']
    df.drop(labels = ['Country (or dependent territory)'], axis = 1, inplace = True)
    df.insert(0, 'country/territory', countries)

    # set the index to be the 'country/territory' column
    df.set_index('country/territory', inplace = True)
    
    return df

def main():    
    tbls_html = get_table_html(URL)
    tbls_data = merge_table_data(tbls_html)
    df = make_dataframe(tbls_data)
    return df

# check whether script works properly
df = main()
print( df.head() )