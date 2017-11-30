from .codechef import obtainRating as ccfor
from .codeforces import obtainRating as cfsor
from .hackerearth import obtainRating as heor 

judgesList = ['hackerearth', 'codechef', 'codeforces']

url = {
    'hackerearth': r'https://www.hackerearth.com/@',
    'codechef': r'https://www.codechef.com/users/',
    'codeforces': r'http://codeforces.com/profile/',
}


def obtainRatings(site, reqUrl):
    """ Obtains Rating From Corresponding Site.
    Arguments:
        site = Name of the Site
        reqUrl = Url of the user profile
    Returns:
        Actual ratings if successfully retrieved, NA otherwise
    """

    rating = "NA"
    if site == "codechef":
        rating = ccfor(reqUrl)
    elif site == "codeforces":
        rating = cfsor(reqUrl)
    elif site == "hackerearth":
        rating = heor(reqUrl)
    return rating
