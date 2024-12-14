# Approach
### Data format

First, read in each line as a robot into this format:
```
{
	"pos": (x, y),
	"vel": (x, y)
}
```
Now, store all of those objects in a list mapped to a `robots` key. Then we also need to store the range/size of the
grid -- to allow for easier unit testing.

### Part 1
> _What will the safety factor be after exactly 100 seconds have elapsed?_

The hardest part of this part of the puzzle was just getting the grid into quadrants! I kept having typos and somehow
dropping rows/columns...it was a mess. In the end, though, I just have the grid contain integers for the count
of robots on each square, so once I did successfully divide the grid into quadrants, it was easy enough to just sum
up the total in the quadrant and then return the product.

I was originally going to step through all 100 steps, moving each robot each time...but thought, "there's no way
I'm going to do that...especially when part 2 will obviously scale to some crazy amount. So I'm just going to do them
all at once with maths!"

It worked great.

### Part 2
> _What is the fewest number of seconds that must elapse for the robots to display the Easter egg?_

Seriously?? You WANT us to step through them all one at a time?

Alright, well, I re-implemented my step function and then just ran it hoping to see a Christmas tree...but it was flying
by so fast, I didn't (or I didn't wait long enough, not sure)...

So I started thinking about how I could identify it...and I realized there is a very slim chance of a bunch of robots
all being on the same line by coincidence. I also figured if the final image was a Christmas tree of sorts, then the
base of the tree would probalby have quite a few robots in a row...right? So in my head I was thinking they'd create
something like this:
```
    #
   ###
  #####
 #######
#########
   ###
   ###
```

So I decided to just check after every move if there were a bunch of robots in the same row. I tried something like 15 in a row first
and it gave me the correct answer! I then refined it a little bit and it turns out "8" was the minimum to find the picture in my
case...it surprises me that 7 show up in a row by chance!

In the end, it may not be the fastest, but it works.

For the record, the resulting picture ended up much cooler than my above...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               1 |
| **Part Two** |            5795 |
