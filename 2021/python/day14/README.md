# Approach
### Part 1
> _Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?_

I approached this part of the puzzle the "obvious" way at first. It took me about 20 minutes to write up because I kept having some stupid typos,
but I literally just followed the rules, building a new string after every step. I did this by just a simple for-loop
looking at each pair of letters, looking in my input map to see if that pair exists. If it doesn't, then leave them alone,
but if they do, build the resulting 3-letter chain and increment the counter by one (to move past the inserted character).

This approach ran nice and fast for part one, but I had a feeling there was no way it was going to work in part 2...

### Part 2
> _Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?_

Yep...no way. I kicked my solution to part 1 off just for fun to see if it would finish, and it DEFINITELY wasn't going to
any time soon. So I knew I needed another approach. The idea came to me pretty quickly: I don't need to build the string
in order to keep count of letters. I just need to keep track of the letters being used, and I can determine how many
of them are in each step by just knowing how many pairs of letters are in the previous step. In other words, I know
if I had 1 `NN` combination in the last step, I will now have 0 `NN`, 1 `NC`, and 1 `CN`. So then given that, on the next step
I would have 0 `NN`, 1 `NC`, 1 `NB`, 1 `BN`, 1 `CC`. I had it visualized something like this:
```
Step 0:                NN
                    /      \
Step 1:           NC        CN
                /    \    /    \
Step 2:        NB    BC  CC    NC
```
So now I have a count of all of the letter PAIRS in the final string. I don't know what the final string actually is, but
I don't need to. I then take my counts and for each individual letter, count the total number of times it appears in my
count map. So for the above, my resulting count map looked like this:
```
{"NC":1, "NB":1, "CC":1, "NC":1}
```
N appears 3 times, C appears 4 times, B appears 1 time. Now, the key here is knowing that the pairs overlap, so every letter
is getting double counted **except for the first and last in the final string!** So, we take our number for each letter
and divide it by 2...and if it's an odd number (of which there should be exactly 2), just round up.

With this method, we never build exponentially long strings, don't have to keep track of much except for pairs of letters
and it runs REALLY fast.

The only reason I had a failed attempt was because I ran my code on the sample input instead of my own input and entered
that number as my answer...oops.

Really fun puzzle, I'm glad I got myself back out of bed to work on it at night. I definitely slept better afterwards!

# Results

|              |        Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|--------------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |          2975 |        1 |               1 |              00:20:21 | 3376 |
| **Part Two** | 3015383850689 |        2 |               3 |             ~00:20:00 | 5084 |

# Original puzzle

### --- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:
```
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
```
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like `AB -> C` means that when elements `A` and `B` are immediately adjacent, element `C` should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template `NNCB`, the first step simultaneously considers all three pairs:

* The first pair (`NN`) matches the rule `NN -> C`, so element `C` is inserted between the first `N` and the second `N`.
* The second pair (`NC`) matches the rule `NC -> B`, so element `B` is inserted between the `N` and the `C`.
* The third pair (`CB`) matches the rule `CB -> H`, so element `H` is inserted between the `C` and the `B`.

Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes `NCNBCHB`.

Here are the results of a few steps using the above rules:
```
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
```
This polymer grows quickly. After step 5, it has length `97`; After step 10, it has length `3073`. After step 10, `B` occurs `1749` times, `C` occurs `298` times, `H` occurs `161` times, and `N` occurs `865` times; taking the quantity of the most common element (`B`, `1749`) and subtracting the quantity of the least common element (`H`, `161`) produces `1749 - 161 = 1588`.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

### --- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring `2192039569602` times) and the least common element is H (occurring `3849876073` times); subtracting these produces `2188189693529`.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
