# Approach
### Data format

Well...it was the first night that I fell asleep beforehand and my alarm just did not wake me up. Luckily my wife woke up
at around 12:20 and poked me because she knew I wanted to work on this. So I got a 20 minute late start, which is a bummer
because this one ended up being pretty easy!

I get the first part of the input and convert them to `range` objects. Once I do that, I use a utility I wrote to
convert all of those ranges into a list of combined ranges -- basically get a collapsed list of ranges where any
overlap is accounted for.

I then get the second part of the input as just a list of IDs.

### Part 1
> _How many of the available ingredient IDs are fresh?_

I was able to do this part in 1 line, but I ended up expanding the list comprehension out into explicit for loops because
I was able to break the for-loop and save a decent amount of time in certain cases.

Basically just loop over each ID and check if it's in any of the combined ranges. If it's not in any range, add it to a
list of "fresh" fruit. At the end, just return the length of that list. Really very simple.

### Part 2
> _How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?_

Well this one was extremely simple since I already had the combined ranges! All I had to do was take the total size of the ranges
(which includes adding 1, since the end of the range is inclusive here) and add them together. Done.

# Results

|              | Exec. Time (ms) - Python 3.13 | Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------:|----------------------------:|
| **Get Data** |                         1.560 |                       0.918 |
| **Part One** |                        10.313 |                       0.482 |
| **Part Two** |                         0.033 |                       0.003 |
| **TOTAL**    |                      *11.906* |                     *1.403* |

** *Ran each part 1000 times and averaged the run times to get final execution time*
