#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:40:26 2019

@author: sehraelahi
"""

## This is the top level file for running search on the queens cover


import sys
from tree          import *
from queue_search  import *
from queen_cover  import *


def zero_heuristic(state):
    return 0

##code works with all the tests

search(make_queen_problem(1,1), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(3,3), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(4,4), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(5,5), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(5,6), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(6,5), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(10,3), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(3,4), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(4,7), ('A_star', zero_heuristic), 5000, [])
search(make_queen_problem(2,50), ('A_star', zero_heuristic), 5000, [])
