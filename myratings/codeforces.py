from .scrape import *
import re


def obtainRating(url):
    """Obtains User Rating From Codeforces Website.
    Arguments:
        url = Url of the User Profile
    Returns:
        Actual ratings if successfully retrieved, NA otherwise
    """

    soup = getSoup(url)
    rating = "NA"

    try:
        userRatingInfo = soup.findAll("span", {"class": re.compile("^user-")})
        for info in userRatingInfo:
            try:
                rating = int(info.text)
                break
            except ValueError:
                continue
        if rating == "NA":
            raise Exception("Rating not Found!!")
        return str(rating)
    except Exception as e:
        #print("Cannot Obtain Ratings From CodeForces")
        #print("Reason :" + str(e))
        return rating
