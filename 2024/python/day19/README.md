# Approach
### Data format

Read the first row as a list of available patterns and then each subsequent row into a list as possible designs.

### Part 1
> _How many designs are possible?_

So I immediately thought of doing a recursive solution, because that just made sense. I implemented a quick solution that was basically:
```
if design is blank return true
otherwise
	iterate over every availble pattern and see if using that pattern the remaining portion of the design can be done with the available.
if we make it to the end and it's possible, just return true, otherwise return false.
```

So I did that, ran it on the sample, and it worked great. So I tried it on the input and...oh no...there are so many combinations
to try it just slowed to a crawl.

So I had to figure something out and that's when I remembered memoization and how much that can help with recursive solutions.
I decided to just pass in a dictionary to my function that held any previously run values and the output they gave (effectively
a function call cache). Ran it again, and it finished in 200ms. WOW!

Alright, on to the next part...

### Part 2
> _What do you get if you add up the number of different ways you could make each design?_

Isn't this the exact same question, just instead of returning a `True`\`False` value, I return a count?

I literally copy and pasted my code from part 1 and changed my return value from a `boolean` to an `int` and kept a sum
of the matches and sure enough, that worked. I then just went back and combined the two functions into one by passing
in a flag to determine if I'm adding or just tracking...

Super fast answer for part 2!

NOTE: I did later remember that python has a nifty `@functools.lru_cache` which I should probably have used on my method
instead of creating my own cache...but oh well, mine works just as well...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             250 |
| **Part Two** |             423 |
