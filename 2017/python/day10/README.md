# Approach
### Data format

I read the input in a couple of different formats for the different parts of the puzzle and store them into a map
so I can use them in each part. I first store the range of data, so that I can adjust it for unit testing as needed.
I also store the original input as a list of integers. I finally store the list of integers as ascii values plus the
trailer defined in the puzzle. So in the end, my parsed input looks like this:

```
{
	"knot": [0, 1, 2, 3, 4, 5, 6, ...],
	"input": [3, 4, 1, 5, ...],
	"ascii": [49,44,50,44,51,17,31,73,47,23]
}
```

### Part 1
> _Once this process is complete, what is the result of multiplying the first two numbers in the list?_

This part was pretty simple. I initially built it with some complicated logic to do the reversal of the portion of the
string and it worked. I then was running into incorrect answers in the second part, so I decided to re-visit my solution
and came up with a little better of a process. Basically, the main portion of the knot hash is just taking a section
of a string and reversing it. The way I ended up doing that is to make a duplicate of the string and add it to the end
of the original. Then I can just reverse the section in the middle and re-build the original from that.

For example:

Given `1234567` as my string, let's say we want to reverse the portion starting at `5` and wrapping around to `2`.
* `12}34{567` shows the section we want to reverse between the `{}` brackets. So first duplicate the string
* `1234567|1234567` where I use `|` to denote the divider position of the concatenation.
* Now, block off the section to reverse and reverse it: `1234{567|12}34567` becomes `1234{217|65}34567`
* Now, we just take the first part of the string from the second half of the above and concatenate with the first portion of the first half: `65}34{217`

And that's it. Now we of course just have to increment our skip and position counters. Once it's done, going through all
of the input values, just return the product of the first two elements in the new list.

### Part 2
> _Treating your puzzle input as a string of ASCII characters, what is the Knot Hash of your puzzle input?_

I kept getting the same answer over and over and it was wrong. It turns out it was a problem with my original knot hash,
where it gave me the correct answer the first time, but subsequent calls were breaking. It took me rewriting it to
finally get the right answer. I also ran into the issue of having to left pad my hex values with `0`s if needed.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |              40 |
