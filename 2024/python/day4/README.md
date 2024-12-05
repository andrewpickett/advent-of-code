# Approach
### Data format

I first saw a grid and saw that I'd have to do things with "neighbors", so my first thought was to use my `Grid` class
since I wrote it for that sort of thing! Awesome.

So I had a 2d grid and was away parsing within 10 seconds! Awesome!

Well, long story short, I ended up just reading the input in as an array of strings...I found it was just going to be
easier to implement.

### Part 1
> _How many times does XMAS appear?_

So, as I mentioned above, I was trying to use my `Grid` class to do this, but after about 5-10 minutes of fumbling
around with getting neighbors in all directions and still needing to check boundaries, my code wasn't looking as
neat as I wanted. So I wasted about 10 minutes with this approach before abandoning it.

Now that I'm just dealing with a list of strings, I started trying to think of a clever way to get the slices/substrings
in a way that wasn't super ugly code...But as I kept implementing, it was just getting ugly again...so I wasted another 5 minutes
on this before I just decided to hack it together.

So, in the end, I just find every `X` and from there create an array of all 8 4-letter "words" that can be created from
that `X`. Now, I have to check all the boundaries, so sometimes it was less than 8 of them, but once I had all of the
4-letter words coming off of that `X`, just count the number that say `XMAS`. Sum them up, and we're done.

I should have just finished this in about 5 minutes, if I had just hacked it together to begin with...oh well.

### Part 2
> _How many times does an X-MAS appear?_

This one went quite a bit quicker. The first step was find all of the `A` characters (instead of `X` as above). This is
because all of the `X-MAS` instances will HAVE to have an `A` in the center:

```
.....
.?.?.
..A..
.?.?.
```
Now from that, my first approach was to check all of the cases for the diagonal neighbors of that `A` that would make a
valid `X-MAS` (basically as long as the diagonals weren't both an `M` or an `S`). I apparently missed a use case the first
go around because I had the wrong answer once. Instead of figuring out which case (because it was late, and I was sleepy),
I decided to just do the same approach as I did with part 1: create a list of all 4 of the 3-letter words that are created.
Then it's only a valid `X-MAS` if `MAS` is present exactly twice (because then the other 2 words would be `SAM`).

So that's pretty much it -- just count the number where that's true.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              27 |
| **Part Two** |              11 |
