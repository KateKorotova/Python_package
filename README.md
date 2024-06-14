# Char Counter


## Description
`char_counter_katek` is a Python package that counts the number of single characters in a given string or in a file containing a string. This package can be used both as a command-line tool and as a module in your Python projects.

## Usage

### Command Line
After installation, you can use the char_counter command to count single characters. The command can take either a string directly or the path to a file containing the string. If both are provided - file is read. 

#### Count Single Characters in a String
To count the single characters in a provided string, use the --string argument:

`char_counter.py --string "yourstring"`

#### Count Single Characters in a File
To count the single characters in a string contained in a file, use the --file argument:

`char_counter.py --file "path/to/your/file.txt"`

### As a Python Module
You can also use the functions provided by the char_counter package in your Python code:

```
from char_counter import count_single_char

# Example usage of count_single_char
result = count_single_char("yourstring")
print(result)  # Output will be the count of single characters in the string

```

## Running Tests
To run the tests for the char_counter package, use pytest.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Name: Yekatierina Korotova

Email: yekaterina.korotova@gmail.com
