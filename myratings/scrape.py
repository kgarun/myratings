import dryscrape
from bs4 import BeautifulSoup


def getSoup(url):
    """Returns BeatifulSoup object of the given URL.
    Arguments:
        url = URL of the corresponding webpage
    Returns:
        BeatifulSoup object of the given URL
    """
    try:
        session = dryscrape.Session()
        session.visit(url)
        response = session.body()
        soup = BeautifulSoup(response, "lxml")
        return soup
    except Exception as e:
        print(str(e))
