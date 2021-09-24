#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


get_maximums = lambda numbers : [max(x) for x in numbers]

join_integers = lambda numbers : int("".join([str(x) for x in numbers]))

def generate_prime_numbers(limit):
	nombres, premiers = [x for x in range(2,limit+1)], []
	while nombres:
		premiers.append(nombres.pop(0))
		nombres = [x for x in nombres if x%premiers[-1]]
	return premiers

combine_strings_and_numbers = lambda strings, num_combinations, excluded_multiples=1 : [x+str(y) for y in range(1, num_combinations+1, excluded_multiples) for x in strings ]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
