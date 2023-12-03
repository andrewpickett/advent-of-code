# Approach
### Part 1
>

Ok, so I'm really ticked at myself for this one. I created a Grid class a few years ago, that really comes in handy with
any puzzles that require knowing about neighbors for points in a grid. I decided to start using that and it worked
perfectly. I had the data parsed and all of the points mapped with their neighbors within 1 minute of the puzzle starting.

I wrote some quick code, got an answer and it was wrong. I looked through everything and found a defect, which I fixed and
was SURE my new answer would be correct -- nope...wrong again.

I spent the next 40 minutes trying to figure out what my problem was, and just could not figure it out...

...yeah...so...it turns out I just can't read and I was adding all the numbers that WEREN'T valid/connected to a special
symbol. Instead of using the numbers that were invalid..

So I just changed which numbers I used and I got the right number immediately.

I should have had this one solved in 5 minutes, but I just didn't read carefully. So ticked at myself.

Long story short, I iterate over every point. If it's a number, I start building the current number as I read through them.
While I'm reading each digit, I check if any neighbors are special characters. If so, I know the whole number will be valid.
Once I get to the end of a row or any non-digit, I know I'm done with building the current number and I can check if it was valid
at any point.

At the end, I have a list of all numbers that were valid, and I can just sum them up.

### Part 2
>

This one wasn't really any harder than the first, since I already had the framework and everything. I just changed what
it meant to be "adjacent" to something valid and instead of a simple boolean tracker, I kept track of all of the numbers
adjacent to the gears. At the end, just sum up which ones had exactly 2 numbers attached to it. Pretty much the same
logic as part 1, so I could probably extract things out a bit more, but I don't want to right now...

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        3 |              46 |              00:48:04 | 5524 |
| **Part Two** |        1 |              36 |              00:58:55 | 4245 |


# Original puzzle
###
