import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


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
    response_text = html_content
    path_html = ".post-inner > .entry-header > .entry-title a::attr(href)"
    selector = Selector(text=response_text)
    selector_list = selector.css(path_html).getall()
    return selector_list


# scrape_updates(fetch(""))


# Requisito 3
def scrape_next_page_link(html_content):
    response_text = html_content
    path_html = "#main > div > nav > div > a.next.page-numbers::attr(href)"
    selector = Selector(text=response_text)
    selector_list = selector.css(path_html).get()
    return selector_list


# Requisito 4
def scrape_news(html_content):
    response_text = html_content
    path_url = "head > link[rel=canonical]::attr(href)"
    path_title = "h1::text"
    path_timestamp = "ul > li.meta-date::text"
    path_writer = "ul > li.meta-author > span.author > a::text"
    path_reading_time = "ul > li.meta-reading-time::text"
    path_summary = "div.entry-content > p:nth-of-type(1) *::text"
    path_category = "div > a > span.label::text"
    selector = Selector(text=response_text)
    url = selector.css(path_url).get()
    title = selector.css(path_title).get()
    timestamp = selector.css(path_timestamp).get()
    writer = selector.css(path_writer).get()
    reading_time = selector.css(path_reading_time).get()
    summary = selector.css(path_summary).getall()
    category = selector.css(path_category).get()
    dict_page = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int("".join(re.findall(r"\d", reading_time)).strip()),
        "summary": "".join(summary).strip(),
        "category": category,
    }
    return dict_page


# requisito5
def get_tech_news(amount):
    count_notices = 0
    next_count = 0
    list_dict = []
    next_html = ""
    html_content = fetch("https://blog.betrybe.com/")
    page_notices = scrape_updates(html_content)
    count_notices += len(page_notices)
    next_page = scrape_next_page_link(html_content)
    for index in range(0, amount):
        if index <= 11:
            dict_notices = scrape_news(fetch(page_notices[index]))
            list_dict.append(dict_notices)
        if index >= 12:
            if next_count >= 12:
                next_count = 0
                next_page = scrape_next_page_link(next_html)
            next_html = fetch(next_page)
            # print(next_html)
            next_notices = scrape_updates(next_html)
            dict_notices = scrape_news(fetch(next_notices[next_count]))
            list_dict.append(dict_notices)
            next_count += 1

    # print(len(list_dict[:amount]))
    create_news(list_dict[:amount])
    return list_dict[:amount]


# get_tech_news(33)
