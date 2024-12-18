# Approach
### Data format

Store the coordinates in reversed order so I can use my `Grid` class to run BFS. I also store the size of the array
and the size of the first block of corruptions so that I can make unit testing easier.

### Part 1
> _what is the minimum number of steps needed to reach the exit?_

...Just initiate the grid with the first 1024 values in the input and run a BFS...

It can't be that easy, can it??

Yes. Yes it can...and it is...weird.


### Part 2
> _What are the coordinates of the first byte that will prevent the exit from being reachable from your starting position?_

...Alright, so just continue to add individual coordinates from the input and re-run the BFS, once it doesn't give
a valid answer, that last point is the answer...right?

It can't be that easy is it??

Yes. Yes it can...and it was...really weird.

I did mess up quite a few submissions on this part, because I didn't read the instructions and tried submitting the coordinate
NUMBER (index in the file)...and then I flipped the `x` and `y` on the next submission...but after I actually paid attention
it really was as simple as above.

Now, it's fairly slow (13 seconds), and there are definitely improvements I could make (e.g. don't increment by 1, maybe increment by
half until it fails and then decrement by half and keep going by halves until we find the final one...but I'm lazy right now).

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              41 |
| **Part Two** |           13741 |
