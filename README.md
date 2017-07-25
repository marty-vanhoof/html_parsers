This is a basic Python script for parsing the html from wikipedia tables and getting the data into a nice form.  The script first converts the data into a Python dictionary and then into a Pandas dataframe.  Pandas dataframes are especially nice for doing data analysis.

This script uses Python 3.6.1 and the following modules:

- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](http://pandas.pydata.org/)
- [requests](http://docs.python-requests.org/en/master/)
- [defaultdict](https://docs.python.org/2/library/collections.html#collections.defaultdict)