from .scrape import *


def obtainRating(url):
    """Obtains User Rating From Hackerrank Website.
    Arguments:
        url = Url of the User Profile
    Returns:
        Actual ratings if successfully retrieved, NA otherwise
    """

    soup = getSoup(url)
    rating = "NA"

    try:
        ratingDiv = soup.findAll("span", {"class": "txt-navy"})
        print(ratingDiv)
        rating = ratingDiv.text
        roundedRating = round(float(rating))
        if rating == "NA":
            raise Exception("Rating not Found!!")
        return roundedRating
    except Exception as e:
        print("Cannot Obtain Ratings From Hackerrank")
        print("Reason :" + str(e))
        return rating
