"""
Python Programming & Linear Programming Optimization

A comprehensive toolkit demonstrating:
- String manipulation algorithms
- Array algorithms without built-in functions
- Multi-criteria decision analysis
- Integer Linear Programming optimization

Author: Victor Prefa
Course: SIG720 Machine Learning - Deakin University
"""

from .string_operations import reverse_student_id, reverse_student_id_from_index
from .array_algorithms import (
    find_max_custom, 
    find_second_max_custom,
    find_distinct_custom,
    count_smaller_numbers,
    analyze_student_id
)
from .linear_programming import (
    brute_force_solve,
    check_constraints,
    calculate_objective,
    verify_constraints
)

__all__ = [
    'reverse_student_id',
    'reverse_student_id_from_index',
    'find_max_custom',
    'find_second_max_custom',
    'find_distinct_custom',
    'count_smaller_numbers',
    'analyze_student_id',
    'brute_force_solve',
    'check_constraints',
    'calculate_objective',
    'verify_constraints'
]

__version__ = '1.0.0'
__author__ = 'Victor Prefa'
