#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""
__author__ = "Rob Spears (GitHub: Forty9Unbeaten)"

# YOUR HELPER FUNCTION GOES HERE


def get_input(input_message):

    # determine if user input is valid
    def is_valid(word):
        if not word:
            return False
        for char in word:
            if not char.isalpha() and char != ' ':
                return False
        return True

    invalid_message = ['There was a problem with your input.\n',
                       'Please make sure you only include known letters \n',
                       'and spaces to indicate unknown letters: ']

    word = input(input_message)
    valid_input = is_valid(word)
    while not valid_input:
        word = input(''.join(invalid_message))
        valid_input = is_valid(word)
    return word


def get_matches(word_list, user_word):


def main():
    with open('dictionary.txt') as f:
        word_list = f.read().split()

    input_message = ['Please enter a word to solve.\n',
                     'Use spaces to signify unknown letters: ']

    user_word = get_input(''.join(input_message)).lower()

    matches = get_matches(word_list, user_word)

    # YOUR ADDITIONAL CODE HERE
    raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
