# test_friend_functions.py
# ------------
# By MWC Contributors
# 
# Defines tests for `friend_functions`. 
# Run this program with `python test_friend_functions.py`.
# You don't need to edit thie file.

from unittest import TestCase, main
from people import friends, family
from friend_functions import (
    count_people, 
    get_email, 
    count_favorite_colors, 
    people_who_like_color, 
    count_people_who_like_color,
    get_color_dict,
)

class TestCountPeople(TestCase):
    def test_returns_correct_value(self):
        self.assertEqual(count_people(family), 5)
        self.assertEqual(count_people(friends), 10)

class TestGetEmail(TestCase):
    def test_returns_email_when_person_found(self):
        self.assertEqual(get_email(family, "Perry Calderon"), "mus.donec@outlook.org")
        self.assertEqual(get_email(friends, "Joy Tate"), "risus.a.ultricies@hotmail.org")

    def test_returns_none_when_person_missing(self):
        self.assertEqual(get_email(family, "Ken Kesey"), None)

class TestCountFavoriteColors(TestCase):
    def test_returns_len_favorite_colors_when_person_found(self):
        self.assertEqual(count_favorite_colors(family, "Tad Winters"), 2)
        self.assertEqual(count_favorite_colors(friends,"Connor Rodriguez"), 4)
        self.assertEqual(count_favorite_colors(friends, "Yuli Reynolds"), 0)

    def test_returns_none_when_person_missing(self):
        self.assertEqual(count_favorite_colors(family, "Ken Kesey"), None)

class TestPeopleWhoLikeColor(TestCase):
    def test_returns_correct_length(self):
        self.assertEqual(len(people_who_like_color(family, "blue")), 2)
        self.assertEqual(len(people_who_like_color(family, "purple")), 0)

    def test_returns_full_dicts(self):
        result = people_who_like_color(family, "orange")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["email"], "auctor.odio@icloud.ca")

class TestCountPeopleWhoLikeColor(TestCase):
    def test_returns_correct_count(self):
        self.assertEqual(count_people_who_like_color(friends, "grey"), 2)
        self.assertEqual(count_people_who_like_color(friends, "beige"), 1)
        self.assertEqual(count_people_who_like_color(friends, "cornflower"), 0)

class TestGetColorDict(TestCase):
    def test_returns_correct_dict(self):
        familyExpected = {
            "aqua": 2,
            "red": 2,
            "blue": 2,
            "black": 2,
            "white": 1,
            "grey": 1,
            "yellow": 2,
            "orange": 1,
        }
        friendsExpected = {
            "lime": 1, 
            "grey": 2, 
            "sea foam": 1, 
            "aqua": 2, 
            "teal": 1, 
            "white": 1, 
            "red": 2, 
            "black": 2, 
            "blue": 2, 
            "tan": 1, 
            "sand": 1, 
            "green": 1, 
            "beige": 1, 
            "turquoise": 1, 
            "yellow": 2,
        }
        self.assertEqual(get_color_dict(family), familyExpected)
        self.assertEqual(get_color_dict(friends), friendsExpected)

main()
