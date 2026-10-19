def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    if value is None:
        return False

    if isinstance(value, (int, float, complex)):
        return value!=0
    if isinstance(value, str):
        return len(value)>0
    if isinstance(value, (list, tuple, dict, set)):
        return len(value)>0


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for value in values:
        if is_truthy(value) == True:
            return value

"""
NOTES - Which values are truthy and falsy?
Here are the rules you need to implement.
Data type	Falsy values	Truthy values
None	        None	           —
Numbers	     0, 0.0, 0j	        Any nonzero number
Strings	    "" (empty string)	"hello", "0", " "
Lists	        []	            [1], [0]
Tuples	        ()	             (1,)
Dictionaries	{}	           {"a": 1}
Sets	      set()	            {1, 2}
The key rule: Empty collections are falsy, but non-empty collections are truthy, regardless of their contents.

"""
