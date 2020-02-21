from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    """Temporarily Suppress Console Output in Python
    src: http://thesmithfam.org/blog/2012/10/25/temporarily-suppress-console-output-in-python/

    Example
    -------
    print("Now you see it")
    with suppress_stdout():
        print("Now you don't")
    >>> Now you see it
    """
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout