# Approach
### Data format

Read each line of input into an array so I can process each character in each line one by one to generate the code.

### Part 1
> _What is the bathroom code?_

Really very simple. I initially just kept a current number variable and if it gets a `U` instruction, subtract 1 unless that puts it below 0...
likewise, if it gets a `R` instruction, just add 1 unless the modulo ends up being 1 (because that means we were at the end of a row).

Using just simple arithmetic on a number counter let me easily solve this first part.

### Part 2
> _Using the same instructions in your puzzle input, what is the correct bathroom code?_

Obviously my super simplistic math approach to part 1 didn't work here, but it really wasn't much harder. I just created
an array to match the keypad. I then did the same type of arithmetic as before, but added an additional check to see if the value
at the end position was ` `, which signified I couldn't move there. Once I implemented this part of the puzzle, I went back and
rewrote part 1 to use the same thing, just so that the solution I have now will work with any keypad layout as long as you
supply the keypad.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
