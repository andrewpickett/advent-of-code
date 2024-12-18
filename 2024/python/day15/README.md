# Approach
### Data format

Divide the input into the list of directions and the grid. I then instantiate my `Grid` class with the points of the grid.
I also set the start point to be the `@` symbol and return all of that as an object. This allows for easier testing
later.

### Part 1
> _what is the sum of all boxes' GPS coordinates?_

This part is pretty straightforward. The different scenarios for each move are:
1. The next space is a `#` -- in which case, we just don't move.
2. The next space is a `.` -- in which case, we just move the `@` symbol to that position.
3. The next space is a `O` -- This is obviously the tricky part. In this case, we need to get the full line of points from the start to the next wall `#` or empty `.`
Once we have the full line, if it ends in a `.` we just loop through each item in the line and move the values over. If it
ends in a `#` we don't move, because the full stack is blocked.

That's really all there is to part 1. Running this was pretty quick and easy. Just do the calculation specified in the
puzzle to get the actual return value.

### Part 2
> _What is the sum of all boxes' final GPS coordinates?_

Ok, so at it's concept, this one wasn't really much harder...I just could NOT get all of the use cases working at the same time.

The first step is to do the grid doubling as mentioned in the puzzle. I wrote an overly-verbose method to do this, but it's very
simple and effective.

Next up, tackling the different use cases:

1. The next space is a `#` no matter the direction we're moving, we just don't move.
2. The next space is a `.` no matter the direction we're moving, we just move.
3. The next space is a `[` or `]` and we're moving left/right -- in this case, we just treat it effectively the same as we did
`O` above. Just get the full line and move as long as it's not blocked.
4. Now...getting a `[` or `]` while moving up/down is the hard part here. We have a few sub-cases:
   * All of the boxes are perfectly aligned up/down -- in this case, the full stack of two columns moves up/down together as long
   as neither are blocked
   * They are offset from each other -- and this can happen as many times as they want. In this case, we have to move any offset
   boxes along with the original in the stack, but then include any additional above/below them.

I knew exactly how to do that last bullet point, but for some reason I just kept getting use cases that would break it and my grid
would end up looking completely corrupted.

Either way, I worked for a while, and finally got it. The basic idea is just travel up/down the line like usual, but if I get a `[` or `]`,
I also add the matching point to my list of points that needs to move. I ended up processing them in a queue, and just keep popping
them off and adding them in the line until there are either none left, or I EVER hit a `#`. At which point, I just set the
value on each of the points in my list to the value of the point before it...the only exceptions are the initial point, if the
previous point was a wall, or if the previous point wasn't already in my list of points that need moved.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             180 |
| **Part Two** |             157 |
