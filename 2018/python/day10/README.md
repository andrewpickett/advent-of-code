# Approach
### Data format

I basically just need to get the two sets of coordinates from each line. There are a ton of ways to do that, but I decided
to just replace all `<`, `>` and `,` characters with a different delimiter `_`. Then I split on my new delimiter
and was able to extract all the points and velocities into their own lists, which I stored in a map for later use.


### Part 1
> _What message will eventually appear in the sky?_

Alright, these are always "fun" puzzles, but a little frustrating because I can't just return the string as my answer.
I have to look at the graph output and interpret it myself. In some other years, I was able to write an interpreter,
but I didn't really want to do that this time.

Ok, so, really I just step through over and over moving the points by their velocity every time. The hardest part is
figuring out "When do I stop?! When is there a legible message available?" I decided there is a really good chance
that there are letters displayed once there is an entire column filled in from top to bottom. This _should_
happen for the letters `BDEFHIKLMNPRT'. So as long as the answer has at least ONE of those letters, this condition should be met. So the first thing is
to just get the range of values of all the points. Once we have that, it's just check that there is a full column of
points filled in SOMEWHERE in the graph. Once that condition is met, then just output the result and see if it is letters.
Fortuntely for me, that worked perfectly.

### Part 2
> _exactly how many seconds would they have needed to wait for that message to appear?_

Just run the exact same code as part 1 and return the number of steps. I originally stored the result from part 1
and just used it for part 2 (which means 0 ms execution time), but that made unit testing harder...so I just went back
to running it a second time.

I did have to laugh that it somehow knew my algorithm for part one would take ~3 seconds...ha!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            2163 |
| **Part Two** |            2150 |
