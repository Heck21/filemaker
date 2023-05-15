from datetime import date
import os


def file_check(path: str) -> str:
    while True:
        if os.path.exists(path):
            print("That file already exists.")

            while True:
                new_name = input("Enter a new file name: ")

                if len(new_name) < 1:
                    print("Filename should not be blank.")
                else:
                    break

            path = path[: (path.rfind("\\") + 1)] + new_name + path[path.rfind(".") :]
        else:
            return path


def c_schoolwork(path: str) -> None:
    path = file_check(path)

    with open(path, "w") as f:
        f.write("/*")
        f.write("\nAuthor: Cavin Warren")
        f.write("\nID#: 1908573")
        f.write(f"\nDate: {today:%B %d, %Y}")
        f.write("\nDescription: C code for [PLACEHOLDER]")
        f.write("\n*DESC*")
        f.write("\n*/")
        f.write("\n\n#include <stdio.h>")
        f.write("\n\nint main() {")
        f.write("\n\n\n    return 0;")
        f.write("\n}")


def python(path: str) -> None:
    path = file_check(path)

    with open(path, "w") as f:
        f.write("'''")
        f.write("\nAuthor: Cavin Warren")
        f.write("\nID#: 1908573")
        f.write(f"\nDate: {today:%B %d, %Y}")
        f.write(f"\nDescription: Python code for [PLACEHOLDER]")
        f.write("\n*DESC*")
        f.write("\n'''")
        f.write("\n\n")


def latex(path: str) -> None:
    path = file_check(path)

    while True:
        title = input(">>> Enter desired title: ")

        if len(title) < 1:
            print("Title should not be blank.")
        else:
            break

    with open(path, "w") as f:
        f.write("\\documentclass[12pt]{article}")
        f.write("\n\\usepackage{amsmath, amsfonts, amsthm, amssymb}")
        f.write("\n\\usepackage{fancyvrb, tcolorbox, geometry, graphicx}")
        f.write("\n\n\\newgeometry{")
        f.write("\n    top=1in,")
        f.write("\n    bottom=1in,")
        f.write("\n    outer=1in,")
        f.write("\n    inner=1in")
        f.write("\n}")
        f.write("\n\n\\theoremstyle{definition}")
        f.write("\n\\newtheorem*{example}{Example}")
        f.write("\n\\newtheorem*{definition}{Definition}")
        f.write(f"\n\n\\title{{\\Huge {title}}}")
        f.write("\n\\author{\\huge Cavin Warren}")
        f.write(f"\n\\date{{\\large {today:%B %d, %Y}}}")
        f.write("\n\n\\begin{document}")
        f.write("\n\n\\maketitle")
        f.write("\n\\pagenumbering{gobble}")
        f.write("\n\\newpage")
        f.write("\n\\pagenumbering{arabic}")
        f.write("\n\n\n\n\\end{document}")


if __name__ == "__main__":
    today = date.today()

    while True:
        print(
            "CHOOSE DESIRED FILE TYPE:\n"
            "1. C\n"
            "2. Python\n"
            "3. LaTeX\n"
            "4. C++\n"
            "5. Java"
        )

        while True:
            try:
                choice = int(input(">>> "))
            except ValueError:
                print("Enter a valid choice.")
            else:
                if choice not in [1, 2, 3]:
                    print("Enter a valid choice.")
                else:
                    break

        while True:
            filename = input(">>> Enter desired filename: ")

            if len(filename) < 1:
                print("Filename should not be blank.")
            else:
                break

        match choice:
            case 1:
                path = f"C:\\Users\\cavin\\Desktop\\main\\SCHOOL\\Programming 2 - CMP1025\\Codes\\C\\{filename}.c"
                c_schoolwork(path)
            case 2:
                path = f"C:\\Users\\cavin\\Desktop\\main\\CODING PRACTICE\\Python\\{filename}.py"
                python(path)
            case 3:
                path = f"C:\\Users\\cavin\\Desktop\\main\\SCHOOL\\Discrete Mathematics - MAT1008\\Discrete Mathematics Notes\\{filename}.tex"
                latex(path)

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
