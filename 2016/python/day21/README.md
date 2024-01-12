# Approach
### Data format

Read each line of input as a string that I will parse later. Store it in a map along with the two passwords I will be
working with.

### Part 1
> _Given the list of scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?_

I really just did exactly the steps for each of the commands. I made each string an array of characters which allowed
me to manipulate them a lot easier. But that's really it.

### Part 2
> _What is the un-scrambled version of the scrambled password fbgdceah?_

90% of this one was just as easy as before. Most of the commands didn't change (swapping b and d is the same as swapping
d and b, etc). The only commands that needed to change to work backwards were:
* `move` -- if the command is move 5 to 2, going backwards you need to move 2 to 5 instead
* `rotate` -- rotating right originally means rotating left. Now the `rotate x steps` command was very straightforward, but the hardest part of this puzzle was the `rotate based on` command...

Alright, so I'm not proud of it, because it doesn't work for any sized password, but I took the length of my password (8) and
just wrote out all of the possibilities of where a specific character could end up based on this rotation. Luckily, every outcome
had a single specific origin. So, I just created a mapping of how far to move back based on where it currently is.

Like I said, it's hacky, but the concept works and it gives the right answer...so YAY!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
