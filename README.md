# Advent of Code 2019

This is the first year where I participate in Advent of Code. I am still in the process of learning Python. Hence my solutions are written in Python.


| Day           | Exercise                            | Note | 
| ------------- | ----------------------------------  | ---- |
| 1             | The Tyranny of the Rocket Equation  | Solution to exercise 2 can be simplified with expression assignment from Python 3.8 | 
| 2             | 1202 Program Alarm                  | Deep copying a list is fast using slice notation |
| 3             | Crossed Wires                       |   |
| 4             | Secure Container                    | I need to work on regex :-) I managed to solve first puzzle using regex but not the second one. I assume that you need to use " lookaround" regex to solve the second problem. |

# Installation and execution of solution and tests
Clone repository into a new folder and execute
```shell
python -m venv .venv
```
to create a virtual environment and activate it by calling

```shell
. .venv/bin/activate
```

Install required packages with
```shell
pip install -r requirements.txt
```

and run tests including solutions with
```shell
pytest
```
