# Approach
### Data format

I read each machine into an object containing the `a` and `b` movements for both `x` and `y` as well as the `target`
values for `x` and `y`. So my machine objects look like this:

```
{
	"a": [12, 34],
	"b": [56, 78],
	"target": [875, 123]
}
```


### Part 1
> _What is the fewest tokens you would have to spend to win all possible prizes?_

I first wrote it with the good old brute force approach: I nested 2 loops (`a` and `b`) from 0 to 100 and just did a check
for if my `a` value multiplied by the values stored in my `a` key of the machine added to the `b` value multiplied by the values
stored in the `b` key of the machine gave me my `target` values. It worked just fine...ran in under 5ms. I was completely
shocked to find I was in te top 1000 with that solution, because I felt I was really slow in writing it up.

But obviously I knew something big was coming in part 2, so I was trying to think about what was actually happening here
while I was writing it...

### Part 2
> _What is the fewest tokens you would have to spend to win all possible prizes?_

Yep, obviously brute force isn't going to work...and with how this puzzle was written, it was clear there was just going
to have to be some purely mathematical way to optimize and solve this.

As I said, I was trying to think about the maths behind what was going on in part 1 while I was writing it...and so
I took a shot at writing up a quick and dirty solution based on what I was seeing, and sure enough it ended up being
correct. So after submitting, I went back and REALLY cleaned up the code to what it is now.

It turned out this was just solving a system of linear equations with 2-variables. You could get all fancy with linear algebra
or just write the system and simply/solve as you need. The two equations you're solving for are:

```
ax*a + bx*b = tx
ay*a + by*b = ty
```

Where `a` and `b` are the actual number of those button presses needed, and all the other variables are the known values
from the input for a given machine (e.g. `ax` is the `x` increase after pressing button `a`).
So that means that you can solve these by solving for one variable (let's say `a`) from the first equation to get:

```
a = (tx - bx*b) / ax
```

So now plug that back into the other equation to solve for `b`:
```
(ay * (tx-bx*b)/ax) + by*b = ty
(ay*tx - ay*bx*b) + ax*by*b = ax*ty
ax*by*b - ay*bx*b = ax*ty-ay*tx
b(ax*by - ay*bx) = ax*ty-ay*tx

b = (ax*ty - ay*tx) / (ax*by - ay*bx)
```

And doing the exact same thing for the other variable, you get your two equations:
```
a = (by*tx - bx*ty) / (ax*by - ay*bx)
b = (ax*ty - ay*tx) / (ax*by - ay*bx)
```

Now that you have those two equations, you know there is only a solution when both of those values for `a` and `b`
are whole numbers. So I just check if `a == int(a)` and `b == int(b)`. If so, then I have a valid solution. Otherwise, I don't.
Then just add up the tokens needed for all valid solutions.

YAY MATHS!!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
