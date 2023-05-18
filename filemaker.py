from datetime import date
from pathlib import Path
import os


def file_check(path: Path) -> Path:
    while True:
        if path.exists():
            print(f"{path} already exists.")

            while True:
                new_name = input("Enter a new file name: ")

                if len(new_name) < 1:
                    print("Filename should not be blank.")
                else:
                    break

            path = Path(str(path).replace(path.stem, new_name))
        else:
            return path


def python(path: Path) -> None:
    path = file_check(path)

    with path.open("w") as f:
        f.write(
            "'''"
            "\nAuthor: Cavin Warren"
            "\nID#: 1908573"
            f"\nDate: {today:%B %d, %Y}"
            "\nDescription: Python code for [PLACEHOLDER]"
            "\n'''"
            "\n\n"
        )


def latex(path: Path) -> None:
    path = file_check(path)

    while True:
        title = input(">>> Enter desired title: ")

        if len(title) < 1:
            print("Title should not be blank.")
        else:
            break

    with path.open("w") as f:
        f.write(
            "\\documentclass[12pt]{article}"
            "\n\\usepackage{amsmath, amsfonts, amsthm, amssymb}"
            "\n\\usepackage{fancyvrb, tcolorbox, geometry, graphicx}"
            "\n\n\\newgeometry{"
            "\n    top=1in,"
            "\n    bottom=1in,"
            "\n    outer=1in,"
            "\n    inner=1in"
            "\n}"
            "\n\n\\theoremstyle{definition}"
            "\n\\newtheorem*{example}{Example}"
            "\n\\newtheorem*{definition}{Definition}"
            f"\n\n\\title{{\\Huge {title}}}"
            "\n\\author{\\huge Cavin Warren}"
            f"\n\\date{{\\large {today:%B %d, %Y}}}"
            "\n\n\\begin{document}"
            "\n\n\\maketitle"
            "\n\\pagenumbering{gobble}"
            "\n\\newpage"
            "\n\\pagenumbering{arabic}"
            "\n\n\n\n\\end{document}"
        )


def cpp(path: Path) -> None:
    path = file_check(path)

    with path.open("w") as f:
        f.write(
            "/*"
            "\nAuthor: Cavin Warren"
            "\nID#: 1908573"
            f"\nDate: {today:%B %d, %Y}"
            "\nDescription: C++ code for [PLACEHOLDER]"
            "\n*/"
            "\n\n"
        )


def java(path: Path) -> None:
    path = file_check(path)

    with path.open("w") as f:
        f.write(
            "/*"
            "\nAuthor: Cavin Warren"
            "\nID#: 1908573"
            f"\nDate: {today:%B %d, %Y}"
            "\nDescription: Java code for [PLACEHOLDER]"
            "\n*/"
            "\n\n"
        )


if __name__ == "__main__":
    today = date.today()

    main_path = Path.home() / "Desktop"
    filepath: Path

    valid_choices = {1, 2, 3, 4}

    while True:
        print(
            "CHOOSE DESIRED FILE TYPE:\n"
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
            filename = input(">>> Enter desired filename: ")

            if len(filename) < 1:
                print("Filename should not be blank.")
            else:
                break

        filepath = main_path / f"{filename}"

        match choice:
            case 1:
                filepath = filepath.with_suffix(".py")
                python(filepath)
            case 2:
                filepath = filepath.with_suffix(".tex")
                latex(filepath)
            case 3:
                filepath = filepath.with_suffix(".cpp")
                cpp(filepath)
            case 4:
                filepath = filepath.with_suffix(".java")
                java(filepath)

        print("\nFile has successfully been created.")

        while True:
            repeat = input("\nDo you want to make another file? (Y/N): ")
            repeat = repeat.upper()
            if repeat not in ["Y", "N"]:
                print("Enter a valid choice.")
            else:
                break

        if repeat == "Y":
            print("\n", end="")
        else:
            print("\n", end="")
            break

    os.system("pause")
