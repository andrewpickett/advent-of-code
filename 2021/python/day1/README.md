# Approach
### Part 1
> _How many measurements are larger than the previous measurement?_

Well, I ended up falling asleep on the couch and waking up at 11:59 (somehow)...so I was able to work on this right away,
but I was definitely still a little groggy. Not a great start to the event, but oh well, I got it done.

As usual, this first day is really quite straightforward. Since we just need to count the number of times an element is
larger than the previous element, we can just do that with one simple list comprehension: start at the first element
and go through to the last, check the element with the one prior and adding up the number of times it's larger.

Done.

### Part 2
> _Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?_

Really nothing different here than the first part...just instead of comparing element `i` with `i-1` just compare
the sum of `i`, `i-1`, `i-2` with the sum of `i-1`, `i-2`, `i-3` and add them up. The only trick here is to start your
list iteration at the 4th element in order to be able to do all of the correct compares.

The biggest bummer here was that I got 504 server timeout errors when trying to submit this answer. Obviously there
was a pretty big load on the server at the time with people submitting. So after a few minutes, it finally went through.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |   1766 |        1 |               1 |              00:02:42 | 1173 |
| **Part Two** |   1797 |        1 |               2 |              00:03:21 |  968 |

# Optimizations

I originally wrote this using list comprehensions. While those are really good for creating new lists, they aren't the best
for performing calculations. So I tried just going with straight for-loops, which did improve performance a little bit, but
not drastically.

| Attempt | Part One Runtime (ms) | Part Two Runtime (ms) | Number Test Runs |
|--------:|----------------------:|----------------------:|-----------------:|
|       1 |                 0.661 |                 2.004 |             5000 |
|       2 |                 0.717 |                 1.742 |             5000 |

TOTAL RUNTIME: 1.378 ms

# Original puzzle
### --- Day 1: Sonar Sweep ---

You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:
```
199
200
208
210
200
207
240
269
260
263
```
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of `199`, `200`, `208`, `210`, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:
```
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```
In this example, there are `7` measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

### --- Part Two ---
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:
```
199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H
```
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked `A (199, 200, 208)`; their sum is `199 + 200 + 208 = 607`. The second window is marked `B (200, 208, 210)`; its sum is `618`. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare `A` with `B`, then compare `B` with `C`, then `C` with `D`, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:
```
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
```
In this example, there are `5` sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
