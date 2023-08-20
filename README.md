HTML parse tree:
The first word after the left bracket is HTML tag (in tree structure we call it node). In most cases, tags come in pairs. Of course, there are some exceptions such as line break tag <br> or doc type tag  <!DOCTYPE>. 
Usually the opening tag is just tag name but the closing tag has a slash before the name. Different tag names represent different functionalities. 
In most cases, there are only a few tags that contain information we need, e.g., tag <div> usually defines a table, tag <a> creates a hyperlink (the link is at attribute 'href' and it may skip prefix if the prefix is the same as current URL), tag <img> comes up with a pic (the link is hidden in attribute src), tag <p> or <h1>-<h6> normally contains text. 

The attribute 'find_all' returns all the matched results, '.text' attribute automatically gets all str values inside the current tag.

HTML
JSON

Tools
1.BeautifulSoup