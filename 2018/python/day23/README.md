# Approach
### Data format

Read the data as a list of tuples where the first element is the radius, and the next 3 are the coordinate.
This allows me to sort the list so that the highest radius is first.

### Part 1
> _How many nanobots are in range of its signals?_

Probably one of the simplest puzzles in a LONG time. I mean...this was really almost the same difficulty as a Day 1
puzzle...I'm guessing part 2 is going to be much harder?!

Just sort the input data. This makes the largest radius the first element. Now loop through all of the elements
and calculate the manhattan distance. If it's less than or equal to the radius, then include it. This can be done
with a simple list comprehension...

### Part 2
> _What is the shortest manhattan distance between any of those points and 0,0,0?_

...yep...yep it got harder...

Alright, well, obviously any sort of just brute force isn't going to work here. So after thinking through the problem
a little bit, I decided to do a binary-search type thing. Basically start by finding the largest possible square that
contains the bots and slowly reduce it in half until we find the most optimal.

This took a ton of debugging and walking through to get the edge cases and algorithm right (recursion...am I right??), and
it still takes quite a while to complete (30 seconds or so), but I'm pretty happy with it.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |           31041 |
