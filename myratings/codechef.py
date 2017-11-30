from .scrape import *


def obtainRating(url):
    """Obtains User Rating From Codechef Website.
    Arguments:
        url = Url of the User Profile
    Returns:
        Actual ratings if successfully retrieved, NA otherwise
    """

    soup = getSoup(url)
    rating = "NA"

    try:
        ratingDiv = soup.findAll("div", {"class": "rating-number"})
        rating = ratingDiv[0].text
        if rating == "NA":
            raise Exception("Rating not Found!!")
        return rating
    except Exception as e:
        #print("Cannot Obtain Ratings From CodeChef")
        #print("Reason :" + str(e))
        return rating
