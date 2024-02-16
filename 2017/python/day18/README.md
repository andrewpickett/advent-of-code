# Approach
### Data format

Just read each line as a string and store in an array. I have a `DuetProgram` object that I created that will take the
list of strings and convert them to `DuetInstructions` that the `DuetProgram` will execute.

### Part 1
> _What is the value of the recovered frequency (the value of the most recently played sound) the first time a rcv instruction is executed with a non-zero value?_

Alright, I basically took the `AssembunnyProgram` I wrote in 2016 and modified it to meet the needs of this puzzle. It
didn't take long...the main part I had to do was keep track of any time a record was written to the `snd` register and so
when I run into a `rcv` command, I can just check that `snd` for any present and return the last one.

### Part 2
> _Once both of your programs have terminated (regardless of what caused them to do so), how many times did program 1 send a value?_

So, this one wouldn't have been too bad if I didn't take it upon myself to keep my code working for both parts of the
puzzle. I just had to modify the `DuetProgram` to handle the correct behavior of `snd` and `rcv`, but the issue was modifying
it in a way that didn't break part 1. It basically just meant I had to carry a flag throughout the program to determine
how to handle `rcv` commands.

Once I had that, I just run through one program until it gets to a `rcv` command. At which point, it checks if it has any
signals to process and if so, it just keeps going. If not, it goes into a "waiting" state and returns back to the caller.
It's at this point, the next program runs to the same point -- but before running, I take all the send signals from the first
program and add them to the `rcv` register. This then continues until both programs have nothing in `rcv`. All the while,
I just save all of the sends from the second program and return the total.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |             200 |
