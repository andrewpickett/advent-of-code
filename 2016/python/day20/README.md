# Approach
### Data format

Read the lines as a `range` so that they can be easily referenced. I then sort that list of ranges by the start value
of each range. I then add it into a map along with the maximum value for easier testing.

### Part 1
> _Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?_

Went down the obvious rabbit hole of just trying to create a set or array of all the valid values and use set operations
to create a full list of blocked ips...

Clearly wasn't going to work with over 4 trillion values.

So, I did a little thinking and realized since I'm just trying to find the lowest allowed, I just need to find the end of the
FIRST combined range of values. The easiest way to do this is to sort the input list of ranges by their start value, then
start evaluating from the beginning each next one and combining them until it runs into a situation where there is no overlap
(and an "overlap" is simply that the start value of the next range is AFTER the end of the current range).

Once I encounter that scenario, just return the end value of the first range and that's the answer. Super simple.

### Part 2
> __

Alright, so now we just need to do that same behavior over and over through the WHOLE list of ranges to end up with
a much shorter list of combined, non overlapping ranges. At that point just count the numbers between the ranges.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
