import requests
from bs4 import BeautifulSoup

def keep_crawling(search_history, target_url):
    '''decide whether to continue to crawl each webpage based on conditions.
    Returns False to stop crawling, otherwise the function returns True.'''

    if search_history[-1] == target_url:
        print("Target article found!")
        return False
    elif len(search_history) > 50:
        print("The search is going on too long; aborting search!")
        return False
    elif len(search_history) != len(set(search_history)):
        print("We are back to an article we've already seen; aborting search!")
        return False
    else:
        return True

article_history = ['https://en.wikipedia.org/wiki/Machine_learning']
target_url = 'https://en.wikipedia.org/wiki/Philosophy'

while keep_crawling(article_history, target_url):
    
    # make http request to get the html from the last page in article_history
    # and then make the html string into a BeautifulSoup object
    r = requests.get(article_history[-1])
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # list of <a> tags within the first paragraph
    a_tags = soup.p.find_all('a')
    if a_tags:
        # if the list if non-empty, get the first link and append it to article_history
        first_link = 'https://en.wikipedia.org' + a_tags[0].get('href')
        print(first_link)
        article_history.append(first_link)
        print(article_history)
        # delay for 2 seconds so we don't overload wikipedia with requests
        time.sleep(2)
    
    break