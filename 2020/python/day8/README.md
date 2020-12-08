# Approach
I'm not going to lie...I had flashbacks to last year when I started reading this puzzle. The input as well as the
puzzle description immediately reminded me of the `intcode computer` from last year...and that thing was initially
a nightmare. So I approached this puzzle with some aprehension and care.

As I read the problem, it started sounding worse and worse, because it started asking to identify infinite loops
(always a difficult task while debugging a "normal" application).

However, once I finished reading everything, I realized this wasn't going to be too difficult because there were
only 3 instructions (`acc`, `nop`, `jmp`) and you just run through the instructions linearly (except for `jmp`).

### Part 1
> _Immediately before any instruction is executed a second time, what value is in the accumulator?_

Really all that was needed was an instruction pointer (e.g. the line number) and a holder for the value in the
accumulator field. Given the types of instructions, it was clear that if you ever run a line's instructions
a second time, you'll be in an infinite loop. So after writing a simple `while` loop running through the instructions
and incrementing the pointer appropriately, I just checked if that pointer is already in a set of run instructions
and if so, then we're done...just return the value in the accumulator.

### Part 2
> _What is the value of the accumulator after the program terminates?_

So for this part, I just figured I'd create a copy of the input, swap the instruction at the first line as mentioned,
and run the same code I had to get the accumulator value. There were 2 things that I needed to update, though,
in order to account for the question:
1. I needed to change my loop to stop if my instruction pointer is higher than the size of the input and return
	in that case as well
2. I needed to identify which scenario caused my program to quit (infinite loop detected, or end of program reached)

This is where I love the multiple return values in Python. I simply returned both the accumulator value and a boolean
to indicate if it was the end of file or not.

Now when I copy the data and swap out each instruction one at a time, I can just run my program and check my
multi-returned value to determine if it was the end of the file, and if so, I already have the accumulator value.

Nice!

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 1262  | 1  | 0  | 00:07:19  | 1227  |
| **Part Two**  | 1643  | 1  | 26  | 00:13:45  | 1643  |
