# Approach
### Data format

I used my `Grid` class that I created for AOC to just read the input in as a Grid which allows me to use my methods likes
`BFS` and everything during this puzzle.

### Part 1
> _What is the outcome of the combat described in your puzzle input?_

WTF?! Ok, so this started off pretty fun. I enjoy solving these types of puzzles. So I wrote my solution, following all
of the directions (which, by the way, are WAAAAYYYY too verbose...). I ran it against ALL of the samples, and I got the
correct answer. So I ran it on my input, surely it'll work, since it worked on all 6 of the sample inputs...

Incorrect.

I kept re-reading, finding potential edge cases, fixing them, and trying again. Every time, it works on all sample inputs
but doesn't work on my input...and it keeps giving the SAME answer, no matter what things I fix/change. The fact that
my algorithm also is not very quick and takes over 2 minutes to run each time was just driving me nuts...

So, I reluctantly decided to look up some of the reddit posts about it, and they supplied more inputs to test and edge cases...so I would
try those, and it STILL works on all of them, but not my input. Finally, I resorted to looking up a solution and run it on my input just
to see how far off my answer was (which killed me!).

It seems like my solution is off by 1 round or something similar. I get `81 x 2627` whereas the correct answer APPEARS
to be `82 x 2624`. So it looks like I have ONE round of attacks that isn't getting registered or something in some random
use case...and again, I have no idea what it is. I have spent HOURS on this puzzle...I even output the final result of the correct solution
and the final result of my solution and they were identical...somewhere I'm just not counting correctly?!?!

### Part 2
> __


# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |                 |
| **Part Two** |                 |
