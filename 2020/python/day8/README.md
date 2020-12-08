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

# Original puzzle

### --- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking
the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid
sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You
should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of
an operation (`acc`, `jmp`, or `nop`) and an argument (a signed number like +4 or -20).

* `acc` increases or decreases a single global value called the accumulator by the value given in the argument.
  For example, `acc +7` would increase the accumulator by 7. The accumulator starts at 0. After an `acc`
  instruction, the instruction immediately below it is executed next.
* `jmp` jumps to a new instruction relative to itself. The next instruction to execute is found using the
  argument as an offset from the `jmp` instruction; for example, `jmp +2` would skip the next instruction,
  `jmp +1` would continue to the instruction immediately below it, and `jmp -20` would cause the instruction
  20 lines above to be executed next.
* `nop` stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

For example, consider the following program:
```
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```
These instructions are visited in this order:
```
nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
```
First, the `nop +0` does nothing. Then, the accumulator is increased from `0` to `1` (`acc +1`) and `jmp +4`
sets the next instruction to the other `acc +1` near the bottom. After it increases the accumulator from
`1` to `2`, `jmp -4` executes, setting the next instruction to the only `acc +3`. It sets the accumulator
to `5`, and `jmp -3` causes the program to continue back at the first `acc +1`.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program
tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is `5`.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in
the accumulator?

### --- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a `jmp` is supposed to be a `nop`, or a `nop` is supposed to be a `jmp`. (No `acc`
instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last
instruction in the file. By changing exactly one `jmp` or `nop`, you can repair the boot code and make it terminate
correctly.

For example, consider the same program from above:
```
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```
If you change the first instruction from `nop +0` to `jmp +0`, it would create a single-instruction infinite
loop, never leaving that instruction. If you change almost any of the `jmp` instructions, the program will
still eventually find another `jmp` instruction and loop forever.

However, if you change the second-to-last instruction (from `jmp -4` to `nop -4`), the program terminates!
The instructions are visited in this order:
```
nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
```
After the last instruction (`acc +6`), the program terminates by attempting to run the instruction below the
last instruction in the file. With this change, after the program terminates, the accumulator contains the
value `8` (`acc +1`, `acc +1`, `acc +6`).

Fix the program so that it terminates normally by changing exactly one `jmp` (to `nop`) or `nop` (to `jmp`).
What is the value of the accumulator after the program terminates?
