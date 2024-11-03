from pages.base import WebPage, PageElement


class MainPage(WebPage):

    _page_uri = "/"
    _title_is = "" #Twitter. It’s what’s happening / Twitter

    sign_in_button = PageElement(xpath="//a[@data-testid='loginButton']")
