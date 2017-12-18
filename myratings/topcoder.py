from .scrape import *


def obtainRating(url):
    """Obtains User Rating From Topcoder Website.
    Arguments:
        url = Url of the User Profile
    Returns:
        Actual ratings if successfully retrieved, NA otherwise
    """

    soup = getSoup(url)
    rating = "NA"

    try:
        ratingDiv = soup.findAll("div", {"class": "rating"})
        rating = ratingDiv[0].text
        roundedRating = round(float(rating))
        if rating == "NA":
            raise Exception("Rating not Found!!")
        return roundedRating
    except Exception as e:
        #print("Cannot Obtain Ratings From Topcoder")
        #print("Reason :" + str(e))
        return rating
