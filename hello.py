#!/usr/bin/env python3
"""
A simple hello world program for learning GitHub.
Try modifying this file and committing your changes!
"""

def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"

def main():
    """Main function to demonstrate basic Python."""
    print(greet())
    print(greet("GitHub"))
    print("\nWelcome to GitHub learning!")
    print("Try modifying this file and see the changes in git diff")

if __name__ == "__main__":
    main()
