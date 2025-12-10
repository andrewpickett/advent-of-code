# Approach
### Data format

My goal was just to divide the input into the individual parts for each machine (line). The only difference I decided to make
was to represent the machine configuration a little differently. Instead of a list of "on/off" characters, I stored it as
a `set` with which indices are "on". So something like `[.##.]` would just be `{1, 2}`. I did this because the buttons
are in this format, and I figured it would be easier to manipulate this way. So I wanted it to look like this:

```json
{
	"m": {1, 2},
	"b": [{3}, {0, 1}, {2, 3}, {0, 2, 3}],
	"j": [3, 5, 7, 9]
}
```

### Part 1
> _What is the fewest button presses required to correctly configure the indicator lights on all of the machines?_

I went with a pretty straightforward BFS for this part.

The first thing that I thought when I read this was: "why would you ever hit the same button more than once? It can't actually
do anything to help you get to the end...". Unlike the "lights-out" type puzzles, where when you click a button it alters neighboring
lights as well as the button's corresponding light, this puzzle's buttons ONLY impact the listed buttons. This means any time
you hit the same button twice, you are literally just undoing what you did the first time. This can be seen in the example that he gave:

```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
...
You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
```

Pressing `(0,1)` twice, does nothing and gives the exact same result as just pressing `(1,3)` once and `(2,3)` once. It doesn't
matter where you put those two `(0,1)` presses, they just cancel each other out...

I also noticed they weren't asking for the full path, so that meant I just had to keep track of the number of steps, not necessarily
the full path (I figured the `joltage` and possibly the resulting path would be included in part 2...but for this part I just omitted it).

So to me that meant this was much more straightforward of a puzzle, and so I decided to just do a BFS on all paths from an empty
set to the resulting set (as represented by a set of integers of the lights that are on).

None of the machine configurations were more than 10 lights, so doing a BFS wouldn't be too difficult. Since it's a BFS, we exhaust
every possibility for a given number of steps before moving to the next level. This means that the moment we get to a state that
is our target, we can just quit and return the number of steps. This wasn't really too difficult, but I was scared of the next part...

### Part 2
> _What is the fewest button presses required to correctly configure the joltage level counters on all of the machines?_

Not at all where I thought this was going. I expected the `joltage` numbers to mean the weighting or something between the
individual lights, and that I would need to do a Dijkstra or A* like path traversal to find the optimal configuration...

That wasn't it at all...

Instead, it was the one thing I really dislike in these puzzles: Linear Programming. The main reason I don't like LP is that
it is extremely difficult (for me, at least) to write solutions without using external libraries. I typically try to do
all of the AoC puzzles by only using the core SDK for whatever language I'm using. I think in all of the years, there's only been
**one** LP problem that I was able to do it in a decent amount of time.

I wasn't about to spend all night trying to figure this out, so I decided to pull in an old frenemy: Z3

I recognized it as this type of problem pretty quickly, as like I said, there's almost always at least one every year. I was just
really hoping this year he'd skip it :c)

Anyways, once I pulled in Z3, it wasn't too much work to actually get the answer, because I just let the library do all of the
heavy lifting.

# Results

|              |       Exec. Time (ms) - Python 3.13 |       Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------------:|----------------------------------:|
| **Get Data** |                               4.212 |                             8.877 |
| **Part One** |                             155.447 |                           127.649 |
| **Part Two** |                            1082.881 |                          1766.934 |
| **TOTAL**    |                           *1242.54* |                         *1903.46* |
