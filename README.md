# Leaguer

## Usage
For manual line by line input: `python3 leaguer.py` or `./leaguer.py` if you have python3+ mapped to your python command

For input by file: `python3 leaguer.py <input_file.txt>` or `./leaguer.py <input_file.txt>`

### The Problem
Required: a command-line application that will calculate the ranking table for a
soccer league.

#### Input/output
The input and output will be text. Either using stdin/stdout or taking filenames on the command
line is fine.

The input contains results of games, one per line. See “Sample input” for details.
The output should be ordered from most to least points, following the format specified in
“Expected output”.

Expect that the input will be well-formed. There is no need to add special handling for
malformed input files.

#### The rules
In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points.
If two or more teams have the same number of points, they should have the same rank and be
printed in alphabetical order (as in the tie for 3rd place in the sample data).

#### Guidelines
Written for Python 3.7 and [pytest](https://docs.pytest.org/en/latest/) used for testing

To run all test, ensure pytest in installed (`pip3 install -U pytest`) and run `python3 -m pytest` in the app root directory

#### Platform support
Developed on Manjaro Linux resulting in Unix line feed (LF) for line endings.

#### Sample input:
||
|---|
| Lions 3, Snakes 3 |
| Tarantulas 1, FC Awesome 0 |
| Lions 1, FC Awesome 1 |
| Tarantulas 3, Snakes 1 |
| Lions 4, Grouches 0 |

#### Expected output:
||
|---|
|1. Tarantulas, 6 pts|
|2. Lions, 5 pts|
|3. FC Awesome, 1 pt|
|3. Snakes, 1 pt|
|5. Grouches, 0 pts|