import dryscrape
from bs4 import BeautifulSoup

session = dryscrape.Session()

def getSoup(url):
    """Returns BeatifulSoup object of the given URL.
    Arguments:
        url = URL of the corresponding webpage
    Returns:
        BeatifulSoup object of the given URL
    """
    try:
        session.visit(url)
        response = session.body()
        session.reset()
        soup = BeautifulSoup(response, "lxml")
        return soup
    except Exception as e:
        print(str(e))
