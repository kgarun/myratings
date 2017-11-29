import codechef
import codeforces
import hackerearth

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
        rating = codechef.obtainRating(reqUrl)
    elif site == "codeforces":
        rating = codeforces.obtainRating(reqUrl)
    elif site == "hackerearth":
        rating = hackerearth.obtainRating(reqUrl)
    return rating
