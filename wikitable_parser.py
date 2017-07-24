from collections import defaultdict
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import requests

# put the URL for the site here
URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_past_and_future_population'