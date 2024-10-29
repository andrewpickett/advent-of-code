# Approach
### Data format

Read the input into a 2-d array. Then go through and find every cart in the array (`>`, `^`, `<`, `v`) and replace the
value in the array with the actual track value "under" that cart. Each of the "carts" is represented by
```
(y-coord, x-coord, direction, intersection_counter)
```

Because it's a tuple ordered like this, I can just run a `.sort()` on the list of them and it will order them by row and
then column so I can process them in the correct way.

I then also store an array for tracking any collisions.

### Part 1
> _To help prevent crashes, you'd like to know the location of the first crash._

In concept, this is pretty simple: for each "cart" in my list, just increment them in the direction they're going.
We then just need to check if any two carts are on the same point. So really, just implement the following:
1) movement logic
   1) intersection logic
   2) turning logic
2) collision detection logic

Then just run through "move, detect" cycles until there has been a collision detected.

It worked great at first, but I realized pretty quickly that I was only doing the collision detection at the END
of the entire turn. Instead I needed to check after every single movement. I then ended up going back and forth
multiple times trying to write it in a way that made the most sense and wasn't overly ugly.

It took a lot longer than I wanted, but in the end it's pretty good.

### Part 2
> _What is the location of the last cart at the end of the first tick where it is the only cart left?_

Run through the same code, but this time only stop when the number of carts left in the list is 0 or 1.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               7 |
| **Part Two** |             207 |
