# Approach
### Part 1
>

First pass at this, I just literally stepped through it, highlighting the possible spots I was on at each step...exactly
like the examples showed. It ran fine on the sample and I got the correct answer, so I ran it on the main input.

It took about 20 seconds...but it gave me the correct answer, so I was at least then able to see the second part.

Now, after reading what the second part was going to be, I figured I should at least optimize part 1 a little bit...so
the first thing I did was don't re-visit any locations I already have. Just keep track of positions I've been to and
don't re-visit them. Pretty simple, but it didn't really help much on the time (down to 18 seconds).

I then realized was that any given point you CAN get to will just alternate "possible" and "not possible" every
2 steps. So instead of trying to keep track of them all, I just ran a flood-fill algorithm from the starting point and
at every step I set the value of the nodes to how many steps away from the start it was. Once I went the full distance (or the
board was full), I stopped. Now I can just iterate over every node on the board and say it's "possible" if its modulo 2 equals
the step count's modulo 2 (since it alternates every other on whether it was possible...even distances will be reachable if the
step count is even, and likewise with odd).

Now it ran in 10ms. Much better. But...it still doesn't completely solve my issue here...

### Part 2
>

Alright, I'm doing this write up a little bit differently. Because this one is definitely a head-scratcher, I'm going to
write things down here as I think of them. They may or may not lead me to a solution, but this should give a little
insight into what I'm thinking (I'll clean up the text afterwards so it reads better, but the general thought process should
remain the same):

### _Immediate thoughts_
The number of steps we need to take is in the tens of millions, so we're likely not going to actually run an algorithm that
many times. So I need to figure out how to break this down into predictable chunks and then there's probably a mathematical
formula to extrapolate out.

#### _10 minutes in_
Ok, so looking at the input, you can see there is a completely blank border around the grid (on the sample too), so that
MUST mean something. There are also no blockers in the starting row/column...so really the input is divided into 4 distinct
quadrants...again, this MUST be significant, but I'm not quite sure how yet.

#### _15 minutes in_
Interesting -- I ran my algorithm for 200+ steps in order to ensure the board was filled and when I printed the board, I
noticed that every edge square is reachable in the manhattan distance from the start. Meaning each corner can be reached
in 130 steps and it goes from 130 down to 65 and back up to 130 across each edge.

Of course this makes sense since there is a direct path from the start to the edges, and clear paths along the edges...
Ok, so given that, I know I can get to anywhere on the edge of the board in a known number of steps. Somehow I should be able to
project that out infinitely far until I've covered the number of steps the puzzle asks...but how?

#### _30 minutes in_
Ok, ok...so I can get to the edge of the first board in exactly `n//2` moves (with `n` being the size of a board).
The shortest distance to any of the new nodes on the new boards would be from the middle of the edge...and it would keep growing out
concentric diamond patterns from the start node.

I think I'm seeing it. I'm going to just run the my algorithm for `n=65`, `n=65+131`, `n=65+131+131`, etc and see what the
growth pattern is.

I also went ahead and checked the step count it is asking for -- conveniently, it is `26501365` -- which happens to be
`x*131+65` (and `x` happens to be `202300` -- which is quite fitting and clearly not a coincidence)!
So that really drives home that I'm on the right track...shouldn't be too hard now...

#### _40 minutes in_

Done. That was tricky. One thing I really didn't like about this one was that the sample input didn't follow the same
pattern completely...which makes me think there MAY be some other way that it was intended to be done.

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) |  Rank |
|--------------|---------:|----------------:|----------------------:|------:|
| **Part One** |        1 |              10 |              06:46:13 | 11493 |
| **Part Two** |          |                 |              07:26:17 |  3310 |


# Original puzzle
### --- Day 21: Step Counter ---
You manage to catch the airship right as it's dropping someone else off on their all-expenses-paid trip to Desert Island! It even helpfully drops you off near the gardener and his massive farm.

"You got the sand flowing again! Great work! Now we just need to wait until we have enough sand to filter the water for Snow Island and we'll have snow again in no time."

While you wait, one of the Elves that works with the gardener heard how good you are at solving problems and would like your help. He needs to get his steps in for the day, and so he'd like to know which garden plots he can reach with exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position (S), garden plots (.), and rocks (#). For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
The Elf starts at the starting position (S) which also counts as a garden plot. Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
Then, he takes a second step. Since at this point he could be at either tile marked O, his second step would allow him to reach any garden plot that is one step north, south, east, or west of any tile that he could have reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........
After two steps, he could be at any of the tiles marked O above, including the starting position (either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........
He will continue like this until his steps for the day have been exhausted. After a total of 6 steps, he could reach any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........
In this example, if the Elf's goal was to get exactly 6 more steps today, he could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's handed you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots could the Elf reach in exactly 64 steps?

Your puzzle answer was 3632.

--- Part Two ---
The Elf seems confused by your answer until he realizes his mistake: he was reading from a list of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.

The actual number of steps he needs to get today is exactly 26501365.

He also points out that the garden plots and rocks are set up so that the map repeats infinitely in every direction.

So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:

.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout; garden plots and rocks repeat as far as you can see. The Elf still starts on the one middle tile marked S, though - every other repeated S is replaced with a normal garden plot (.).

Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:

In exactly 6 steps, he can still reach 16 garden plots.
In exactly 10 steps, he can reach any of 50 garden plots.
In exactly 50 steps, he can reach 1594 garden plots.
In exactly 100 steps, he can reach 6536 garden plots.
In exactly 500 steps, he can reach 167004 garden plots.
In exactly 1000 steps, he can reach 668697 garden plots.
In exactly 5000 steps, he can reach 16733044 garden plots.
However, the step count the Elf needs is much larger! Starting from the garden plot marked S on your infinite map, how many garden plots could the Elf reach in exactly 26501365 steps?
