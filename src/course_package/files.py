from pathlib import Path
import hashlib
from collections import defaultdict
from typing import Callable
import os


def find_files(base_dir: str, pattern: str) -> Path:
    """Function to find paths from base directory with pattern

    Parameters
    ----------
    base_dir: directory where search start
    pattern: pattern to include
    """
    return Path(base_dir).rglob(pattern)


def save_duplicates(lists_of_files: list, filename: str) -> None:
    """Function to save list of files to file

    Parameters
    ----------
    lists_of_files: the lists of files containing duplicate content
    filename: name of the file to be created
    """
    if not os.path.exists("duplicates"):
        os.makedirs("duplicates")
    path = Path("duplicates") / filename

    with open(path, "w") as fh:
        for files in lists_of_files:
            fh.writelines(str(files) + "\n")


def duplicates(base_dir: str = None, pattern: str = None, save: bool = False) -> list:
    """Function to find files with duplicate content

    A method to find files containing duplicate content using a dictionary

    Parameters
    ----------
    base_dir: directory where search start
    pattern: pattern to include
    save: boolean deciding if saving to file
    """
    files = find_files(base_dir, pattern)
    dictionary = defaultdict(list)
    for path in files:
        dictionary[path.read_text(encoding="utf-8")].append(path.name)

    files = [val for val in dictionary.values() if len(val) > 1]
    if save:
        filename = "nohash.txt"
        save_duplicates(files, filename)
    return files


def duplicate_with_hashing(
    base_dir: str = None, pattern: str = None, hash_func: Callable = None, save=False
) -> list:
    """Function to find files with duplicate content

    A method to find files containing duplicate content using a dictionary
    and hashing the content

    Parameters
    ----------
    base_dir: directory where search start
    pattern: pattern to include
    function: which hashing function to use
    save: boolean deciding if saving to file
    """
    files = find_files(base_dir, pattern)
    dictionary = defaultdict(list)

    for path in files:
        content_hash = hash_func(path)
        dictionary[content_hash].append(path.name)

    files = [val for val in dictionary.values() if len(val) > 1]

    if save:
        filename = hash_func.__name__ + ".txt"
        save_duplicates(files, filename)
    return files


def sha256_chunks(path: Path) -> str:
    """Function to hash the content

    This function uses the sha256 hasing algorithm
    and the content is hashed in 4kB chunks

    Parameters
    ----------
    path: path object to the file

    Returns
    -------
    : hashed content
    """
    hasher = hashlib.sha256()
    with open(path, "rb") as file:
        chunk = file.read(4096)
        while chunk:
            hasher.update(chunk)
            chunk = file.read(4096)
        return hasher.hexdigest()


def sha256_filedigest(path: Path) -> str:
    """Function to hash content

    This function uses the sha256 hashing algorithm
    and uses hashlibs file_digest function to handle
    the hasing

    Parameters
    ----------
    path: path object to the file

    Returns
    -------
    : hashed content
    """
    with open(path, "rb") as file:
        return hashlib.file_digest(file, "sha256").hexdigest()


def sha256_path(path):
    """Function to hash content

    This function uses the sha256 hashing algorithm
    and updates the hasher with content read from Path
    objects method read_text

    Parameters
    ----------
    path: path object to the file

    Returns
    -------
    : hashed content
    """
    hasher = hashlib.sha256()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()


def md5_path(path):
    """Function to hash content

    This : Callablefunction uses the md5 hashing algorithm
    and updates the hasher with content read from Path
    objects method read_text

    Parameters
    ----------
    path: path object to the file

    Returns
    -------
    : hashed content
    """
    hasher = hashlib.md5()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()


def blake2b_path(path):
    """Function to hash content

    This function uses the blake2b hashing algorithm
    and updates the hasher with content read from Path
    objects method read_text

    Parameters
    ----------
    path: path object to the file

    Returns
    -------
    : hashed content
    """
    hasher = hashlib.blake2b()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()


def blake2s_path(path):
    """Function to hash content

    This function uses the blake2s hashing algorithm
    and updates the hasher with content read from Path
    objects method read_text

    Parameters
    ----------
    path: path object to the file

    Returns
    -------
    : hashed content
    """
    hasher = hashlib.blake2s()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()
