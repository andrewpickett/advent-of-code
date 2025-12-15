# Approach
### Data format

Just read in each range by splitting the input on `,`.

#### Time Complexity

While the entire input is on only 1 line, we have to split it on `,` characters. Per the python's
built in `.split()` function, we know that the time for this would be $O(n)$ where $n$
is the number of elements divided by `,` in the file.

### Part 1
> _What do you get if you add up all of the invalid IDs?_

Ugh...I really need to sleep. My brain was completely unable to function during this. I think I started solving part 2
while I was reading the problem, so I was making it much harder than it needed to be and it took me WAY longer than it should have to complete.

In the end, my approach was something like this:
1. Get the true range of possible values to be checking.
   1. We know invalid numbers MUST be even length, since it's a number duplicated (for part 1)
   2. So for the lower bound, if it's not even, then simply round up to the nearest even power of 10.
   3. For the upper bound, if it's not even, then go to the number one less than the current power of 10.
2. Now that we have the true range of possible values, if the end is lower than the start, there's nothing to do...so we only care when it's a valid range of numbers.
3. At this point, we can make a new range of numbers by taking the first half of the start of our range and the first half of the end of our range.
4. Now, we iterate over this new range and just check if the given number doubled is in the "true" range we calculated.
5. If so, add that invalid number to a set

```
Example: If the original range is 998-1012, we can do the above steps to find:
  1. Find the "true" range: 1000-1012
  2. The start is less than the end, so we can continue
  3. New range: 10-10 (first half of 1000 + first half of 1012)
  4. Iterate over this new range of numbers and check if the doubled number is in our range. 1010 is in 1000-1012, so it's invalid!
  5. Add 1010 to our set of numbers
```

With this approach, instead of having to iterate over 15 values (998-1012), we only had to check 3.

A bigger example would be something like:
```
Example: If the original range is 8034-10235, we can do the above steps to find:
  1. Find the "true" range: 8034-9999
  2. The start is less than the end, so we can continue
  3. New range: 80-99 (first half of 8034 + first half of 9999)
  4. Iterate over this new range of numbers and check if the doubled number is in our range.
        8080, 8181, 8282, 8383, 8484, 8585, 8686, 8787, 8888, 8989, 9090, 9191, 9292, 9393, 9494, 9595, 9696, 9797, 9898, 9999
     Are all in our range, so they are all invalid.
  5. Add all of them to our set of numbers
```

Instead of iterating over 2201 values (8034-10235), we only had to check 20 of them (80-99).

The benefit of this, is that as you start breaking the number into smaller chunks, you have to check fewer values.
For part 1, this doesn't really matter, because we just run it with a value of `2` as our number of chunks to break each
number into...but for part 2 this will be extremely helpful.

At the end, we are left with a set of invalid numbers, so the answer is to just return the sum. WHEW!

#### Time Complexity

We have to iterate over every range we found, which is going to be $\Theta(n)$ where $n$
is the number of ranges defined in the file. Now, I then `split` and `copy` every element,
but they are only ever going to be length of 2, which is constant (so this portion would be
$O(1)$.

I then collapse the ranges down to their "true" range, which is again $O(1)$...but then comes
dividing the ranges into the number of valid parts and iterating over each of them to find
valid values. For this part, we are always dividing the range into ranges that have a length
half the size...which is effectively $n^\frac{1}{2}$.

This means that this whole part of the algorithm would be $O(n^\frac{1}{2})$ where $n$ is the length of the largest number in any range.

Since this is run for every line, our final time complexity would be $O(n\sqrt(n))$ or simply $O(n^\frac{3}{2})$ where $n$
is the length of the largest number in the file.

### Part 2
> _What do you get if you add up all of the invalid IDs using these new rules?_

Well, like I said, I was solving this part originally, so I knew what I needed to do. I pretty much do the exact same thing
as part one, but instead of doubling the value and dividing the ranges in half and everything being based on "2", I check every
amount of numbers that evenly divide the length of the values in my range! I was afraid this was going to run for a long time,
but I was pleasantly surprised to see it finish in ~1ms...so...I really didn't have to change much code to get this to work!

#### Time Complexity

Using the same analysis I did for part 1, we can say that the "worst" part of the performance is the case where we are only
dividing it into 2 partitions (so part 1). As we divide it into more smaller partitions, the performance only gets better...
evenaully approaching $O(n)$. So we'd really have $m$ iterations where $m$ is the number of pertitions that evenly divide
the longest number in the input. As such, we end up with $O(mn^\frac{3}{2})$ final complexity.

# Results

|              | Exec. Time (ms) - Python 3.13 | Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------:|----------------------------:|
| **Get Data** |                         0.131 |                       0.131 |
| **Part One** |                         0.717 |                       0.220 |
| **Part Two** |                         1.058 |                       0.276 |
| **TOTAL**    |                       *1.906* |                     *0.627* |

** *Ran each part 20000 times and averaged the run times to get final execution time*

#### Time Complexity

If we add these three parts together, we would get something like $O(l + (m+1)n^\frac{3}{2})$. But really, that `+1` doesn't
really add anything of value, so it's essentially $O(mn^\frac{3}{2} + l)$ where $l$ is the number of ranges in the file, $m$ is the
number of partitions that evenly divide the largest number, and $n$ is the length of the largest number in the file.

#### Possible Improvements

Honestly, as of right now, I don't see any obvious major improvements that I could make. This already runs very quickly, and
is fairly efficient.
