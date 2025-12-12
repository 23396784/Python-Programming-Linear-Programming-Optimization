"""
String Operations Module

Python string manipulation algorithms with complexity analysis:
- String reversal using slicing
- Index-based partial reversal
- Input validation

Author: Victor Prefa
Course: SIG720 Machine Learning - Deakin University
"""

from typing import List, Union


def reverse_student_id(student_id: str) -> List[str]:
    """
    Reverse the characters of a student ID string into a list.
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n) for the output list
    
    Parameters
    ----------
    student_id : str
        Student ID starting with 's' (e.g., "s225187913")
        
    Returns
    -------
    list
        Reversed characters as individual list elements
        
    Raises
    ------
    ValueError
        If input is not a string starting with 's'
        
    Examples
    --------
    >>> reverse_student_id("s225187913")
    ['3', '1', '9', '7', '8', '1', '5', '2', '2', 's']
    """
    # Input validation
    if not isinstance(student_id, str) or not student_id.lower().startswith('s'):
        raise ValueError("Student ID must be a string starting with 's'")
    
    # Reverse using Python slicing - O(n) operation
    # This leverages Python's optimized string operations
    return list(student_id[::-1])


def reverse_student_id_from_index(student_id: str, start_index: int) -> str:
    """
    Reverse a student ID string starting from a specified index.
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n) for creating new string
    
    Parameters
    ----------
    student_id : str
        Student ID starting with 's'
    start_index : int
        Index from which to start reversing (inclusive)
        
    Returns
    -------
    str
        String with portion from start_index onwards reversed
        
    Raises
    ------
    ValueError
        If student_id doesn't start with 's'
    TypeError
        If start_index is not an integer
    IndexError
        If start_index is out of range
        
    Examples
    --------
    >>> reverse_student_id_from_index("s123456", 3)
    's126543'
    >>> reverse_student_id_from_index("s225187913", 1)
    's319781522'
    """
    # Input validation
    if not isinstance(student_id, str) or not student_id.lower().startswith('s'):
        raise ValueError("Student ID must be a string starting with 's'")
    
    if not isinstance(start_index, int):
        raise TypeError("Index must be an integer")
    
    if start_index < 0 or start_index >= len(student_id):
        raise IndexError(f"Index {start_index} out of range for string length {len(student_id)}")
    
    # Split and reverse using slicing
    # This is the most Pythonic and efficient approach
    unchanged_part = student_id[:start_index]
    part_to_reverse = student_id[start_index:]
    
    return unchanged_part + part_to_reverse[::-1]


def extract_digits(student_id: str) -> List[int]:
    """
    Extract integer digits from a student ID.
    
    Parameters
    ----------
    student_id : str
        Student ID string (e.g., "s225187913")
        
    Returns
    -------
    list
        List of integer digits
        
    Examples
    --------
    >>> extract_digits("s225187913")
    [2, 2, 5, 1, 8, 7, 9, 1, 3]
    """
    return [int(char) for char in student_id if char.isdigit()]


def demo():
    """Demonstrate string operations."""
    print("String Operations Demo")
    print("=" * 40)
    
    student_id = "s225187913"
    
    # Test reverse
    print(f"\nOriginal: {student_id}")
    reversed_list = reverse_student_id(student_id)
    print(f"Reversed list: {reversed_list}")
    
    # Test index-based reversal
    for idx in [1, 3, 5]:
        result = reverse_student_id_from_index(student_id, idx)
        print(f"Reversed from index {idx}: {result}")
    
    # Extract digits
    digits = extract_digits(student_id)
    print(f"\nExtracted digits: {digits}")
    
    print("\nDemo completed!")


if __name__ == "__main__":
    demo()
