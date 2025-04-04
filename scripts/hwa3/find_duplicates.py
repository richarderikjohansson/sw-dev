import argparse
import time

from course_package.files import (
    blake2b_path,
    blake2s_path,
    duplicate_with_hashing,
    duplicates,
    md5_path,
    sha256_chunks,
    sha256_filedigest,
    sha256_path,
)

PATH = "a_few_files"
PATTERN = "*.txt"
DESC_MAP = {
    "nohash": "Find duplicates without hashing content",
    "sha256_fd": "Find duplicates using hashed content with sha256 and digest file directly",
    "sha256_chunks": "Find duplicates using hashed content with sha256 in 4kB chunks",
    "sha256": "Find duplicates using hashed content with sha256 from Path object",
    "md5": "Find duplicates using hashed content with md5 from Path object",
    "blake2b": "Find duplicates using hashed content with blake2b from Path object",
    "blake2s": "Find duplicates using hashed content with blake2s from Path object",
}
FUNCTION_MAP = {
    "nohash": duplicates,
    "sha256_fd": lambda save: duplicate_with_hashing(
        PATH, PATTERN, hash_func=sha256_filedigest, save=save
    ),
    "sha256_chunks": lambda save: duplicate_with_hashing(
        PATH, PATTERN, hash_func=sha256_chunks, save=save
    ),
    "sha256": lambda save: duplicate_with_hashing(
        PATH, PATTERN, hash_func=sha256_path, save=save
    ),
    "md5": lambda save: duplicate_with_hashing(
        PATH, PATTERN, hash_func=md5_path, save=save
    ),
    "blake2b": lambda save: duplicate_with_hashing(
        PATH, PATTERN, hash_func=blake2b_path, save=save
    ),
    "blake2s": lambda save: duplicate_with_hashing(
        PATH, PATTERN, hash_func=blake2s_path, save=save
    ),
}


def main():
    save_desc = "Saves the files found with name of the first argument"
    time_desc = "Times the execution of the function"
    print_desc = "Prints the duplicate files to stdout"
    description = "Program to find files with duplicate content"
    parser = argparse.ArgumentParser(add_help=True, description=description)
    subparsers = parser.add_subparsers(
        dest="method", required=True, help="Methods available"
    )

    for method in FUNCTION_MAP.keys():
        description = DESC_MAP.get(method, "")
        subparser = subparsers.add_parser(
            method, help=description, description=description
        )
        subparser.add_argument("-s", "--save", action="store_true", help=save_desc)
        subparser.add_argument("-t", "--timeit", action="store_true", help=time_desc)
        subparser.add_argument("-p", "--printit", action="store_true", help=print_desc)

    args = parser.parse_args()
    func = FUNCTION_MAP[args.method]

    if args.method == "nohash":
        st_ex = time.time()
        dupes = func(PATH, PATTERN, args.save)
        execution_time = time.time() - st_ex
    else:
        st_ex = time.time()
        dupes = func(save=args.save)
        execution_time = time.time() - st_ex

    if args.timeit:
        print(f"Execution time: {execution_time} s")

    if args.printit:
        for files in dupes:
            print(files)


if __name__ == "__main__":
    main()
