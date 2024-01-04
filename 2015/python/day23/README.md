# Approach
### Data format

Store each line of the input file as a list of split parts in an array. Then we can just run through the instructions
from top to bottom as needed.

### Part 1
> _What is the value in register b when the program in your puzzle input is finished executing?_

INCREDIBLY straighforward -- especially for one so late in the calendar! Literally just keep a map of registers and implement
each operation. RUn through the input and it's done.

### Part 2
> _Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?_

Do the exact same thing but start with register `a` with a value of `1`.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |               0 |
