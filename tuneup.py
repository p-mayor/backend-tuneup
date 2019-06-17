#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "peter mayor"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sortby = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats()
        return result
    return inner


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    formatted_movies = []
    for item in movies:
        formatted_movies.append(item.split('\t')[1])
    seen = {}
    duplicates = []
    # original solution
    # while movies:
    #     movie = movies.pop()
    #     if is_duplicate(movie, movies):
    #         duplicates.append(movie)

    for movie in formatted_movies:
        if movie in seen:
            seen[movie] += 1
            duplicates.append(movie)
        else:
            seen[movie] = 1

    print (duplicates)


@profile
def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    setup = 'from __main__ import find_duplicate_movies'
    """Computes a list of duplicate movie entries"""
    t = timeit.Timer("find_duplicate_movies('movies.txt')", setup)
    print(t)
    repeat_num = 3
    run_num = 3
    result = t.repeat(repeat=repeat_num, number=run_num)
    result = [number/float(run_num) for number in result]
    print(f'Best time across {repeat_num} repeats of {run_num} runs per repeat: {min(result)} sec')
    return min(result)


def main():
    result = timeit_helper()
    # print('Found {} duplicate movies:'.format(len(result)))
    print(result)


if __name__ == '__main__':
    main()
