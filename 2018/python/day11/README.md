# Approach
### Data format

For the data, I create the full power grid by taking the calculations described, simplifying them algebraically, and then
building the entire grid.

### Part 1
> _What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with the largest total power?_

Just run through the whole grid and add up the 3x3 squares everywhere. Return the highest value.

### Part 2
> _What is the X,Y,size identifier of the square with the largest total power?_

Alright, I still need to do some work here...because my algorithm would take forever to finish. I ran it until the size
was about 35x35, and paused it, saw that the largest up to that point was when it was an 11x11 grid and figured it
may be done with that being the largest. So I restarted my algorithm and limited it to only going to 12x12. When it finished,
I put the answer I got in the site and it was correct.

So, I got the right answer, it doesn't run TOO long, but I don't know how to better find the values so I can check
all 300x300...oh well for now, I guess.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             207 |
| **Part Two** |            4108 |
