from bs4 import BeautifulSoup
import requests

def getHtmlCode(url): # Returns all the html code from the URL
	r = requests.get(url)
	return r.text

