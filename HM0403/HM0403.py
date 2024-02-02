import sys
from pathlib import Path
from colorama import Fore, Style, init


init()


def folder_browsing(path, indent=0):
    """File and folder browsing."""
    path = Path(path)

    # Is the root directory
    is_root = not indent

    # Set the colors of files and folders
    if path.is_file():
        print("   " * indent, Fore.BLUE + f"{path.name}" + Style.RESET_ALL)
    elif path.is_dir():
        color = Fore.YELLOW if is_root else Fore.GREEN
        print("   " * indent, color + f"{path.name}" + Style.RESET_ALL)

        # Browsing subfolders and files using recursion
        if path.is_dir():
            items = path.iterdir()
            for item in items:
                folder_browsing(item, indent + 1)
    else:
        print(f"Invalid directory {Fore.RED + f"{path}" + Style.RESET_ALL}!")


def main():
    """Getting data from the user and output."""
    if len(sys.argv) < 2:
        print("Give me the path to the directory!")
    else:
        user_input = sys.argv[1]
        return folder_browsing(user_input)


if __name__ == "__main__":
    main()
