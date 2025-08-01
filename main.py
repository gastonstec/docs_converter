# main.py
# This file serves as the entry point for the console application.
from console import main

# Ensure the console application runs when this script is executed directly.
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error occurred:", e)
        raise e