# Approach
### Data format

For this one, I kn

### Part 1
> _after you swipe your card, if the screen did work, how many pixels should be lit?_

I kept changing my mind on this one. At first, I decided to just use a 2d array and put the string values in there...but
then I thought I would be clever and just represent each row as a binary number (`# = 1` and `. = 0`) and then use
bitwise operators to actually manipulate it.

It was going pretty well, but then I realized the actual puzzle was going to be 50 columns wide, so that would be a very large number,
and I also realized I'd have to do some matrix rotations and other things for the column shifting...so I decided to
just go back to my original plan.

Once I made that decision it was pretty quick and easy to implement and I just built the full array and counted the number
of `#` present.

### Part 2
> _After you swipe your card, what code is the screen trying to display?_

Well, considering I built the full array already, I just output the array and you could very clearly make out the letters
that it was trying to spell. I decided not to try to parse it to return the actual string and just type it manually from what I saw.

This part took all of 7 seconds to complete.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
