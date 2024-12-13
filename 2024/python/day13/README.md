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

TODO -- write up mathematical reasoning...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
