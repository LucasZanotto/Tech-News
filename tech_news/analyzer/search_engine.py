from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    list_search = []
    search_titles = search_news({"title": {"$regex": title, "$options": "i"}})
    for info in search_titles:
        list_search.append((info["title"], info["url"]))
    return list_search


# print(search_by_title("idqwtyu91761dt90d1"))


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    list_search = []
    search_categories = search_news(
        {"category": category.lower().capitalize()}
    )
    for info in search_categories:
        list_search.append((info["title"], info["url"]))
    return list_search


print(search_by_category("tecnologia"))
