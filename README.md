Account creds must be defined in the data/existing_user.json file. 
To run tests system must have corresponding webdriver for browser:
Chrome - chromedriver, Firefox - geckodriver, etc. 

For example:

Run test module via default browser Chrome:

```$ pytest tests/test_blog.py```

Run specific class or single test method:

```$ pytest tests/test_blog.py::TestBlog``` or 

```$ pytest tests/test_blog.py::TestBlog::test_post_blog```

Run test module via specific browser:

```$ pytest --browser=firefox tests/test_blog.py```


Code convention:

Use PEP-8, but with:
1) 100 symbols hard wrap.
2) Full typing. If something imported in file just for typing - we must put it in "if TYPE_CHECKING:" construction.
3) All data transfers must be done through dto object and fixture for it.
4) Every test groups in blocks GIVEN/WHEN/THEN.