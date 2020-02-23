from time import time
from contextlib import contextmanager
import sys, os
import ipywidgets as wgt
from IPython.display import Image, display


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

@contextmanager
def timing(description: str = 'Time') -> None:
    """[summary]
    
    Parameters
    ----------
    description : str, optional
        [description], by default 'Time'

    Example
    -------
    with timing:
        _ = [1+1 for _ in range(10**5)]
    """
    start = time()
    yield 
    ellapsed_time = time() - start
    print(f'{description}: {ellapsed_time}')


def browse_images(paths):
    def view_image(image_path):
        display(Image(image_path))
    return wgt.interact(view_image, image_path=paths)
