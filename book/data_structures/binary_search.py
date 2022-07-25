from typing import Union 
import numpy as np
Array = np.ndarray


def binary_search(arr: Union[list, Array], target: int) -> Union[int, None]:
    """Returns the index of 'arr' containing 'target' if one exists, 
    or None if the target doesn't exist.

    This method assumes there are no repeated elements in 'arr'.
    """

    if not arr:
        return None

    low_idx, high_idx = 0, len(arr) - 1    
    while low_idx <= high_idx:
        pivot = low_idx + ((high_idx - low_idx) // 2)
        if target > arr[pivot]:
            low_idx = pivot + 1
        elif target < arr[pivot]:
            high_idx = pivot - 1 
        else:
            return pivot
    return None

def binary_search_with_duplicates(
    arr: Union[list, Array], target: int) -> Union[int, None]:
    """Returns the index of the first instance of 'target' in 'arr' if it is 
    contained in the array, or returns None if 'target' is not in 'arr'.
    """
    a_target_idx: Union[int, None] = binary_search(arr=arr, target=target)  
    if a_target_idx is None:
        return None
    
    # Check left neighbors for duplicates
    pivot: int = a_target_idx
    while target == arr[pivot - 1]:
        pivot -= 1
    return pivot

#%%

class TestBinarySearch:

    def test_empty_array(self):
        """Empty array should return None"""
        in_arr: list = []
        assert binary_search(arr=in_arr, target=5) is None
    
    def test_odd_arr(self):
        """Array has odd number of elements and no duplicates."""
        in_arr: list[int] = [i for i in range(9)]
        targets: list[int] = in_arr
        for target in targets:
            search_idx: int = binary_search(arr=in_arr, target=target)
            assert search_idx is not None
            assert search_idx == in_arr.index(target)

    def test_even_arr(self):
        """Array has even number of elements and no duplicates."""
        in_arr: list[int] = [i for i in range(10)]
        targets: list[int] = in_arr
        for target in targets:
            search_idx: int = binary_search(arr=in_arr, target=target)
            assert search_idx is not None
            assert search_idx == in_arr.index(target)
        
    def test_duplicate_elements(self):
        """Array with multiple instances of the same value."""
        in_arr: list[int] = sorted([1, 2, 3] * 4)
        targets: list[int] = [1, 2, 3]
        for target in targets:
            search_idx: int = binary_search_with_duplicates(
                arr=in_arr, target=target)
            assert search_idx == in_arr.index(target)