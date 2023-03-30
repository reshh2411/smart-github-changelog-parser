#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""regex_check.py: takes list from main.py and returns true/false based on the conditions"""

__author__ = "Reshhmaa B"
__date__ = "March 31, 2023"
__status__ = "Development"

import re


def true_false_regex(regex1_py, regex2_py, diff_matches_list):
    """
    regex1: to match the comments
    regex2: to match the comment
    diff_matches_list: list of all changes
    return: true or false

    This function returns true or false depending on the changes made in source codes.
    Prints True if only the comments are changed and false if source lines are changed.
    """
    for elements in diff_matches_list:
        if not re.search(regex1_py, elements) or re.search(regex2_py, elements):
            # return False
            print(False)
            break
    else:
        print(True)
        # return True
