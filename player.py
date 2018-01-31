# Program Name  : TV Program Player
# Created by    : Francois Mindiel
# Created date  : 28/04/16
# Version       : 1.0
# Description   : This program uses the back end program to create programme info.
#                 It relies on tvprogram.py for that matter, and accesses the latter's functions.
#

# Update History:

import tvprogram        # to be able to use class and functions from tvprogram.py

#Creating 3 objects (program1, program2, program3) and passing parameter values.

program1 = tvprogram.TVProgram("Arrested Development", "The Cabin Show", 3, 1, "Level-headed son Michael Bluth takes over family affairs after his father is imprisoned.\n"
                                                                               "\t\t\t\t But the rest of his spoiled, dysfunctional family are making his job unbearable. ",
                               "comedy", 5, 30, "http://www.imdb.com/title/tt0367279/?ref_=ttep_ep_tt",
                               "http://cdn.pastemagazine.com/www/blogs/lists/header-arrested-development-season-4-first-full-trailer.jpg",
                               "https://www.youtube.com/watch?v=3iWrB_Nkcvc",
                               "Mitchell Hurwitz", "Ron Howard",
                               ["Jason Bateman", "Portia de Rossi", "Will Arnett", "Michael Cera"])

program2 = tvprogram.TVProgram("Heroes", "episode 1", 1, 1, "Common people discover that they have super powers. Their lives intertwine as a devastating event must be prevented.",
                               "Science fiction", 3, 50, "http://www.imdb.com/title/tt0813715/",
                               "http://cdn2.denofgeek.us/sites/denofgeekus/files/heroes-characters.jpg",
                               "https://www.youtube.com/watch?v=x1eKGa0gHwI",
                               "Tim Kring", "Tim Kring",
                               ["Hayden Panettiere", "Jack Coleman", "Milo Ventimiglia", "Masi Oka", "Zachary Quinto", "Ali Larter "])

program3 = tvprogram.TVProgram("How I met your mother", "Last Forever", 9, 23, "A father recounts to his children, through a series of flashbacks, the journey he\n"
                                                                               "\t\t\t\t and his four best friends took leading up to him meeting their mother. ",
                               "Comedy", 4, 45, "http://www.imdb.com/title/tt0460649/",
                               "http://i.imgur.com/yIl0fRI.jpg",
                               "https://www.youtube.com/watch?v=BbcpmuNbxSU",
                               " Carter Bays", "Craig Thomas",
                               ["Josh Radnor", "Jason Segel", "Cobie Smulders", "Neil Patrick Harris", "Alyson Hannigan"])

### This is to display program1 on the screen ###

print(program1.__doc__)         # displays the description of the class used

program1.print_title()          # calling display functions for program1
program1.print_star_rating()
program1.print_episode_title()
program1.print_description()
program1.print_genre()
program1.print_duration()
program1.print_image_url()
program1.print_vid_url()
program1.print_web_url()
program1.print_actor_list()

program1.open_web_url()         # opens website for program1

### This is to display program2 on the screen ###

print(program2.__doc__)         # displays the description of the class used

program2.print_title()          # calling display functions for program2
program2.print_star_rating()
program2.print_episode_title()
program2.print_description()
program2.print_genre()
program2.print_duration()
program2.print_image_url()
program2.print_vid_url()
program2.print_web_url()
program2.print_actor_list()

program2.open_vid_url()         # opens youtube sample video for program2

### This is to display program3 on the screen ###

print(program3.__doc__)         # displays the description of the class used

program3.print_title()          # calling display functions for program3
program3.print_star_rating()
program3.print_episode_title()
program3.print_description()
program3.print_genre()
program3.print_duration()
program3.print_image_url()
program3.print_vid_url()
program3.print_web_url()
program3.print_actor_list()

program3.open_image_url()       # opens online picture gallery for program3







# This is the end of the program
# Francois Mindiel ID 2804582
# This work is protected by copyright laws!