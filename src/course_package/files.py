from pathlib import Path
import hashlib
from collections import defaultdict
from typing import Callable, Generator, List
import os


def find_files(base_dir: str, pattern: str) -> Generator:
    """Find files

    Args:
        base_dir: Base directory
        pattern: Pattern to look for

    Returns:
        Path to files
    """
    return Path(base_dir).rglob(pattern)


def save_duplicates(files_list: Generator, filename: str) -> None:
    """Save duplicate files

    Args:
        lists_of_files: List of files
        filename: File name
    """
    if not os.path.exists("duplicates"):
        os.makedirs("duplicates")
    path = Path("duplicates") / filename

    with open(path, "w") as fh:
        for files in files_list:
            fh.writelines(str(files) + "\n")


def duplicates(base_dir: str, pattern: str, save: bool = False) -> Generator:
    """Find duplicate files from the full content

    Args:
        base_dir: [TODO:description]
        pattern: [TODO:description]
        save: [TODO:description]

    Returns:
        List of duplicate files
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
    base_dir: str, pattern: str, hash_func: Callable, save: bool = False
) -> Generator:
    """Wrapper to apply hashing to find duplicate

    Args:
        base_dir: base directory
        pattern: pattern to look for
        hash_func: hash function
        save : bool if saving files

    Returns:
        Files
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
    """sha256 hash in 4kB chunks

    Args:
        path: Path to file

    Returns:
        Digest from hash
    """
    hasher = hashlib.sha256()
    with open(path, "rb") as file:
        chunk = file.read(4096)
        while chunk:
            hasher.update(chunk)
            chunk = file.read(4096)
        return hasher.hexdigest()


def sha256_filedigest(path: Path) -> str:
    """sha256 hash

    Args:
        path: Path to file

    Returns:
        Digest from file
    """
    with open(path, "rb") as file:
        return hashlib.file_digest(file, "sha256").hexdigest()


def sha256_path(path: Path) -> str:
    """sha256 hash

    Args:
        path: Path to file

    Returns:
        Digest from file
    """
    hasher = hashlib.sha256()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()


def md5_path(path: Path) -> str:
    """md5 hash

    Args:
        path: Path to file

    Returns:
        Digest of file
    """
    hasher = hashlib.md5()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()


def blake2b_path(path: Path) -> str:
    """blake2b hash

    Args:
        path: Path to file

    Returns:
        Disest of file
    """
    hasher = hashlib.blake2b()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()


def blake2s_path(path: Path) -> str:
    """blake2s hash

    Args:
        path: Path to file

    Returns:
        Digest of file
    """
    hasher = hashlib.blake2s()
    bstr = path.read_text().encode("utf-8")
    hasher.update(bstr)
    return hasher.hexdigest()
