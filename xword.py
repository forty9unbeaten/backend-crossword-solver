#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""
__author__ = "Rob Spears (GitHub: Forty9Unbeaten)"

import sys

if sys.version_info[0] < 3:
    raise Exception('Hey amigo, gotta run Python 3...')


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
    blank_indices = [i for i in range(
        0, len(user_word)) if user_word[i] == ' ']
    for word in word_list:
        if len(word) == len(user_word):
            split_word = list(word)
            for i in blank_indices:
                split_word[i] = ' '
            if ''.join(split_word) == user_word:
                yield word


def print_matches(matches):
    print('\n*** Possible Matches ***')
    print('________________________\n')
    for word in matches:
        print('-- ' + word + '\n')


def main():
    with open('dictionary.txt') as f:
        word_list = f.read().split()

    input_message = ['Please enter a word to solve.\n',
                     'Use spaces to signify unknown letters: ']

    user_word = get_input(''.join(input_message)).lower()
    matches = get_matches(word_list, user_word)
    print_matches(matches)


if __name__ == '__main__':
    main()
