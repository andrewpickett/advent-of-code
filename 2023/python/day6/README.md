# Approach
### Part 1
> _What do you get if you multiply these numbers together?_

Well, I fell asleep at 11:30. BUT, I had an alarm set for 11:50 just in case that sort of thing happens to give me time
to wake up and get on the computer to start solving!!

...but...I slept through the alarm. I finally woke up around 12:20...so I finally got started shortly after that.

Either way, it was nice to have a "reasonable" day 6 puzzle! These are the kinds of puzzles I expected at this point, and
they're a lot of fun.

On first read, you start thinking of implementing the solution exactly how the story tells you -- with for loops and actually "running" the
races to figure out which ones are the winners...but this is Advent of Code. It's clear that that approach will likely not
work for part 2, so I reread the puzzle and immediately saw that there would have to be a purely mathematical solution to
solving it.

Looking at the examples (and just thinking through it logically) it at first looked like maybe a Pascal's Triangle (Binomial coefficients) type of thing
because for any given race, when increasing the time the button is held make the distances increase to a point mid-way and then decrease the same amount back to `0`.

Example for `t = 7`: `0, 6, 10, 12, 12, 10, 6, 0`

So I sat down and wrote out the math and pretty quickly it was clear the formula to calculate the
distance `d` for any given time total time `t` and speed `s`:

`d = s*(s-t)`

So, now the puzzle becomes "what values of `s` for a given `t` will give you a value greater than `d`?" Which makes the equation we need to solve:
```
d < s*(s-t)
0 < s^2 - st - d
```

There's a nice, simple quadratic equation we can solve to find values of s that satisfy that! So in the example given, it becomes `0 < s^2 - 7s - 9` which
when plugging into the quadratic formula gives values of `s` of `~5.4` and `~1.7`. In order to satisfy the equation with natural numbers (since we can't hold
the button for fractions of a millisecond), we just need to floor the upper bound and ceiling the lower bound giving us values of `5` and `2`.

And that's really it. The only "tricky" part is if the values of `s` are already whole numbers, you need to subtract one from the upperbound and add
one to the lowerbound, since equality isn't allowed.

Plug in the values from the input, do this calculation, multiply all the results together, and you're done!

### Part 2
> _How many ways can you beat the record in this one much longer race?_

Exact same calculation -- which is what I was hoping for and why I spent time figuring out the mathematical solution to part 1 to
begin with. Just concatenate the input values and run them through the same formula and you get the answer right away.

Time for sleep.

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) |  Rank |
|--------------|---------:|----------------:|----------------------:|------:|
| **Part One** |        1 |              <1 |              00:40:16 | 10608 |
| **Part Two** |        1 |              <1 |              00:44:00 |  9624 |


# Original puzzle
### --- Day 6: Wait For It ---
The ferry quickly brings you across Island Island. After asking around, you discover that there is indeed normally a large pile of sand somewhere near here, but you don't see anything besides lots of water and the small island where the ferry has docked.

As you try to figure out what to do next, you notice a poster on a wall near the ferry dock. "Boat races! Open to the public! Grand prize is an all-expenses-paid trip to **Desert Island**!" That must be where the sand comes from! Best of all, the boat races are starting in just a few minutes.

You manage to sign up as a competitor in the boat races just in time. The organizer explains that it's not really a traditional race - instead, you will get a fixed amount of time during which your boat has to travel as far as it can, and you win if your boat goes the farthest.

As part of signing up, you get a sheet of paper (your puzzle input) that lists the **time** allowed for each race and also the best **distance** ever recorded in that race. To guarantee you win the grand prize, you need to make sure you **go farther in each race** than the current record holder.

The organizer brings you over to the area where the boat races are held. The boats are much smaller than you expected - they're actually **toy boats**, each with a big button on top. Holding down the button **charges the boat**, and releasing the button **allows the boat to move**. Boats move faster if their button was held longer, but time spent holding the button counts against the total race time. You can only hold the button at the start of the race, and boats don't move until the button is released.

For example:
```
Time:      7  15   30
Distance:  9  40  200
```
This document describes three races:

* The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
* The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
* The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.

Your toy boat has a starting speed of zero **millimeters per millisecond**. For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by **one millimeter per millisecond**.

So, because the first race lasts 7 milliseconds, you only have a few options:

* Don't hold the button at all (that is, hold it for 0 milliseconds) at the start of the race. The boat won't move; it will have traveled **`0` millimeters** by the end of the race.
* Hold the button for **`1` millisecond** at the start of the race. Then, the boat will travel at a speed of `1` millimeter per millisecond for `6` milliseconds, reaching a total distance traveled of **`6` millimeters**.
* Hold the button for **`2` milliseconds**, giving the boat a speed of `2` millimeters per millisecond. It will then get `5` milliseconds to move, reaching a total distance of **`10` millimeters**.
* Hold the button for **`3` milliseconds**. After its remaining `4` milliseconds of travel time, the boat will have gone **`12` millimeters**.
* Hold the button for **`4` milliseconds**. After its remaining `3` milliseconds of travel time, the boat will have gone **`12` millimeters**.
* Hold the button for **`5` milliseconds**, causing the boat to travel a total of **`10` millimeters**.
* Hold the button for **`6` milliseconds**, causing the boat to travel a total of **`6` millimeters**.
* Hold the button for **`7` milliseconds**. That's the entire duration of the race. You never let go of the button. The boat can't move until you let go of the button. Please make sure you let go of the button so the boat gets to move. **`0` millimeters**.

Since the current record for this race is `9` millimeters, there are actually `4` different ways you could win: you could hold the button for `2`, `3`, `4`, or `5` milliseconds at the start of the race.

In the second race, you could hold the button for at least `4` milliseconds and at most `11` milliseconds and beat the record, a total of `8` different ways to win.

In the third race, you could hold the button for at least `11` milliseconds and no more than `19` milliseconds and still beat the record, a total of `9` ways you could win.

To see how much margin of error you have, determine the **number of ways you can beat the record** in each race; in this example, if you multiply these values together, you get `288` (`4` * `8` * `9`).

Determine the number of ways you could beat the record in each race. **What do you get if you multiply these numbers together?**

### --- Part Two ---
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really **only one race** - ignore the spaces between the numbers on each line.

So, the example from before:
```
Time:      7  15   30
Distance:  9  40  200
```
...now instead means this:
```
Time:      71530
Distance:  940200
```
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for `71530` milliseconds and the record distance you need to beat is `940200` millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of `71503` ways!

**How many ways can you beat the record in this one much longer race?**
