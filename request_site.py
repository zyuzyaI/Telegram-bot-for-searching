"""Search on www.olx.ua products for search terms and return
a list of 5 new products that do not see the previous search."""

import requests
from bs4 import BeautifulSoup
import shelve
