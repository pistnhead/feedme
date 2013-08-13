#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""FeedMe

Usage:
    feedme.py
    feedme.py <number-of-people>
    
Status:
    This is a proof-of-concept application as of now,
    only interacts with twitter, and only for one service
    that is available in select cities in India - Faasos.
"""

import logging
#import requests
from docopt import docopt


def plural(word, n=1):
    if n > 1:
        word = word + 's'
    return word


def build_order(docargs):
    """
    Builds order based on selected options. For now things are hardcoded to my daily choices. 
    """
    people = docargs.get('<number-of-people>', 1)
    if not people:
        people = 1
        
    order = '@fassos #faasosnow {people} veg salad {wraps}'.format(wraps=plural('wrap', people),
                                                                   people=people)
    logging.info('Order: %s' % order)
    return order


def main():
    """
    Run when we execute this file as a python script.
    """
    # Setting up logging, you can watch debug.log file for messages.
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    logging.info('Begin Session')
    
    # Setting up docopts, if you don't know about this fantastic library, look it up!
    docargs = docopt(__doc__, version='FeedMe 0.1')
    logging.info('Arguments: %s' % docargs)
    order = build_order(docargs=docargs)
    
    # For now print the order to screen, later we'll be sending it to twitter automatically
    print order

if __name__ == '__main__':
    main()
