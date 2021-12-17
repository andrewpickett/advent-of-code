# Approach
### Part 1
> __

This did not feel like a day 17 puzzle. When I read it, I immediately started thinking it could be solved purely
mathematically. The first thought I had was that in order to get the highest y value, it would have to be entering
the square completely vertically (x velocity of 0). Since the velocity drops by 1 every step, that would mean
the total distance would be n*(n+1) / 2, where n is the initial velocity. Figure out which values of n will result
in a total distance within the given range, and I easily found the list of possible x values that would possibly enter
the square completely vertically.

Great, so now on to the y-value...

I could tell it was going to be a similar approach as I took with the x values, but I started fumbling over myself.

I started spiraling a little bit until I was getting confused at what I was looking at and what I was trying to actually
determine.

All the while, I was thinking in the back of my mind that part 2 was going to ask for a lot more -- probably something
involving "all possible" trajectories or something like that.

After about 15 minutes of confusing myself, I decided to just hack out the code to actually DO every combination
of initial x and y values in a given range (I took an arbitrary stab at a number) and get a list of all initial x/y
velocities that resulted in hitting the square. I then used that list to find the maximum y value.

Once I had the maximum y value, it was just plugging it into n * (n+1) / 2 to get the height it would reach...

I didn't like it, because I knew it could be done simpler, but I moved on.

### Part 2
> _How many distinct initial velocity values cause the probe to be within the target area after any step?_

Well look at that, it wanted all possible values. It's almost like I'm learning how these puzzles are set up or something.
Well, I had already written the code to find them all given a specific
range, so all I had to do was make sure my range was accurate and return the length of the resulting list.

So in trying to determine the most accurate range to search for, I realize how completely simple part 1 was...I'll come back
to that.

So let's start with the x value range. The MAXIMUM value for the initial x velocity would be the far end of the target
square. This is pretty obvious because if your initial x velocity is greater than the square, you're going to overshoot
it right away. The minimum would be the lowest value that allows you to enter the square vertically. So I did an estimate
of that value by taking the lowest x of the square, multiplying it by 2 and taking the square root...then flooring that value.
This works because we know that the total distance travelled is n*(n+1) / 2, so to make sure we have AT LEAST a specific x
value of that, we can do what I said (yes, I know I could use the quadratic equation to get the exact values, but I didn't care
to be that precise here...).

So now I have my range of x values that will POSSIBLY land me in the square.

For the y values, we know the minimum would be the lowest y value of the square, for the same reason as the x maximum:
if you have lower, your initial step would take you below the bottom of the square and that doesn't work. But now figuring
out the maximum. Well that would be easy, right? Because when the projectile goes up, it will come back down in the
reverse stepping as it went up (e.g. it goes up with velocity 5, 4, 3, 2, 1...it will come down with 1, 2, 3, 4, 5)...So
it will always end up back at the y=0 line, but with a different velocity depending on how high it initially went. That means
the highest velocity it could have when it hits the y=0 line would be the minimum y value of the square (since again, the next step
would then put it below the bounds of the square if it was any lower). Which means the maximum y trajectory would just be
1 less than (the absolute value of) that value...

...
...
...

Wait...isn't that EXACTLY what the part one asked??? "What's the HIGHEST value that it can reach?"...

Oh man...

So I could have just looked at the lowest y value, and taken 1 less than the absolute value of it to find the maximum
height. Plug that into the n*(n+1)/2 equation and gotten the answer to part 1. Awesome. So I made that change and it worked.

But since I had already written the code to find all of them, my part 2 was super simple now that I had my x and y value
ranges to check. I plugged them in, ran the code, and took the length of the results. Voila. No problems.

I really should have been able to solve part 1 in under a minute, because it was exactly what my brain was trying to
actually SAY when I read the problem...I just couldn't hold onto it long enough to write it down. Oh well.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |  12561 |        1 |               0 |              01:02:12 | 4110 |
| **Part Two** |   3785 |        1 |              90 |              00:06:08 | 3406 |

# Original puzzle

### --- Day 17: Trick Shot ---
You finally decode the Elves' message. HI, the message says. You continue searching for the sleigh keys.

Ahead of you is what appears to be a large ocean trench. Could the keys have fallen into it? You'd better send a probe to investigate.

The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y (upward, or downward if negative) directions. For example, an initial x,y velocity like `0,10` would fire the probe straight up, while an initial velocity like `10,-1` would fire the probe forward at a slight downward angle.

The probe's x,y position starts at `0,0`. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

* The probe's x position increases by its x velocity.
* The probe's y position increases by its y velocity.
* Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
* Due to gravity, the probe's y velocity decreases by 1.

For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be within a target area after any step. The submarine computer has already calculated this target area (your puzzle input). For example:
```
target area: x=20..30, y=-10..-5
```
This target area means that you need to find initial x,y velocity values such that after any step, the probe's x position is at least `20` and at most `30`, and the probe's y position is at least `-10` and at most `-5`.

Given this target area, one initial velocity that causes the probe to be within the target area after any step is `7,2`:
```
.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
...........................#...
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
```
In this diagram, `S` is the probe's initial position, `0,0`. The x coordinate increases to the right, and the y coordinate increases upward. In the bottom right, positions that are within the target area are shown as `T`. After each step (until the target area is reached), the position of the probe is marked with `#`. (The bottom-right `#` is both a position the probe reaches and a position in the target area.)

Another initial velocity that causes the probe to be within the target area after any step is `6,3`:
```
...............#..#............
...........#........#..........
...............................
......#..............#.........
...............................
...............................
S....................#.........
...............................
...............................
...............................
.....................#.........
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................T#TTTTTTTTT
....................TTTTTTTTTTT
```
Another one is `9,0`:
```
S........#.....................
.................#.............
...............................
........................#......
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTT#
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
```
One initial velocity that doesn't cause the probe to be within the target area after any step is `17,-4`:
```
S..............................................................
...............................................................
...............................................................
...............................................................
.................#.............................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT..#.............................
....................TTTTTTTTTTT................................
...............................................................
...............................................................
...............................................................
...............................................................
................................................#..............
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
..............................................................#
```
The probe appears to pass through the target area, but is never within it after any step. Instead, it continues down and to the right - only the first few steps are shown.

If you're going to fire a highly scientific probe out of a super cool probe launcher, you might as well do it with style. How high can you make the probe go while still reaching the target area?

In the above example, using an initial velocity of `6,9` is the best you can do, causing the probe to reach a maximum y position of `45`. (Any higher initial y velocity causes the probe to overshoot the target area entirely.)

Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory?

### --- Part Two ---

Maybe a fancy trick shot isn't the best idea; after all, you only have one probe, so you had better not miss.

To get the best idea of what your options are for launching the probe, you need to find every initial velocity that causes the probe to eventually be within the target area after any step.

In the above example, there are `112` different initial velocity values that meet these criteria:
```
23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7
```
How many distinct initial velocity values cause the probe to be within the target area after any step?
