from functools import lru_cache


@lru_cache
def read(path):
    print('Iniciando')
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
    return []
