# rseprac solutions

### Dr Christopher Melen

The sections below provide explanations for each of the proposed solutions. Please see the added `solutions` folder for the relevant material.

**N.B**: Six problems were mentioned in the preparation guide, but the original repo only seems to contain five problems... Perhaps this is an 'off by one' error.

## Problem 1

See the Bash script `solutions/problem_1/change_file_ext.sh`, which performs the requested task. It takes three positional arguments: `dir` (the path to the directory of files), `from` (the file extension to target) and `to` (the extension to change to).

The script prints a confirmation message when the task has been completed.

To ensure the script is executable modify permissions with:

`chmod 755 solutions/problem_1/change_file_ext.sh`

## Problem 2

See the contents of the `solutions/problem_2` folder.

Two equivalent solutions are provided, one a Bash script the other a Python script. Both take the same arguments: `dir` (the path to the directory of sample files) and `min_values` (the requested minimum number of values per sample file). If a file is found to have fewer than `min_values` values a message indicating this is printed to standard output. A final message is also printed when the task has completed, indicating how many defective files have been detected.

## Problem 3

The provided script was defective, so a corrected version is provided. A text file containing an explanation of general principles for optimising Python code is also provided.

## Problem 4

See the contents of the `solutions/problem_4` folder.

## Problem 5

See the contents of the `solutions/problem_5` folder.

The original `rseprac/problem_5/omni.py` source file has an issue at line 2, where it uses the unicode U+201C character instead of standard ASCII double quotes. This is not recognised by the Python 3 interpreter. Therefore the version given in the preparation guide is taken as the 'source of truth' for this problem.