from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    job = []
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        the_file = DictReader(file, delimiter=",", quotechar='"')

        for file in the_file:
            job.append(file)

    return job
