# Approach

So, I fell asleep on the couch and woke up at about 12:15am...so I literally rolled over and opened the puzzle.
The instructions were extremely confusing to me in my sleep-fogged brain. I read them twice and it still meant
nothing to me, but after taking a few minutes to wake up, I realized they weren't difficult at all.

### Part 1
> _What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?_

My first observation with this puzzle was that "if you have multiple options, always choose the one with a less
difference". So basically, you just want to iterate from 0 to the maximum number of your input by ones and if
you have the adapter, add it. If you don't, just move to the next number.

That will give you an ordered list of all your adapters from your lowest to highest joltage...so...really all you
need is an ordered list of your input!

Then just add your built in joltage adapter (3 more than the last element) and add in the 0 from the initial input

```python
data.sort()
data.insert(0, 0)
data.append(data[-1] + 3)
```

That should give you your full chain from input source to your device using all of your adapters.

Now, we need to look at the differences between the adapters to determine how many 1-jolt and 3-jolt differences we have

So, because I assumed we'd need SOMETHING like this in the next part, I decided to create a list of all of the differences
between each adapter. Just subtract each element from it's next element and you get an array with all of the
differences:

```python
diff_list = [adapters[i+1] - adapters[i] for i in range(len(adapters) - 1)]
```

Now just count how many times `3` appears in that list and multiply it by the number of times `1` appears and there's your
first answer!

### Part 2
> _What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?_

Ok...so...at this point, it was about 1:00am. So let's keep that in mind here.

The part of the puzzle where they mention there will be more than a trillion possibilities immediately made me
realize brute force was out of the question. So I started looking at the data I had. In looking at the examples
given, I noticed that the only parts of the chain that could be done multiple ways were where we had more than
one hop of 1 joltage in a row. So anywhere we had a difference of 1 followed by 1 could be improved by removing
one of them.

Awesome! Ok, let's start replacing values in our difference array!

* `[...3, 1, 1, 3...]` could become `[...3, 2, 3...]`...so anywhere I have `1, 1` means I have 2 possibilities! NICE!
* `[...3, 1, 1, 1, 3...]` could become `[...3, 1, 2, 3...]` or`[...3, 2, 1, 3...]` or `[...3, 3, 3...]`. So
	`1, 1, 1` gives me 4 possibilities.

Right here I knew I was on to a solution...but holy cow did it go downhill from here. Due to my not thinking straight,
I started writing up recursive solutions to find all occurrences of each of those in the difference array. Why
recursion? I don't know. It SEEMED to make sense at the time. I was breaking up the array into prefixes, total counts,
using `sets`, and I don't even know what else.

I would get my solution to work for the first example, but not the second...then the second and not the first. I kept
changing my base cases in my recursive method to get the results I wanted. Finally I got both examples working, ran it
on my input, and it just hung. I realized I had essentially written a recursive brute force method. Not going to work.

I stopped and went to bed.

Ok, so this morning with a much clearer head, I re-visited what I had and started over.

Back to the pattern I was on to up top:
* Two 1s in a row gives 2 possibilities
* Three 1s in a row gives 4 possiblities
* Four 1s in a row gives 7 possibilities -- I wrote them out by hand to verify
* Five 1s in a row gives 13 possibilities

...So what's the pattern here? What would six 1s in a row give? I pretty quickly noticed that it was a "tribonacci"
sequence:

```trib(n) = trib(n-1) + trib(n-1) + trib(n-3)```

So six 1s would give 24, seven 1s would give 44...etc.

Alright, so I should just be able to count the number of times each of those lengths happen in my difference
array and multiply them all together to get the total! If I have a difference array with 3 1s in a row two distinct times
(e.g. `[3, 1, 1, 3, 1, 1, 3]`), it would be 2*2=4 total possibilities.

I tried some harder examples that I could validate via brute force listing (e.g.
`[3, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 3, 1, 1, 3, 3]` which would give `4*7*2=56`) and it seemed to be working

I plugged in my input got a huge number in under 1 ms entered it...and it was wrong.

I spent the next hour debugging looking over my maths, and could not figure it out. Finally I realized I was
forgetting to add the `0` input at the beginning of my input for part 2...which means I was missing one sequence since
my input's diff sequence starts with a `1` instead of `3` like all of my examples.

Adding the `0` in and running my code gave me the correct answer! Whew!

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 1625  | 1  | 0  | 00:19:44  | 7781  |
| **Part Two**  | 3100448333024  | 2  | 0  | ~02:00:00  | 18158  |

# Original puzzle

### --- Day 10: Adapter Array ---
Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you
can figure out whether it will impact your vacation plans, however, your device suddenly turns off!

Its battery is dead.

You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong
number of jolts. Always prepared, you make a list of all of the joltage adapters in your bag.

Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter
can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.

In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter
in your bag. (If your adapter list were `3`, `9`, and `6`, your device's built-in adapter would be rated for `12` jolts.)

Treat the charging outlet near your seat as having an effective joltage rating of `0`.

Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your
resort and realize you can't even charge your device!

If you use every adapter in your bag at once, what is the distribution of joltage differences between the
charging outlet, the adapters, and your device?

For example, suppose that in your bag, you have adapters with the following joltage ratings:
```
16
10
15
5
1
11
7
19
6
12
4
```
With these adapters, your device's built-in joltage adapter would be rated for `19 + 3 = 22` jolts,
3 higher than the highest-rated adapter.

Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter,
you'd need to choose them like this:

* The charging outlet has an effective rating of `0` jolts, so the only adapters that could connect to it
  directly would need to have a joltage rating of `1`, `2`, or `3` jolts. Of these, only one you have is an
  adapter rated `1` jolt (difference of `1`).
* From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of `3`).
* From the 4-jolt rated adapter, the adapters rated `5`, `6`, or `7` are valid choices.
  However, in order to not skip any adapters, you have to pick the adapter rated `5` jolts (difference of `1`).
* Similarly, the next choices would need to be the adapter rated `6` and then the adapter rated `7`
  (with difference of `1` and `1`).
* The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of `3`).
* From `10`, the choices are `11` or `12`; choose `11` (difference of `1`) and then `12` (difference of `1`).
* After `12`, only valid adapter has a rating of `15` (difference of `3`), then `16` (difference of `1`),
  then `19` (difference of `3`).
* Finally, your device's built-in adapter is always `3` higher than the highest adapter, so its rating is `22`
  jolts (always a difference of `3`).

In this example, when using every adapter, there are `7` differences of 1 jolt and `5` differences of 3 jolts.

Here is a larger example:
```
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
```
In this larger example, in a chain that uses all of the adapters, there are `22` differences of 1 jolt and `10`
differences of 3 jolts.

Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and
count the joltage differences between the charging outlet, the adapters, and your device. What is the number of
1-jolt differences multiplied by the number of 3-jolt differences?

### --- Part Two ---
To completely determine whether you have enough adapters, you'll need to figure out how many different ways
they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous
rules about when adapters can successfully connect still apply.

The first example above (the one that starts with `16, 10, 15`) supports the following arrangements:
```
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
```
(The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the
first example, the total number of arrangements that connect the charging outlet to your device is `8`.

The second example above (the one that starts with `28, 33, 18`) has many arrangements. Here are a few:
```
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, (52)
```
In total, this set of adapters can connect the charging outlet to your device in `19208` distinct arrangements.

You glance back down at your bag and try to remember why you brought so many adapters; there must be more than
a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your
device?
