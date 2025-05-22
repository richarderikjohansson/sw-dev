import argparse
from course_package.calculator import IntCalculator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)

    args = parser.parse_args()
    IntCalculator(args.input).run()
