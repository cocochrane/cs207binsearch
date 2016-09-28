
def binary_search(da_array: list, needle, left:int=0, right:int=-1) -> int:
    """
    An algorithm that operates in O(lg(n)) to search for an element
    in an array sorted in ascending order.
    
    Parameters
    ----------
    da_array : list
        a list of "comparable" items sorted in non-descending order
    needle: an item to find in the array; it may or may not
        be in the array
    left: int, optional
        the left index in the array to search from. Default 0
    right: int, optional
        the right index in the array to search to. Default is -1
        in which case we will use the end of the array `len(da_array) - 1`
        
    Returns
    -------
    index: int
        an integer representing the index of `needle` if found, and -1
        otherwise
        
    Notes
    -----
    PRE: `da_array` is a list that is sorted in non-decreasing order (thus items in
        `da_array` must be comparable: implement < and ==)
        - left must be less than or equal to right 
    POST: 
        - `da_array` is not changed by this function (immutable)
        - returns `index`=-1 if `needle` is not in `da_array`
        - returns an int `index ` in [0:len(da_array)] if
          `index` is in `da_array`
    INVARIANTS:
        - If `needle` in `da_array`, needle in `da_array[rangemin:rangemax]`
          is a loop invariant in the while loop below.
          
    Examples
    --------
    >>> input = list(range(10))
    >>> binary_search(input,2) 
    2
    >>> binary_search(input, 4.5)
    -1
    >>> import numpy as np
    >>> binary_search([1,2,np.inf], 2)
    1
    >>> binary_search([1,2,np.inf],np.inf)
    2
    >>> binary_search(input, 2, 3, 1) #shows that algorithm requires left <= right in order for correct solution (pre-condition)
    -1
    >>> binary_search(['a','b','c','d'],'c') #supports types that have notion of == and < 
    2
    >>> binary_search([2,1,5,3,6],3) #shows that breaking sorted precondition leads to incorrect result
    -1
    >>> binary_search([1,1,2,2,3,3,4],3) #finds the second 3- when multiple needles needles, index returned varies
    5
    >>> binary_search([0,1,1,2,2,3,3,4],3) #finds the first 3- when multiple needles needles, index returned varies
    5
    """
    if left==0:
        rangemin = 0
    else:
        rangemin = left
    if right==-1:
        rangemax=len(da_array) - 1
    else:
        rangemax=right
    while True:
        "needle in da_array => needle in da_array[rangemin:rangemax]"   
        if rangemin > rangemax:
            index = -1
            return index
        #If rangemin and rangemax are both very high we do not want overflow,
        #so get the midpoint like this:
        midpoint = rangemin + (rangemax - rangemin)//2
        if da_array[midpoint] > needle:#lower part
            rangemax = midpoint - 1
        elif da_array[midpoint] < needle:
            rangemin = midpoint + 1
        else:
            index = midpoint
            return index

