HTML parse tree:
The first word after the left bracket is HTML tag (in tree structure we call it node). In most cases, tags come in pairs. Of course, there are some exceptions such as line break tag <br> or doc type tag  <!DOCTYPE>. 
Usually the opening tag is just tag name but the closing tag has a slash before the name. Different tag names represent different functionalities. 
In most cases, there are only a few tags that contain information we need, e.g., tag <div> usually defines a table, tag <a> creates a hyperlink (the link is at attribute 'href' and it may skip prefix if the prefix is the same as current URL), tag <img> comes up with a pic (the link is hidden in attribute src), tag <p> or <h1>-<h6> normally contains text. 
The HTML tag for the hidden link is <script>.

The attribute 'find_all' returns all the matched results, '.text' attribute automatically gets all str values inside the current tag.

Python: 
There is a built-in library called 're'. There are a couple of functions inside this module. But for web scraping, 're.findall' and 're.search' are commonly used. 
re.findall returns a list of all the matched words and re.search returns a regex object. 
We simply apply attribute re.search('','').group() to concatenate the text together.
regex - look-ahead and look-behind   (?<=) and (?=)
If the content you are looking for is always behind a comma and before a question mark. You can simply do     (?<=\,)\S*(?=\?)

Data you can work with when scraping data
    1.HTML
    2.JSON
    3.Regular Expression

Tools
1.BeautifulSoup
2.Selenium
3.Chrome Webdriver
4.Firefox Webdriver
5.Scrapy