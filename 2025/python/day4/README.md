# Approach
### Data format

Read the input as a `Grid`. Luckily my utility classes work perfectly for this kind of puzzle.

### Part 1
> _How many rolls of paper can be accessed by a forklift?_

Since my `Grid` utility class already has a bunch of helper functions for getting all of the points and setting all
of their neighbors and values and everything, I am able to just iterate over every point in the `Grid` that has a
value of `@` and then count how many neighbors it has with a value of `@`. Do that one time and return the total count.

It took me a couple of minutes to remember how to use my `Grid` completely, but I solved this part in about 4 minutes, so
I was pretty happy with that.

I decided to store all of the points that the forklift can reach in a `set` because it will make part 2 much easier.

### Part 2
> _How many rolls of paper in total can be removed by the Elves and their forklifts?_

...I read this and my brain started struggling to figure out how to determine which rolls are accessible by a forklift...

I read it over and over, and looked at the example and started thinking that I'd have to do some sort of flood fill to
determine which ones a forklift driving around the outside would be able to reach and remove...and just do that over and over...
I started playing with that for about 5-8 minutes until I realized what I did in part 1 is exactly the definition of
being accessible by a forklift.

...I'm a complete idiot...Just run a loop performing the part 1 code on the grid and for every point it finds that is
accessible, change the value to `.`. Once I run through the whole grid without changing any values to `.` in a given
iteration, I can quit the loop. Keep track over all iterations of how many I change, and voila. Simple answer.

I seriously could have finished this part in about 2 minutes...but alas...I once again was trying to over-complicate things.

# Results

|              |        Exec. Time (ms) - Python 3.13 |      Exec. Time (ms) - PyPy 3.11 |
|--------------|-------------------------------------:|---------------------------------:|
| **Get Data** |                              334.266 |                           36.319 |
| **Part One** |                               29.609 |                           11.622 |
| **Part Two** |                              852.251 |                          233.609 |
| **TOTAL**    |                           *1216.126* |                         *281.55* |

** *Ran each part 100 times and averaged the run times to get final execution time*
