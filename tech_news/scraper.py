import requests
import time 
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    headers = {"user-agent": "Fake user-agent"}
    # perfect_url = url.replace('app', 'blog')
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        elif response.status_code != 200:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    response_text = html_content
    path_html = ".post-inner > .entry-header > .entry-title a::attr(href)"
    print()
    selector = Selector(text=response_text)
    selector_list = selector.css(path_html).getall()
    return selector_list


# scrape_updates(fetch(""))


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
