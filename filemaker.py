from datetime import date
from pathlib import Path
from enum import Enum, auto
from getpass import getpass
import sys


class FileType(Enum):
    PYTHON = auto()
    LATEX = auto()
    CPP = auto()
    JAVA = auto()


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

            filepath = filepath.with_stem(new_name)
        else:
            return filepath


def create_python_file(
    filepath: Path,
    today: date,
    name: str = "",
    id_num: str = "",
    *,
    tab_size: int = 4,
    doc_block: bool = True,
) -> None:
    """
    Creates Python file with document block and boilerplate code.

    Parameters:
        filepath: Path to file.
        today: Date object.
        name: Name used in document block. Default: ""
        id_num: ID number used in document block. Default: ""
        tab_size: Amount of spaces a tab expands to. Default: 4
        doc_block: Add document block. Default: True

    Returns:
        Nothing
    """

    filepath = filepath.with_suffix(".py")
    filepath = file_check(filepath)

    document_block = (
        '"""'
        f"\nAuthor: {name}"
        f"\nID#: {id_num}"
        f"\nDate: {today:%B %d, %Y}"
        "\nDescription: Python code for [PLACEHOLDER]"
        '\n"""'
        "\n\n\n"
    )

    boilerplate = (
        "def main() -> None:"
        "\n\tpass  # PLACEHOLDER"
        '\n\n\nif __name__ == "__main__":'
        "\n\tmain()"
    )

    with filepath.open("w") as f:
        if doc_block:
            f.write(document_block)
        f.write(boilerplate.expandtabs(tab_size))


def create_latex_file(filepath: Path, today: date, name: str = "") -> None:
    """
    Creates LaTeX file with boilerplate code.

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
    filepath: Path,
    today: date,
    name: str = "",
    id_num: str = "",
    *,
    tab_size: int = 4,
    doc_block: bool = True,
) -> None:
    """
    Creates C++ file with document block and boilerplate code.

    Parameters:
        filepath: Path to file.
        today: Date object.
        name: Name used in document block. Default: ""
        id_num: ID number used in document block. Default: ""
        tab_size: Amount of spaces a tab expands to. Default: 4
        doc_block: Add document block. Default: True

    Returns:
        Nothing
    """

    filepath = filepath.with_suffix(".cpp")
    filepath = file_check(filepath)

    document_block = (
        "/*"
        f"\nAuthor: {name}"
        f"\nID#: {id_num}"
        f"\nDate: {today:%B %d, %Y}"
        "\nDescription: C++ code for [PLACEHOLDER]"
        "\n*/\n\n"
    )

    boilerplate = (
        "#include <iostream>"
        "\n\nint main(void)"
        "\n{"
        "\n\t// PLACEHOLDER"
        "\n\n\treturn 0;"
        "\n}"
    )

    with filepath.open("w") as f:
        if doc_block:
            f.write(document_block)
        f.write(boilerplate.expandtabs(tab_size))


def create_java_file(
    filepath: Path,
    today: date,
    name: str = "",
    id_num: str = "",
    *,
    tab_size: int = 4,
    doc_block: bool = True,
) -> None:
    """
    Creates Java file with document block and boilerplate code.

    Parameters:
        filepath: Path to file.
        today: Date object.
        name: Name used in document block. Default: ""
        id_num: ID number used in document block. Default: ""
        tab_size: Amount of spaces a tab expands to. Default: 4
        doc_block: Add document block. Default: True

    Returns:
        Nothing
    """

    filepath = filepath.with_suffix(".java")
    filepath = file_check(filepath)

    document_block = (
        "/*"
        f"\nAuthor: {name}"
        f"\nID#: {id_num}"
        f"\nDate: {today:%B %d, %Y}"
        "\nDescription: Java code for [PLACEHOLDER]"
        "\n*/\n\n"
    )

    boilerplate = (
        f"public class {filepath.stem} {{"
        "\n\tpublic static void main(String[] args) {"
        "\n\t\t"
        "\n\t}"
        "\n}"
    )

    with filepath.open("w") as f:
        if doc_block:
            f.write(document_block)
        f.write(boilerplate.expandtabs(tab_size))


def main() -> None:
    """Main Function"""

    today = date.today()
    main_path = Path.cwd()
    filepath: Path

    """Add info here to make it show up in document block."""
    name: str = ""
    id_num: str = ""

    valid_choices = {member.value for member in FileType}
    response: str = ""
    valid_responses = {"Y", "N"}

    print(f"Current Directory: {main_path}\n", end="")

    while True:
        db: bool = True

        print("\nCHOOSE DESIRED FILE TYPE:")
        for language in FileType:
            print(f"{language.value}.\t{language.name}")

        while True:
            try:
                choice = int(input(">>> "))
                if choice not in valid_choices:
                    raise ValueError
            except ValueError:
                print("Enter a valid choice.")
            else:
                break

        if choice != FileType.LATEX.value:
            while True:
                response = input("\n>>> Include document block? (Y/N): ")
                response = response.upper()
                if response not in valid_responses:
                    print("Enter a valid response.")
                else:
                    break

        if response == "N":
            db = False

        while True:
            filename = input("\n>>> Enter desired filename: ")

            if len(filename) < 1:
                print("Filename should not be blank.")
            else:
                break

        filepath = main_path / f"{filename}"

        match choice:
            case FileType.PYTHON.value:
                create_python_file(filepath, today, name, id_num, doc_block=db)
            case FileType.LATEX.value:
                create_latex_file(filepath, today, name)
            case FileType.CPP.value:
                create_cpp_file(filepath, today, name, id_num, doc_block=db)
            case FileType.JAVA.value:
                create_java_file(filepath, today, name, id_num, doc_block=db)

        print("\nFile has successfully been created.")

        while True:
            response = input("\n>>> Make another file? (Y/N): ")
            response = response.upper()
            if response not in valid_responses:
                print("Enter a valid response.")
            else:
                break

        if response == "N":
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nExiting...")
    else:
        getpass("\nPress ENTER to exit...")
