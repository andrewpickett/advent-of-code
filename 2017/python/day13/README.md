# Approach
### Data format


### Part 1
> _Given the details of the firewall you've recorded, if you leave immediately, what is the severity of your whole trip?_

Maths FTW. Basically, being "caught" means that the layer number you're on modulo a specific amount based on the depth == 0.
Specifically, the formula is `2*(depth-1)`, because for a given depth, it takes `2*(depth-1)` picoseconds for the seeker
to come back to the top position. So you're only caught if the layer number you are on modulo that amount == 0.

You can ignore cases where the layer number is LESS than the depth because there's no way for the seeker to make it back
before you get there in those cases.

So just do that calculation for each element in the input and return the sum of the products. Done.

### Part 2
> _What is the fewest number of picoseconds that you need to delay the packet to pass through the firewall without being caught?_

My initial thought/approach is not fast, but it works -- I just start calculating the severity for each run of the
program with an increasing delay. Once I get a severity that is 0, it means I made it through.

Well, except for when the only time you're caught is at the 0th index -- so I first check if I get caught at that position,
because if I do, I don't need to do any more severity check, I can just skip that delay and move on.

I'm SURE there's a much better way to do this with LCMs or something, but I'm too lazy right now to figure it out. I'll
maybe come back to it sometime.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |           31700 |
