# Approach
### Data format

Read the input as an integer. That is all.

### Part 1
> _With the number of Elves given in your puzzle input, which Elf gets all the presents?_

This one's hilarious, because I used to do a code challenge with people to see how few lines they could solve essentially
this puzzle in. It's called the Josephus problem and can be done completely mathematically. The way I used to do it
for the challenge was something like this:
```
(2x - (highest power of 2 less than 2x)) OR 1
```

### Part 2
> _With the number of Elves given in your puzzle input, which Elf now gets all the presents?_

I assumed this one would have a similar pattern and way to mathematically derive a formula to solve this...but I didn't
know it off the top of my head. So the first thing I did was actually write up the code to build the table (as a list)
and actually run through the algorithm described, popping off elves one at a time until the array was a size of 1.

At that point, I just returned the value.

I ran this on the test input, plus a couple of my own, and found a pattern to the solutions. The outputs I had looked like
this:

```
1, 1, 3, 1, 2, 3, 1, 2, 3, 8, 10, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 25, 27, 29, 31, 33, 35, 37, 39...
```
Which very clearly showed a pattern:
```
1, 1, 3
1, 2, 3 -- 1, 2, 3 -- 8, 10, 12
1, 2, 3, 4, 5, 6, 7, 8, 9 -- 1, 2, 3, 4, 5, 6, 7, 8, 9 -- 23, 25, 27, 29, 31, 33, 35, 37, 39
```
So I spent a long time trying to come up with a mathematical way to represent that and
calculate it. Which I did! It was beautiful and concise. I ran it on tons of test inputs and they all yielded correct answers...
so I ran it on the actual puzzle and -- WRONG ANSWER!

I then spent the next long while rechecking my formula, finding sequences that match, finding other theorems that all matched
my math based on the outputs I was seeing from the brute force algorithm..

...

Yeah...I had an error in my algorithm to begin with. So for the code I wrote, I came up with a beautiful solution...but my
code was wrong.

So, once I fixed the code, I did all the work again. This time the output wasn't nearly as easy to determine, but it all
basically comes down to the same idea and I finally got a formulaic way to get the answer.

That was rough...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
