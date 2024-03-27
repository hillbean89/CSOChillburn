"""
Lists and Unittest Lab
Updated By: Colin
CSCI 110 Lab
Date: 03/14/2024

Read and solve - Pet: https://open.kattis.com/problems/pet 

Algorithm steps:
    1. Create a list to store the total scores of each contestant
    2. Repeat 5 times:
        i. Read the input line
        ii. Split the line into a list of numbers
        iii. Convert the list of strings into a list of ints
        iv. Sum the list of ints
        v. Append the sum to the list of scores
    3. Find the max score in the list of scores
    4. Find the index of the max score in the list of scores
    5. Print the index of the max score + 1 and the max score
"""

import string
from typing import List
import sys  


def main() -> None:
    """Main function that solves the problem
    """
    # step 1. create a list to store the total scores of each contestant
    scores = []
    # FIXM 1 - repeat step 2-4 5 times
    for i in range(5):
    # FIXM 2 - read the input line as a list of integers using get_data function
        integers=get_data()
    # FIXM 3 - find the sum of scores using list_sum function
        total_socres=(list_sum(integers))

    # FIXM 4 - append the sum to the list of scores

        scores.append(total_socres)

    # FIXM 5 - print the final output calling answer function
    print(answer(scores))


def get_data() -> List[int]:
    """Reads the data from std input and returns it as a list of ints
    Args:
        None
    Returns:
        List[int]: list of ints
    """
    str_nums = input().split()  # list of string numbers
    #  6: convert str_nums as list of ints and return it
    int_nums= list(map(int, str_nums))
    return int_nums


def list_sum(int_nums) -> int:
    """Finds and returns sum of the numbers in the list.
    Args:
        numbers: List[int]: # takes a list of numbers as a parameter

    Returns:
        int: sum of the numbers in the list
    """
    #  7: find the sum of the numbers in the list and return it
    sums=sum(int_nums)
    return sums


def answer(scores: List[int]) -> str:
    """Find and return the answer as a string.
    Args:
        scores (List[int]): List of 5 contestants scores
    Returns:
        str: index of the max score + 1 and the max score as a string
    """
    max_score = max(scores)
    index = scores.index(max_score)
    #  8: return the index+1 and the max number in the list as a string
    sum_scores = f"{index+1} {max_score}"
    return sum_scores


if __name__ == "__main__":
    main()
