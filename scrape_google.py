import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession 

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def parse_results(response):
    css_identifier_result = ".fl"
   # css_identifier_title = "h3"
    css_identifier_link = "a"
    css_identifier_text = ".fl"
    
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:

       # output.append(result)
        item = {
            'text': result.find(css_identifier_text, first=True).text,
            'link': 'https://google.com' + result.find(css_identifier_link, first=True).attrs['href']
        }
        # item = {
        #     'title': result.find(css_identifier_title, first=True).text,
        #     'link': result.find(css_identifier_link, first=True).attrs['href'],
        #     'text': result.find(css_identifier_text, first=True).text
        # }



        if item['text'] == '1' or item['text'] == '2' or item['text'] == '3' or item['text'] == '4' or item['text'] == '5' or item['text'] == '6' or item['text'] == '7' or item['text'] == '8' or item['text'] == '9' or item['text'] == '10':  
            output.append(item)
        
    return output

def scrape_google(query):

    # query = urllib.parse.quote_plus(query)
    oldQuery = query.split()
    resultQuery = "+".join(oldQuery)
    # https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+%22python+developer+London
    # response = get_source("https://www.google.co.uk/search?q=" + resultQuery)
    response = get_source("https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+%22" + resultQuery)

    print(parse_results(response))
    # find numbers of pages
    # <a aria-label="Page 3"> 

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                       'https://translate.',
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links 




