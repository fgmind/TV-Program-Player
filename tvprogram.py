# Program Name  : TV Program Backend
# Created by    : Francois Mindiel
# Created date  : 28/04/16
# Version       : 1.0
# Description   : This program is the back end system, used to create objects for storing programmes.
#                 It creates the objects, with specific parameters, along with some required functions.
#

# Update History:
import webbrowser       # used to open a url in the web browser

class TVProgram(object):            # class used to create objects, with initialisation
    """
*************************************************************************************************
This class stores details about TV shows, such as the title, duration, actor list, and much more!
*************************************************************************************************
    """

    def __init__(self, program_title="", program_episode_title="", program_season=0,
                 program_episode=0, program_description="", program_genre="", program_num_stars=0,
                  program_duration=0, program_weburl="", program_imageurl="", program_vidurl="",
                 program_director="", program_writer="", program_actor_list=[]):

        # getting values from imported parameters
        self.title = program_title
        self.episode_title = program_episode_title
        self.season = program_season
        self.episode = program_episode
        self.description = program_description
        self.genre = program_genre
        self.num_stars = program_num_stars
        self.duration = program_duration
        self.weburl = program_weburl
        self.imageurl = program_imageurl
        self.vidurl = program_vidurl
        self.director = program_director
        self.writer = program_writer
        self.actor_list = program_actor_list

    def print_title(self):                                  # prints title
        print("TV Title:\t\t", self.title)

    def print_episode_title(self):                          # prints episode title
        print("episode title:\t", self.episode_title)

    def print_description(self):                            # prints description
        print("Description:\t", self.description)

    def print_genre(self):                                  # prints genre
        print("Genre:\t\t\t", self.genre)

    def print_duration(self):                               # prints duration in minutes
        print("Duration:\t\t", self.duration, "minutes")

    def print_image_url(self):                              # prints link to image gallery
        print("image url:\t\t", self.imageurl)

    def print_web_url(self):                                # prints link to website
        print("Website url:\t", self.weburl)

    def print_vid_url(self):                                # prints link to youtube video
        print("Sample video:\t", self.vidurl)

    def open_image_url(self):                               # opens image gallery in web browser
        webbrowser.open(self.imageurl)

    def open_web_url(self):                                 # opens website in browser
        webbrowser.open(self.weburl)

    def open_vid_url(self):                                 # opens youtube video in browser
        webbrowser.open(self.vidurl)

    def print_actor_list(self):                             # prints list of actors, with a count in front
        print("List of Actors:")
        count = 1
        for actors in self.actor_list:
            print("\t\t\t\t", count, actors)
            count = count + 1

    def print_star_rating(self):                            # prints stars to represent quality of show
        print("Star Rating:\t", "*" * self.num_stars)







# This is the end of the program
# Francois Mindiel ID 2804582
# This work is protected by copyright laws!