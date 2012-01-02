from urllib import urlopen
from BeautifulSoup import BeautifulSoup as BS
from BeautifulSoup import Comment

def read_page ( url ):
    """Given a URL, download the contents of the page and return a Beautiful
    Soup object of the parsed HTML.  The Beautiful Soup object can then be
    used to traverse the document tree or for searching elements. Examples:

        page = read_page(some_url)
        table = page.find('table', {'id':'results'})
        rows = table.findAll('tr')
        first_row = rows[0]
        first_child = first_row.findChild()
    """
    page = urlopen(url)
    html = page.read()
    return BS(''.join(html))

def remove_comments ( element, debug=False ):
    """Given a BeautifulSoup Element, remove any comments from it.
        Takes optional param debug (boolean) which prints the contents
        deleted.
    """
    comments = element.findAll(text=lambda text:isinstance(text, Comment))
    removed = [comment.extract() for comment in comments]
    if debug:
        for x in removed: print x
