### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nurlan-Aliev/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Nurlan-Aliev/python-project-50/actions)
[![Action Status](https://github.com/Nurlan-Aliev/python-project-50/actions/workflows/check_test.yml/badge.svg)](https://github.com/Nurlan-Aliev/python-project-50/actions/workflows/check_test.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/b446b81f1d5f47f4bc24/maintainability)](https://codeclimate.com/github/Nurlan-Aliev/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b446b81f1d5f47f4bc24/test_coverage)](https://codeclimate.com/github/Nurlan-Aliev/python-project-50/test_coverage)

# Welcome Generate Difference

This package allows you to generate the differences between two files json or yaml.</br>
And also display the result in three different forms Stylish, Plain, JSON.

### Stylish
Default format. The output is in the format of a string formatted as a dictionary.</br>
Status change to be placed before the key.

|        Status         | Meaning                                                         |
|:---------------------:|-----------------------------------------------------------------|
|       **+ Key**       | Key isn't in first file second file and was added in the second |
|       **- key**       | Key is in first file second file and was removed in seconds     |
| **- key </br> + key** | The key is present in both files with different value           |
|       **key**         | The key is present in both files with the same value            |

### Plain
Plain displays the result in text form. Specifies a property (if the property
is nested, the path to the root is displayed) the status of the change.</br>
If the property was added, the path, status and value are indicated</br>
If changed, the path is indicated and how the value has changed.

### JSON
The output was in JSON format. With value as a dictionary with two keys status and value

|     Status     | Meaning                                                         | 
|:--------------:|-----------------------------------------------------------------|
|   **added**    | Key isn't in first file second file and was added in the second |
|  **removed**   | Key is in first file second file and was removed in seconds     |
|  **updated**   | The key is present in both files with different value           |
| **not_change** | The key is present in both files with the same value            |

## Example of using different formats
[![asciicast](https://asciinema.org/a/8W4EZsgqduZMrZniN9JRbhtAw.svg)](https://asciinema.org/a/8W4EZsgqduZMrZniN9JRbhtAw)


 ## Installation
Clone the repository and install manually.
```bash
$ git clone https://github.com/Nurlan-Aliev/python-project-50.git
$ cd python-project-50
```

#### Install using pip
```bash
$ python3 -m build
$ python3 -m pip install --user dist/*.whl
```

## Start Game

For start using enter gendiff name of first file name of second file.</br>
Use -f (plain, json) for choose format 
```bash
$ gendiff first_file.json second second_file.json
$ gendiff -f plain first_file.json second second_file.json
$ gendiff -f json first_file.json second second_file.json
```