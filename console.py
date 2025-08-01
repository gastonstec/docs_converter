# console.py
# This file is part handles command-line arguments for console application.
import argparse

# Function to parse command-line arguments
def main():
    parser = argparse.ArgumentParser(description="File processing application")
    parser.add_argument("--source_uri", type=str, help="File path or URI to the source data")
    args = parser.parse_args()

    if args.source_uri:
        print(f"Hello, {args.source_uri}! This app received an argument.")
    else:
        print("Hello! This app can take arguments. Try --source_uri <your source path>.")