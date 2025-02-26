def write_binary(filename, string):
    """
    Function that write a 'utf-8' encoded string
    to a binary file

    Args:
        filename (str): filename of the binary file we want
                        to write the string to
        string (str): string to encode and write to filename
    """
    with open(f"{filename}.bin", "wb") as file:
        file.write(string.encode())


def read_binary(filename):
    """
    Function to read the content from a binary file with 
    'utf-8' encoded string.

    Args:
        filename (str): path to the file that should be read

    Returns:
        string (str): decoded string from filename
    

    """
    with open(filename, "rb") as file:
        string = file.read().decode()
    return string
