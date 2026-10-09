#!/usr/bin/env python3
"""
Simple Task Manager Utility
Created for Git Practice Exercises
"""

import sys

def show_banner():
    print("==============================")
    print("      MY AWESOME TO-DO LIST        ")
    print("==============================")

def display_help():
    print("Commands:")
    print("  list         - Show all tasks")
    print("  add <task>   - Add a new task")
    print("  help         - Show this help message")

def main():
    show_banner()
    
    # Dummy starting tasks for version control practice
    tasks = [
        "Learn git init and status",
        "Practice git add and commit",
        "Explore git branches"
    ]

    if len(sys.argv) < 2:
        print("\nNo command provided.")
        display_help()
        return

    command = sys.argv[1].lower()

    if command == "list":
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"  {index}. {task}")
    elif command == "add" and len(sys.argv) > 2:
        new_task = " ".join(sys.argv[2:])
        tasks.append(new_task)
        print(f"\nSuccessfully added task: '{new_task}'")
    else:
        print(f"\nUnknown command: '{command}'")
        display_help()

if __name__ == "__main__":
    main()