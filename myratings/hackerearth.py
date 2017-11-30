from .scrape import *


def obtainRating(url):
    """Obtains User Rating From Hackerearth Website.
    Arguments:
        url = Url of the User Profile
    Returns:
        Actual ratings if successfully retrieved, NA otherwise
    """
    soup = getSoup(url)
    rating = "NA"

    try:
        ratingDiv = soup.findAll("span", {"class": "track-following-num"})
        rating = ratingDiv[1].text
        if rating == "NA":
            raise Exception("Rating not Found!!")
        return rating
    except Exception as e:
        #print("Cannot Obtain Ratings From Hackerearth")
        #print("Reason :" + str(e))
        return rating
