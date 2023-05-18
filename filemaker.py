from datetime import date
from pathlib import Path
from getpass import getpass


def file_check(filepath: Path) -> Path:
    """
    Checks if path to file already exists, allows creation of new path.

    Parameters:
        filepath: Path to file.

    Returns:
        The original path if it does not already exist.

        The altered path if the original path already exists.
    """

    while True:
        if filepath.exists():
            print(f"\n{filepath} already exists.")

            while True:
                new_name = input(">>> Enter a new file name: ")

                if len(new_name) < 1:
                    print("Filename should not be blank.")
                else:
                    break

            suffix = filepath.suffix
            filepath = Path.cwd() / f"{new_name}{suffix}"
        else:
            return filepath


def create_python_file(
    filepath: Path, today: date, name: str = "", id_num: str = ""
) -> None:
    """
    Creates Python file with initial docstring.

    Parameters:
        filepath: Path to file.
        today: Date object.
        name: Name used in docstring. Default: ""
        id_num: ID number used in docstring. Default ""

    Returns:
        Nothing
    """

    filepath = filepath.with_suffix(".py")
    filepath = file_check(filepath)

    with filepath.open("w") as f:
        f.write(
            "'''"
            f"\nAuthor: {name}"
            f"\nID#: {id_num}"
            f"\nDate: {today:%B %d, %Y}"
            "\nDescription: Python code for [PLACEHOLDER]"
            "\n'''"
            "\n\n\n"
        )


def create_latex_file(filepath: Path, today: date, name: str = "") -> None:
    """
    Creates LaTeX file with initial boilerplate code.

    Parameters:
        filepath: Path to file.
        today: Date object.
        name: Name used for author on title page. Default: ""

    Returns:
        Nothing
    """

    filepath = filepath.with_suffix(".tex")
    filepath = file_check(filepath)

    while True:
        title = input(">>> Enter desired title: ")

        if len(title) < 1:
            print("Title should not be blank.")
        else:
            break

    with filepath.open("w") as f:
        f.write(
            "\\documentclass[12pt]{article}"
            "\n\\usepackage{amsmath, amsfonts, amsthm, amssymb}"
            "\n\\usepackage{fancyvrb, tcolorbox, geometry, graphicx}"
            "\n\n\\newgeometry{top=1in, bottom=1in, outer=1in, inner=1in}"
            "\n\n\\theoremstyle{definition}"
            "\n\\newtheorem*{example}{Example}"
            "\n\\newtheorem*{definition}{Definition}"
            f"\n\n\\title{{\\Huge {title}}}"
            f"\n\\author{{\\huge {name}}}"
            f"\n\\date{{\\large {today:%B %d, %Y}}}"
            "\n\n\\begin{document}"
            "\n\n\\maketitle"
            "\n\\pagenumbering{gobble}"
            "\n\\newpage"
            "\n\\pagenumbering{arabic}"
            "\n\n\n\n\\end{document}"
        )


def create_cpp_file(
    filepath: Path, today: date, name: str = "", id_num: str = ""
) -> None:
    """
    Creates C++ file with initial document block.

    Parameters:
        filepath: Path to file.
        today: Date object.
        name: Name used in document block. Default: ""
        id_num: ID number used in document block. Default ""

    Returns:
        Nothing
    """

    filepath = filepath.with_suffix(".cpp")
    filepath = file_check(filepath)

    with filepath.open("w") as f:
        f.write(
            "/*"
            f"\nAuthor: {name}"
            f"\nID#: {id_num}"
            f"\nDate: {today:%B %d, %Y}"
            "\nDescription: C++ code for [PLACEHOLDER]"
            "\n*/"
            "\n\n"
        )


def create_java_file(
    filepath: Path, today: date, name: str = "", id_num: str = ""
) -> None:
    """
    Creates Java file with initial document block.

    Parameters:
        filepath: Path to file.
        today: Date object.
        name: Name used in document block. Default: ""
        id_num: ID number used in document block. Default ""

    Returns:
        Nothing
    """

    filepath = filepath.with_suffix(".java")
    filepath = file_check(filepath)

    with filepath.open("w") as f:
        f.write(
            "/*"
            f"\nAuthor: {name}"
            f"\nID#: {id_num}"
            f"\nDate: {today:%B %d, %Y}"
            "\nDescription: Java code for [PLACEHOLDER]"
            "\n*/"
            "\n\n"
        )


def main() -> None:
    """Main Function"""

    today = date.today()
    filepath: Path

    name: str = ""
    id_num: str = ""

    valid_choices = {1, 2, 3, 4}

    print(f"Current Directory: {Path.cwd()}\n", end="")

    while True:
        print(
            "\nCHOOSE DESIRED FILE TYPE:\n"
            "1. Python\n"
            "2. LaTeX\n"
            "3. C++\n"
            "4. Java"
        )

        while True:
            try:
                choice = int(input(">>> "))
            except ValueError:
                print("Enter a valid choice.")
            else:
                if choice not in valid_choices:
                    print("Enter a valid choice.")
                else:
                    break

        while True:
            filename = input("\n>>> Enter desired filename: ")

            if len(filename) < 1:
                print("Filename should not be blank.")
            else:
                break

        filepath = Path.cwd() / f"{filename}"

        match choice:
            case 1:
                create_python_file(filepath, today, name, id_num)
            case 2:
                create_latex_file(filepath, today, name)
            case 3:
                create_cpp_file(filepath, today, name, id_num)
            case 4:
                create_java_file(filepath, today, name, id_num)

        print("\nFile has successfully been created.")

        while True:
            repeat = input("\nDo you want to make another file? (Y/N): ")
            repeat = repeat.upper()
            if repeat not in ["Y", "N"]:
                print("Enter a valid choice.")
            else:
                break

        if repeat == "N":
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(code="\nExiting...")
    else:
        getpass("\nPress ENTER to exit...")
