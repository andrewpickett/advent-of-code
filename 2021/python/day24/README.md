# Approach
### Part 1
> _What is the largest model number accepted by MONAD?_

Ok...so...after reading this problem, and seeing the ALU that was involved, I immediately sat down and wrote the ALU implementation.
Easy. Took 5 minutes max.

Great...alright, super easy. Looking at the examples given, I started getting confused on what the input was supposed to
be to my ALU. I re-read the problem and realized the examples they showed had no actual relevance to the actual puzzle
and that they were just arbitrary examples of other codes.

The problem is asking for me to FIND the input value that leaves a "0" in the `z` register after all of the input instructions
completed.

Alright, so...brute force, maybe? I mean, just looping over 10^14 integers...yeah, nevermind. The instructions say the
MONAD puts constraints on what values can be in the input, so I needed to try to figure out what those constraints were.

I decided to just start running the code over all 14-digit inputs and outputting the `z` value to see if I could find any patterns.
I noticed that the outputs repeated quite often, and only when the last digits were `19` did the `z` value decrease at all.
So maybe there was something there?

I spent probably about 40 minutes just looking at the outputs, trying to find patterns, and trying to think of how to
programmatically determine the constraints. Finally, it dawned on me to actually try figuring out exactly what the code DOES
in order to determine what constraints leave me a 0.

Pretty quickly I noticed the input was divided into 14 repeating (...at least I thought so at first) sections. It reads in one
of the inputs, and then does stuff and then repeats 14 times. So the things I noticed immediately were:

* `w` always just contained the last read input number
* `x` was always reset to 0 in each section
* `y` was always reset to 0 in each section

...So that means the ONLY piece of information that carried across the sections to the end was the value of `z` itself.
I started tracking it and noticed it was getting populated with the input values +/- some other integers and then into the next
section with it...but it seemed like it just continued growing.

So I started at the end and worked my way backwards, and I very quickly realized there were actually 2 DIFFERENT sections that
were used, not just 1...and each one was used exactly 7 times.

After spending probably 30 minutes analyzing the code, I realized that the `z` variable actually behaved like a stack, not just
a single integer register. One of the sections basically just pushed a number onto the stack and the other one would pop
a value off of the stack and conditionally push another.

The only way `z` would be `0` at the end was if all of the values were successfully popped off of the stack!

