# Approach
### Part 1
> _What is the lowest location number that corresponds to any of the initial seed numbers?_

This first part is pretty direct. Again, though, he's really making the inputs difficult to parse!

I basically separated out the list of seeds from the rest of the mappings. Then just iterate over every seed in the list
and run it through the mappings lists one at a time, mapping the result of the seed input to the next mapping and so on.
It's exactly how the puzzle describes it, and it was really quite simple.

I could have solved it MUCH faster if I hadn't spent so much time trying to figure out a good way to parse the input into
the format I needed. I went through 5 or 6 different iterations of the format of the input until I landed on the one
I finally used. I could have just hard coded it and probably solved it in 15 minutes or so...but oh well.

### Part 2
> _What is the lowest location number that corresponds to any of the initial seed numbers?_

Holy cow. Day 5. What is he thinking??

Ok, so the first thing was to change the format of the seeds to be a range instead of just individual values. Simple enough...
but...now we're talking literally billions of values to run through. Clearly that's not going to work, and there MUST be
some shortcut way to handle this.

I actually first did an approach where I worked BACKWORDS, starting from the locations and working my way UP the chain to
find if it mapped to a valid seed value. It was again pretty simple, but absolutely not optimized and I kicked it off and let it run.
It took about 20 minutes and returned an answer -- somehow, someway, it was actually correct. So at that point I just
submitted the answer and went to bed.

The next morning, with a clearer head I spent a little time trying to optimize it and come up with a better solution, which I finally
did:

Essentially, we only need to compare ranges, because any values within the same range from source to destination will have the same minimum
in the end.

It sounds simple enough, but seriously...manipulating rages of values and checking for where they overlap each other and
sorting them and making sure all the use cases are accounted for...it hurts my head! I spent a lot of time just writing examples
down in a notebook and seeing how they flow through. As I was doing that, I just started writing the code to match what I was doing
by hand on the example.

It basically involved recursively collapsing the intervals down to non-overlapping intervals and comparing the values that way.
Along the way, I had quite a few bugs and compiler errors, but after fixing them, I ran the code, and was absolutely stunned to find I got the right answer
with very little tweaking of my code -- and it ran in a matter of milliseconds.

I'm quite happy with that one.

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        1 |               0 |              00:56:23 | 7272 |
| **Part Two** |        6 |               2 |              01:32:02 | 3037 |


# Original puzzle
### --- Day 5: If You Give A Seed A Fertilizer ---
You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we **ran out of sand** to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our **food production problem**. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil `123` and fertilizer `123` aren't necessarily related to each other.

For example:
```
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
```
The almanac starts by listing which seeds need to be planted: seeds `79`, `14`, `55`, and `13`.

The rest of the almanac contains a list of **maps** which describe how to convert numbers from a **source category** into numbers in a **destination category**. That is, the section that starts with `seed-to-soil map:` describes how to convert a **seed number** (the source) to a **soil number** (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire **ranges** of numbers that can be converted. Each line within a map contains three numbers: the **destination range start**, the **source range start**, and the **range length**.

Consider again the example `seed-to-soil map`:
```
50 98 2
52 50 48
```
The first line has a **destination range start** of `50`, a **source range start** of `98`, and a **range length** of `2`. This line means that the source range starts at `98` and contains two values: `98` and `99`. The destination range is the same length, but it starts at `50`, so its two values are `50` and `51`. With this information, you know that seed number `98` corresponds to soil number `50` and that seed number `99` corresponds to soil number `51`.

The second line means that the source range starts at `50` and contains `48` values: `50`, `51`, ..., `96`, `97`. This corresponds to a destination range starting at `52` and also containing `48` values: `52`, `53`, ..., `98`, `99`. So, seed number `53` corresponds to soil number `55`.

Any source numbers that **aren't mapped** correspond to the **same** destination number. So, seed number `10` corresponds to soil number `10`.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:
```
seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
```
With this map, you can look up the soil number required for each initial seed number:

* Seed number `79` corresponds to soil number `81`.
* Seed number `14` corresponds to soil number `14`.
* Seed number `55` corresponds to soil number `57`.
* Seed number `13` corresponds to soil number `13`.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find **the lowest location number that corresponds to any of the initial seeds**. To do this, you'll need to convert each seed number through other categories until you can find its corresponding **location number**. In this example, the corresponding types are:

* Seed `79`, soil `81`, fertilizer `81`, water `81`, light `74`, temperature `78`, humidity `78`, **location `82`**.
* Seed `14`, soil `14`, fertilizer `53`, water `49`, light `42`, temperature `42`, humidity `43`, **location `43`**.
* Seed `55`, soil `57`, fertilizer `57`, water `53`, light `46`, temperature `82`, humidity `82`, **location `86`**.
* Seed `13`, soil `13`, fertilizer `52`, water `41`, light `34`, temperature `34`, humidity `35`, **location `35`**.

So, the lowest location number in this example is `35`.

**What is the lowest location number that corresponds to any of the initial seed numbers?**

### --- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the `seeds:` line actually describes **ranges of seed numbers**.

The values on the initial `seeds:` line come in pairs. Within each pair, the first value is the **start** of the range and the second value is the **length** of the range. So, in the first line of the example above:
```
seeds: 79 14 55 13
```
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number `79` and contains `14` values: `79`, `80`, ..., `91`, `92`. The second range starts with seed number `55` and contains `13` values: `55`, `56`, ..., `66`, `67`.

Now, rather than considering four seed numbers, you need to consider a total of **27** seed numbers.

In the above example, the lowest location number can be obtained from seed number `82`, which corresponds to soil `84`, fertilizer `84`, water `84`, light `77`, temperature `45`, humidity `46`, and **location `46`**. So, the lowest location number is **`46`**.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. **What is the lowest location number that corresponds to any of the initial seed numbers**?
