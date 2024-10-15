# Approach
### Data format

For this, I just want to read each line into an object of tuples. One tuple for position, one for velocity, one for
acceleration. In the end, I have a list of these objects:
```
{'p': (0, 0, 0), 'v': (0, 0, 0), 'a': (0, 0, 0)}
```

### Part 1
> _Which particle will stay closest to position <0,0,0> in the long term?_

I first started trying to think about how to step through each point and figure out the ending trajectory away from
the origin. I was going through figuring out the slopes after each step and only when it started going away from the
origin would I then calculate which was going slowest, etc...

And then I realized this was EXTREMELY easy because it's not asking about any specific point in time. Instead it's just
asking "in the long term"...meaning as it goes on towards infinity. For that, all points will eventually be moving
away from the origin, the question is "which is moving slowest". It doesn't matter how far away they started, it doesn't
matter their current velocity...it only matters how fast they are accelerating, as eventually they will all be
accelerating away from the origin.

This means, we just need to take the "manhattan distance" of the acceleration vector, and the one that has the smallest,
is the winner. Because eventually, all others will be flying away from the origin faster than it. REALLY simple, actually.

### Part 2
> _How many particles are left after all collisions are resolved?_

Alright, now we have specific times involved. So we need to get a bit more creative. First thoughts with this:
```
p = 0.5at^2 + vt + s

p == position
a == acceleration
v == velocity
s == start position
t == time
```
We SHOULD be able to get the position of any point at a given time with the above formula...so if we take 2 points and
make them equal to each other:
```
0.5a[1]t^2 + v[1]t + s[1] == 0.5a[2]t^2 + v[2]t + s[2]

[1] == first point
[2] == second point
```
It will leave us with a quadratic equation, which we can solve to find what TIME `t` the 2 points intersect each other...
If the quadratic equation has no real roots, or no roots at all, then they never meet. Since we are dealing with discrete
time blocks, we also know if the solution to the quadratic isn't an integer they won't collide.

...Ok...so that sounded awesome, and seemed to work in practice. However, again, since we're dealing with discrete time blocks,
the above won't ACTUALLY work. The above works for continuous movement/acceleration. Bummer...

Instead, it seems the next position depends WHOLLY on the previous position:
```
v[t] = v[t-1] + a
p[t] = p[t-1] + v[t] + a
```

So instead, we'll just start iterating over each point, calculate the above and check to see if any other points are
at that position. If there are, we remove it from our list of valid points (and just don't add the new one). This will
start whittling down the list of points. Eventually there will be no change. I was originally going to try to figure out
how to determine when they are moving away from each other enough that there would be no more collisions, but after running
through it a couple thousand times, I saw that they stopped colliding after only 40 iterations. So I just capped
my loop at 40 and sure enough that was enough to get the right answer.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |              92 |
