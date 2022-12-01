# Approach
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

|              |     Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-----------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |        119 |        1 |               0 |                   N/A |  N/A |
| **Part Two** | ZFHFSFOGPO |        1 |               0 |                   N/A |  N/A |


# Original puzzle
### --- Day 8: Two-Factor Authentication ---
You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is `50` pixels wide and `6` pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

* `rect AxB` turns on all of the pixels in a rectangle at the top-left of the screen which is `A` wide and `B` tall.
* `rotate row y=A by B` shifts all of the pixels in row `A` (0 is the top row) right by `B` pixels. Pixels that would fall off the right end appear at the left end of the row.
* `rotate column x=A by B` shifts all of the pixels in column `A` (0 is the left column) down by `B` pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

* `rect 3x2` creates a small rectangle in the top-left corner:
```
###....
###....
.......
```
* `rotate column x=1 by 1` rotates the second column down by one pixel:
```
#.#....
###....
.#.....
```
* `rotate row y=0 by 4` rotates the top row right by four pixels:
```
....#.#
###....
.#.....
```
* `rotate column x=1 by 1` again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:
```
.#..#.#
#.#....
.#.....
```

As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

### --- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.
