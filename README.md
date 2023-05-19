# ABOUT

This script was created to aid me in creating files used during classes.

Making this script saves me a lot of time as I don't have to worry about inconsistencies or errors in new files that get made.

It is also possible and extremely easy to extend the functionality of the script if necessary.

# DESCRIPTION

- `filemaker.py` - Main script.

# WHAT IT DOES

- Generates files for the following languages:
    - Python
    - LaTeX
    - C++
    - Java
- Python, C++ and Java files have a documentation block with a name field, an ID number field, a date field, and a description field as well as basic boilerplate code for each language. You can choose if the documentation block is included when the file is made.
- LaTeX files have the boilerplate code used when I make documents.

# REQUIREMENTS

- Python

# HOW TO USE

## Through Command Line

```shell
cd path/to/directory
git clone https://github.com/Heck21/filemaker.git
cd filemaker
python filemaker.py
```

## Manually

1. Download zip from repository to desired directory.
2. Unzip file.
3. Run `filemaker.py`

# CUSTOMIZATION

## Name and ID Number

When you run the script for the first time, you will notice that the name and ID field in whatever is generated is empty.

If you want to have your name and ID number automatically added to the documentation block when generating a file, place them in the `name` and `id_num` variables in the script.

## Tab Sizes

The functions that create the Python, C++ and Java files have a `tab_size` parameter that is used when generating the boilerplate code. 

The default is 4 but if you want to change it, just change the `tab_size` parameter's default value for each function in the script.

# REGARDING WHERE FILES GET MADE

Because I use the current working directory to create the paths, wherever you install the script is where all files will be made.

If you want files to be made in whatever directory you're in the following can be done:

## On Windows

Assuming you are using Powershell and have a personal profile script, the following can be added to it:

```powershell
function Run-Filemaker {
    $pythonExecutable = "python"
    $pythonScriptPath = "path/to/script"

    $command = "$pythonExecutable $pythonScriptPath"
    Invoke-Expression -Command $command
}
```

You can change the name of the function if you want.

An alias can be made from this function if needed.

## On Unix

At the moment I don't use any Unix systems but I assume an alias can be made for whatever shell you use to run the script.

<br>

This makes it so that you can run the script from the command line. Wherever the script is ran is where the file will be created.