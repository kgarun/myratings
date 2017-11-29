import requests
from bs4 import BeautifulSoup


def getSoup(url):
    """Returns BeatifulSoup object of the given URL.
    Arguments:
        url = URL of the corresponding webpage
    Returns:
        BeatifulSoup object of the given URL
    """
    try:
        r = requests.get(
            url,
            headers={
                "referer":
                url,
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
                 AppleWebKit/537.36 (KHTML, like Gecko) \
                 Chrome/39.0.2171.95 Safari/537.36'
            })
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup
    except Exception as e:
        print(str(e))
