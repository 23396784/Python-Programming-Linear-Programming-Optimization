"""
Array Algorithms Module

Custom array operations WITHOUT using built-in functions:
- Find maximum and its index
- Find second maximum
- Find distinct elements
- Count smaller numbers for each element

Author: Victor Prefa
Course: SIG720 Machine Learning - Deakin University
"""

from typing import List, Tuple, Optional


def find_max_custom(digits: List[int]) -> Tuple[int, int]:
    """
    Find maximum value and its index WITHOUT using max() or sort().
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - constant extra space
    
    Parameters
    ----------
    digits : list
        List of integer digits
        
    Returns
    -------
    tuple
        (maximum_value, index_of_maximum)
        
    Examples
    --------
    >>> find_max_custom([2, 2, 5, 1, 8, 7, 9, 1, 3])
    (9, 6)
    """
    if not digits:
        raise ValueError("Cannot find maximum of empty list")
    
    maximum = digits[0]
    max_index = 0
    
    for i in range(1, len(digits)):
        if digits[i] > maximum:
            maximum = digits[i]
            max_index = i
    
    return maximum, max_index


def find_second_max_custom(digits: List[int]) -> Optional[int]:
    """
    Find second maximum value WITHOUT using max() or sort().
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - constant extra space
    
    Parameters
    ----------
    digits : list
        List of integer digits
        
    Returns
    -------
    int or None
        Second maximum value, or None if not enough distinct values
        
    Examples
    --------
    >>> find_second_max_custom([2, 2, 5, 1, 8, 7, 9, 1, 3])
    8
    """
    if len(digits) < 2:
        return None
    
    # Initialize first and second maximum
    first_max = second_max = None
    
    for num in digits:
        if first_max is None or num > first_max:
            second_max = first_max
            first_max = num
        elif num != first_max and (second_max is None or num > second_max):
            second_max = num
    
    return second_max


def find_distinct_custom(digits: List[int]) -> List[int]:
    """
    Find distinct elements preserving order WITHOUT using set().
    
    Time Complexity: O(n²) - for each element, check if seen before
    Space Complexity: O(n) - for storing distinct elements
    
    Parameters
    ----------
    digits : list
        List of integer digits
        
    Returns
    -------
    list
        List of distinct digits in original order
        
    Examples
    --------
    >>> find_distinct_custom([2, 2, 5, 1, 8, 7, 9, 1, 3])
    [2, 5, 1, 8, 7, 9, 3]
    """
    distinct = []
    
    for digit in digits:
        # Check if digit already in distinct list
        found = False
        for d in distinct:
            if d == digit:
                found = True
                break
        
        if not found:
            distinct.append(digit)
    
    return distinct


def count_smaller_numbers(digits: List[int]) -> List[int]:
    """
    For each digit, count how many numbers in the array are smaller.
    
    Time Complexity: O(n²) - nested comparison
    Space Complexity: O(n) - for result array
    
    Parameters
    ----------
    digits : list
        List of integer digits
        
    Returns
    -------
    list
        Count of smaller numbers for each position
        
    Examples
    --------
    >>> count_smaller_numbers([1, 2, 3, 4, 5, 6])
    [0, 1, 2, 3, 4, 5]
    >>> count_smaller_numbers([2, 2, 5, 1, 8, 7, 9, 1, 3])
    [2, 2, 5, 0, 7, 6, 8, 0, 4]
    """
    smaller_counts = []
    
    for current_digit in digits:
        count = 0
        for other_digit in digits:
            if other_digit < current_digit:
                count += 1
        smaller_counts.append(count)
    
    return smaller_counts


def analyze_student_id(student_id: str) -> dict:
    """
    Complete analysis of student ID digits.
    
    Parameters
    ----------
    student_id : str
        Student ID string
        
    Returns
    -------
    dict
        Analysis results including max, second max, distinct, and smaller counts
    """
    # Extract digits
    digits = [int(char) for char in student_id if char.isdigit()]
    
    # Perform analysis
    max_val, max_idx = find_max_custom(digits)
    second_max = find_second_max_custom(digits)
    distinct = find_distinct_custom(digits)
    smaller_counts = count_smaller_numbers(digits)
    
    return {
        'digits': digits,
        'maximum': max_val,
        'max_index': max_idx,
        'second_maximum': second_max,
        'distinct_digits': distinct,
        'distinct_count': len(distinct),
        'smaller_counts': smaller_counts
    }


def demo():
    """Demonstrate array algorithms."""
    print("Array Algorithms Demo (No Built-in Functions)")
    print("=" * 50)
    
    student_id = "s225187913"
    results = analyze_student_id(student_id)
    
    print(f"\nStudent ID: {student_id}")
    print(f"Digits: {results['digits']}")
    print(f"\nMaximum: {results['maximum']} at index {results['max_index']}")
    print(f"Second Maximum: {results['second_maximum']}")
    print(f"\nDistinct digits: {results['distinct_digits']}")
    print(f"Distinct count: {results['distinct_count']}")
    print(f"\nSmaller counts: {results['smaller_counts']}")
    
    # Detailed breakdown
    print("\nDetailed Position Analysis:")
    for i, (digit, count) in enumerate(zip(results['digits'], results['smaller_counts'])):
        print(f"  Position {i}: Digit {digit} has {count} smaller numbers")
    
    print("\nDemo completed!")


if __name__ == "__main__":
    demo()