So I literally went through each section and wrote the code just in terms of the stack manipulation (using #1 to represent the first number in the input string, etc):
```
z.push(#1 + 8)
z.push(#2 + 13)
z.push(#3 + 8)
z.push(#4 + 10)
if #5 != z.pop() - 11
	z.push(#5 + 12)
if #6 != z.pop() - 13
	z.push(#6 + 1)
z.push(#7 + 13)
z.push(#8 + 5)
if #9 != z.pop() - 2
	z.push(#9 + 10)
if #10 != z.pop() - 6
	z.push(#10 + 3)
z.push(#11 + 2)
if #12 != z.pop() - 0
	z.push(#12 + 2)
if #13 != z.pop() - 15
	z.push(#13 + 12)
if #14 != z.pop() - 4
	z.push(#14 + 7)
```

So now I can just logically think through the constraints that would lead me to be able to have nothing left on the stack at the end.
the first 4 sections add 4 numbers to the `z`-stack. In order to pop a value off, my 5th input digit needs to be 11 less than my 4th
input digit plus 10 (the previous instruction pushed input digit 4 + 10 to the stack).
This means my 5th digit must be 1 less than my 4th digit.
So that's my first constraint: digit 5 must be 1 less than my forth, so digit 4 can only be digits 2 through 9, and digit 5 must be 1 through 8.

I proceeded to manually go through the input and analysis like this to determine the possible values for each input location and I got the list
I put in the `constraints` variable. From there to find the largest number, I just took the largest possible value from each
position.

Entered the answer and it worked. I did decide to run it through the ALU first just to to verify `z` was `0` before submitting
and it was.

So long story short (too late): I manually deconstructed the code to determine the possible values for the input...I didn't
actually need to use the ALU at all, and I didn't write any code to do the determiniation...so I feel like I cheated in some way,
but I was done and it worked...on to part 2...

### Part 2
> _What is the smallest model number accepted by MONAD?_

Well hey! I already did all of the analysis, so I just took the minimum values from each constraint and guess what? It worked!
No additional work needed to figure it out.

# Results

|              |         Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------------:|---------:|----------------:|----------------------:|-----:|
| **Part One** | 59998426997979 |        1 |               0 |             ~01:30:00 | 3107 |
| **Part Two** | 13621111481315 |        1 |               0 |              00:00:10 | 2966 |

# Original puzzle

### --- Day 24: Arithmetic Logic Unit ---

Magic smoke starts leaking from the submarine's arithmetic logic unit (ALU). Without the ability to perform basic arithmetic and logic functions, the submarine can't produce cool patterns with its Christmas lights!

It also can't navigate. Or run the oxygen system.

Don't worry, though - you probably have enough oxygen left to give you enough time to build a new ALU.

The ALU is a four-dimensional processing unit: it has integer variables `w`, `x`, `y`, and `z`. These variables all start with the value `0`. The ALU also supports six instructions:

* `inp a` - Read an input value and write it to variable `a`.
* `add a b` - Add the value of `a` to the value of `b`, then store the result in variable `a`.
* `mul a b` - Multiply the value of `a` by the value of `b`, then store the result in variable `a`.
* `div a b` - Divide the value of `a` by the value of `b`, truncate the result to an integer, then store the result in variable `a`. (Here, "truncate" means to round the value toward zero.)
* `mod a b` - Divide the value of `a` by the value of `b`, then store the remainder in variable `a`. (This is also called the modulo operation.)
* `eql a b` - If the value of `a` and `b` are equal, then store the value `1` in variable `a`. Otherwise, store the value `0` in variable `a`.

In all of these instructions, `a` and `b` are placeholders; `a` will always be the variable where the result of the operation is stored (one of `w`, `x`, `y`, or `z`), while `b` can be either a variable or a number. Numbers can be positive or negative, but will always be integers.

The ALU has no jump instructions; in an ALU program, every instruction is run exactly once in order from top to bottom. The program halts after the last instruction has finished executing.

(Program authors should be especially cautious; attempting to execute div with b=0 or attempting to execute mod with a<0 or b<=0 will cause the program to crash and might even damage the ALU. These operations are never intended in any serious ALU program.)

For example, here is an ALU program which takes an input number, negates it, and stores it in x:
```
inp x
mul x -1
```
Here is an ALU program which takes two input numbers, then sets `z` to `1` if the second input number is three times larger than the first input number, or sets `z` to `0` otherwise:
```
inp z
inp x
mul z 3
eql z x
```
Here is an ALU program which takes a non-negative integer as input, converts it into binary, and stores the lowest (1's) bit in `z`, the second-lowest (2's) bit in `y`, the third-lowest (4's) bit in `x`, and the fourth-lowest (8's) bit in `w`:
```
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
```
Once you have built a replacement ALU, you can install it in the submarine, which will immediately resume what it was doing when the ALU failed: validating the submarine's model number. To do this, the ALU will run the MOdel Number Automatic Detector program (MONAD, your puzzle input).

Submarine model numbers are always fourteen-digit numbers consisting only of digits `1` through `9`. The digit `0` cannot appear in a model number.

When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen separate `inp` instructions, each expecting a single digit of the model number in order of most to least significant. (So, to check the model number `13579246899999`, you would give `1` to the first `inp` instruction, `3` to the second `inp` instruction, `5` to the third `inp` instruction, and so on.) This means that when operating MONAD, each input instruction should only ever be given an integer value of at least `1` and at most `9`.

Then, after MONAD has finished running all of its instructions, it will indicate that the model number was valid by leaving a `0` in variable `z`. However, if the model number was invalid, it will leave some other non-zero value in `z`.

MONAD imposes additional, mysterious restrictions on model numbers, and legend says the last copy of the MONAD documentation was eaten by a tanuki. You'll need to figure out what MONAD does some other way.

To enable as many submarine features as possible, find the largest valid fourteen-digit model number that contains no 0 digits. What is the largest model number accepted by MONAD?

### --- Part Two ---

As the submarine starts booting up things like the Retro Encabulator, you realize that maybe you don't need all these submarine features after all.

What is the smallest model number accepted by MONAD?
