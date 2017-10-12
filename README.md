1. [wikitable_parser.py](https://github.com/marty-vanhoof/html_parsers/blob/master/wikitable_parser.py) is a Python script for parsing the html from wikipedia tables and getting the data into a nice form.  The script first converts the data into a Python dictionary and then into a Pandas dataframe.  Pandas dataframes are especially nice for doing data analysis.  This script uses Python 3.6.1 and the following modules:

- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](http://pandas.pydata.org/)
- [requests](http://docs.python-requests.org/en/master/)
- [defaultdict](https://docs.python.org/2/library/collections.html#collections.defaultdict)

2. [wiki_web_crawl.py](https://github.com/marty-vanhoof/html_parsers/blob/master/wiki_web_crawl.py) is a Python script (work in progress) that will implement an interesting experiment by repeatedly following the first link on each wikipedia page.  Apparently clicking on the first link in a wikipedia article and then repeatedly clicking the first link on each subsequent page will usually lead to the Philosophy article.  See [here](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy).  