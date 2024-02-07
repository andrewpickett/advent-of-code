# Approach
### Data format

Read the input as an `AssembunnyProgram`. These are fun!

### Part 1
> _What is the lowest positive integer that can be used to initialize register `a` and cause the code to output a clock signal of `0`, `1`, `0`, `1`... repeating forever?_

I added a new register to my Assembunny program called `out`. Whenever the `out` instruction runs, I just write the current
value to the array I store in that register. If at any point my `out` register breaks the pattern of `0`, `1`, `0`, `1`, etc,
I stop the program and exit. I then increment the initial value in register `a` and try again.

I had to set a limit of number of steps to run before stopping...so it's really an assumption that if I still have the
correct pattern after that many steps then it will just repeat forever. I did some trial and error and found `40000` steps
was a good number to use.

### Part 2
> __

Merry Christmas!!!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            7106 |
| **Part Two** |             N/A |
