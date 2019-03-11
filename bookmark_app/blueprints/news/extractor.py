import newspaper
# from newspaper import Article, Config

config = newspaper.Config()
config.keep_article_html = True


def extract(url):
    """
    Extract data from url

    ":param url: URL of website to scrape"
    :return: dict
    """
    article = newspaper.Article(url=url, config=config)
    article.download()
    print('***************')
    print(url)
    print('***************')
    article.parse()
    return dict(
        title=article.title,
        text=article.text,
        html=article.html,
        image=article.top_image,
        authors=article.authors,
        )


def get_links_on_page(url):
    """
    Get a list of all the links on a url

    ":param: url: URL of webstite to scrape"
    :return: list of newspaper.article.Article objects
    These objects have urls, titles, html etc.
    :return: list
    """
    paper = newspaper.build(url)

    return [link for link in paper.articles]
