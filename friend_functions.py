# friend_functions.py
# ------------
# By MWC Contributors
#
# Each of the functions below expects a list of dictionaries as its first
# argument. Two examples of the expected input are provided in people.family
# and people.friends.

# Your job is to complete these functions. Remove the NotImplementedError from
# each and instead write code which returns the expected values. 

def count_people(people):
    """Counts the number of people. 
    
        >>> count_people(family)
        5
        >>> count_people(friends)
        10
    """
    raise NotImplementedError()

def get_email(people, name):
    """Returns the named person's email address. If there is no such person, returns None.

        >>> get_email(family, "Tad Winters")
        "ligula.aenean@hotmail.edu"
        >>> get_email(friends, "Tad Winters")
        None
    """
    raise NotImplementedError()

def count_favorite_colors(people, name):
    """Returns the number of colors liked by the named person. If there is no such person, returns None.

        >>> count_favorite_colors(family, "Tad Winters")
        2
        >>> count_favorite_colors(family, "Raphael Chambers")
        1
    """
    raise NotImplementedError()

def people_who_like_color(people, color):
    """Returns a list containing only those people who like the given color.
        >>> people_who_like_color(family, "yellow")
        [
            {
	        "name": "Walker Hurley",
	        "email": "auctor.odio@icloud.ca",
                "favorite_colors": ["red", "yellow", "blue", "orange"],
            },
            {
	        "name": "Clementine Joseph",
	        "email": "hendrerit@aol.co.uk",
                "favorite_colors": ["yellow", "aqua", "black"],
            }
        ]
        >>> people_who_like_color(family, "indigo")
        []
    """
    raise NotImplementedError()

def count_people_who_like_color(people, color):
    """Returns the number of people who like a given color. 
    
        >>> count_people_who_like_color(family, "red")
        2
        >>> count_people_who_like_color(family, "orange")
        1
    """
    raise NotImplementedError()

def get_color_dict(people):
    """Returns a dict showing how many people like each color. 
    Any color liked by any of the people will be included, and only colors
    liked by someone will be included. The order of items in the dict doesn't matter.

        >>> get_color_dict(family)
        {
            "aqua": 2,
            "red": 2,
            "blue": 2,
            "black": 2,
            "white": 1,
            "grey": 1,
            "yellow": 2,
            "orange": 1,
        }
    """
    raise NotImplementedError()
        




