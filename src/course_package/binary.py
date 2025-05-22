import os


def write_binary(filename: str, string: str) -> None:
    """Write content to binary file

    Args:
        filename: name of the file
        string: content to write
    """
    if not filename.endswith("bin"):
        filename = filename + ".bin"

    if not os.path.exists("binary_files"):
        os.mkdir("binary_files")

    save_path = f"binary_files/{filename}"
    with open(f"{save_path}.bin", "wb") as file:
        file.write(string.encode())


def read_binary(filename: str) -> str:
    """Read from binary file

    Args:
        filename: file name

    Returns:
        Content from file
    """

    with open(filename, "rb") as file:
        string = file.read().decode()
    return string
