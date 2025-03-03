import os


def write_binary(filename: str, string: str) -> None:
    """Function that write a 'utf-8' encoded string to a binary file.

    Parameters
    ----------
    filename : filename of the binary file we want to write the string to
    string : string to encode and write to filename
    """
    if not filename.endswith("bin"):
        filename = filename + ".bin"

    if not os.path.exists("binary_files"):
        os.mkdir("binary_files")

    save_path = f"binary_files/{filename}"
    with open(f"{save_path}.bin", "wb") as file:
        file.write(string.encode())


def read_binary(filename: str) -> str:
    """Function to read the content from a binary file with 'utf-8' encoded string.

    Parameters
    ----------
    filename : path to the file that should be read

    Returns
    -------
    string : decoded string from filename
    """

    with open(filename, "rb") as file:
        string = file.read().decode()
    return string
