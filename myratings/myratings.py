"""Displays the Rating Summary of the User from various CP Sites.
    Mode 1:
        In this mode user handles and ratings are stored in the disk so that
        the user need not enter his/her handle everytime and also provides
        comparison between old and new ratings.It the default mode.
    Mode 2:
        If it is not possible to maintain log, users can still view their
        ratings by simply selecting competitive programming site option number
        and entering handle.
"""

import os
import errno
import fileinput
from .judges import *


def manageLog():
    """ Manages the handle folder (for persistence data where the id of the
    user in various Competitive Programming site is stored.
    Returns:
        True = Upon successfully creating handle folder and subfiles
        False = Otherwise
    """
    configureReq = False
    if not os.path.isdir("handle"):
        configureReq = True
        try:
            os.makedirs("handle")  # Creating handle Folder

            with open('handle/log.txt',
                      'w') as log:  # Creating and Initializing Log File
                for judge in judgesList:
                    log.write(judge + " " + "0\n")

        except OSError as e:
            print("Cannot Manage Handle Folder\nReason: ", end="")
            if e.errno == errno.EACCES:
                print("Permission denied")
            elif e.errno == errno.ENOSPC:
                print("No space left on device")
            elif e.errno == errno.EROFS:
                print("Read-only file system")
            else:
                print(str(e))
            return False

    for judge in judgesList:  # Creating Log file for each judge
        filename = judge + '.txt'
        filepath = "handle/" + filename
        if not os.path.exists(filepath):
            open(filepath, 'w').close()

    if configureReq:
        configure()

    return True


def configure():
    """Helps to set the Userid and Judge Preferences.
    """

    for judge in judgesList:
        print("Do you want to add " + judge + "?? (y/n) ", end="")
        response = input()
        if response.lower() == "y":
            with open("handle/" + judge + ".txt", 'w') as log:
                print("Enter your handle: ", end="")
                response = input()
                log.write(response + " NA")  # Updating user Handle

            for line in fileinput.input(
                    "handle/log.txt", inplace=1):  # Updating Log File
                print(line.replace(judge + " 0\n", judge + " 1\n"), end="")


def getRatings():
    """Obtains the Ratings summary of the User and Updates respective Log File.
    Returns:
        rating = a list of lists(site,oldrating,newrating)
    """

    rating = []
    userHandleError = []

    with open('handle/log.txt', 'r') as log:
        for line in log:
            site, preference = line[:-1].split(" ")# Splitting Site and Preference
            if preference == "1":
                userId, oldRating, newRating = None, None, None
                with open('handle/' + site + '.txt', 'r') as siteHandle:
                    for info in siteHandle:
                        userId, oldRating = info.split(" ")  # Obtaining UserId and Ratings

                reqUrl = url[site] + userId  # Constructing Request URL
                newRating = obtainRatings(site, reqUrl)  # Obtaining Latest Rating
                if(newRating == "NA"):
                    userHandleError.append(site)
                else:
                    rating.append([site, oldRating, newRating])

                if newRating != "NA":  # Updating LogFile
                    if oldRating == "NA" or int(oldRating) != int(newRating):
                        with open('handle/' + site + '.txt','w') as siteHandle:
                            siteHandle.write(userId + " " + str(newRating))

    if len(userHandleError) > 0:
        print("\nPlease enter correct user handle of the following site(s):")
        for errhandle in userHandleError:
            print("   ==> "+errhandle)        

        print("\nUse following command to config handle:\n myratings config\n\n")

    return rating


def printRatingSummary(ratings):
    """Prints rating Summary.
    Arguments:
        rating =  a list of lists(site,oldrating,newrating)
    """

    print("\n     Site       OldRating   NewRating  Changes")

    for rating in ratings:
        site = rating[0]
        oldRating = "NA"
        newRating = "NA"
        change = "NA"

        if rating[1] != "NA":
            oldRating = int(rating[1])
        if rating[2] != "NA":
            newRating = int(rating[2])
        if oldRating != "NA" and newRating != "NA":
            change = newRating - oldRating

        print("{:^15} {:^10} {:^10} {:^10}".format(site, oldRating, newRating, change))


def onlineRatings():
    """Displays the Latest rating of the user.No log file is maintained.
    """

    counter = 1
    ptr = None
    print("Please Select one of the following options")
    for judge in judgesList:
        print(str(counter) + " ==> " + judge)
        counter += 1

    while True:
        print("Select any option.Press 'Q' to quit")
        ptr = input()  # Inputting Option

        try:
            ptr = int(ptr)
            if ptr < 1 or ptr >= counter:  # Doesnt fit in the limit
                raise Exception("Quitting....")
            else:
                site = judgesList[ptr - 1]
                reqUrl = url[site]
                print("Enter Your " + site + " Handle: ", end="")
                handle = str(input())
                reqUrl += handle
                print("Your " + site + " ratings : " +
                      obtainRatings(site, reqUrl))

        except Exception as e:
            print("Wish you High Ratings!!")
            break  # Breaks infinite loop


def main():
    """ Main function of the Module. """

    args = os.sys.argv

    if len(args) > 1:
        if args[1].lower() == "config":
            configure() # Calls method that configure user handle
        else:
            print("Usage:\n myratings (or) \n myratings config ")

    if manageLog() is True:  # Mode 1
        ratings = getRatings()
        printRatingSummary(ratings)
    else:  # Mode 2
        print("Still You can view your ratings :)")
        onlineRatings()


if __name__ == "__main__":
    main()
