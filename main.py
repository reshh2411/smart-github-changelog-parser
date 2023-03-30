#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""main.py: takes inputs of directory and programming language, diffs the repo
and checks if there are differences in the comments using regexes"""

__author__ = "Reshhmaa B"
__date__ = "March 31, 2023"
__status__ = "Development"

import re
import argparse
from pathlib import Path
from subprocess import PIPE, Popen
from regex_check import true_false_regex


def default_function():

    def py_regex_function(diff_matches_list):

        """
        this function is called when the input language is python
        """

        # regex for matching differences in the comments (condition - true)
        regex1_py = r'.*[#].*[+]}|[#].*[-]]'

        # regex for matching differences in the comments (condition - false)
        regex2_py = r'{[+[#]+}|[[]-#-]'

        true_false_regex(regex1_py, regex2_py, diff_matches_list)
        print()

    def ccpp_regex_function(diff_matches_list):

        """
        this function is called when the input language is c or c++
        """

        # regex for matching differences in the comments (condition - true)
        regex1_ccpp = r'.*[\/\/].*[+]}|[\/\/].*[-]]'

        # regex for matching differences in the comments (condition - false)
        regex2_ccpp = r'{[+]\/\/[+]}|[[]-\/\/-]'

        true_false_regex(regex1_ccpp, regex2_ccpp, diff_matches_list)
        print()

    def diff_function(path_argument, language_argument):

        """
        path_argument: directory input
        language_argument: programming language input
        """

        # capturing of git diff output

        git_diff_command = 'git diff -U1 --word-diff'
        with Popen(git_diff_command, cwd=path_argument, stderr=PIPE, stdout=PIPE, shell=True) as process:
            diff_var = process.communicate()[0].decode("utf=8")
        regex_to_match_diff_header = re.findall("^@@.*@@[^@]+", diff_var, re.MULTILINE)

        for diff_header_matches in regex_to_match_diff_header:

            # list of diff output

            diff_list = diff_header_matches.split("\n")
            diff_list2 = list(filter(None, diff_list))

            # regex to capture only the changes made in the comments and source codes from diff_list2 and making a list

            diff_matches_list = []
            pattern = re.compile(r'.*[-]]|.*[+]}')

            for elements in diff_list2:
                if pattern.search(elements):
                    diff_matches_list.append(elements)

            # calling functions according to the input of the programming language

            if language_argument == "python" or language_argument == "py":
                print(diff_list2)
                print(diff_matches_list)
                py_regex_function(diff_matches_list)

            elif language_argument == "c" or language_argument == "c++":
                print(diff_list2)
                print(diff_matches_list)
                ccpp_regex_function(diff_matches_list)

            else:
                print("Wrong choice of language.")
                break

    def path_function():
        
        """
        this functions checks whether the input directory is a git repository
        """
        
        path_argument = Path(args.directory_path)
        git_repository = list(path_argument.glob("*.git"))
        
        language_argument = args.language
        
        if len(git_repository) == 0:
            print("No Git repository found!")
        else:
            diff_function(path_argument, language_argument)

    path_function()


if __name__ == '__main__':

    # getting the directory path and language as command line arguments

    # initializing Parser
    parser = argparse.ArgumentParser()

    # adding Arguments
    parser.add_argument("directory_path", help="Enter the path to the directory")
    parser.add_argument("language", help="Enter the programming language (python/py/c/c++)")

    args = parser.parse_args()
    
    default_function()





