# Approach
### Part 1
> _How many steps are required to reach ZZZ?_

This part was pretty simple. Just create a map with the left/right paths for each node. Start traversing
by following the instructions on a loop, while keeping a counter and when you hit `ZZZ`, just return your counter.

Took 5ish minutes to implement

### Part 2
> _How many steps does it take before you're only on nodes that end with Z?_

Ok, so I first figured I'd TRY the brute force method by just getting all my start nodes (ones that
end with `A`) and then run through the same algorithm I had before, but do each step on each of the nodes
in the start group before moving on to the next. It ran for about 20 minutes before I decided to kill it
and figure out the ACTUAL way he wants us to solve this.

So I looked at my input and noticed there are ONLY 6 start elements and EXACTLY 6 end elements.

This lead me to try making an assumption about the network:
any given start element wouldn't ever get to multiple end elements.

With that assumption in mind, I figured I could just count how long it takes each start element
to get to their respective end element.

So I did that and had an array of 6 lengths...so then it's just run a Least Common Multiple
computation on those 6 numbers to get the time that all 6 would line up at the same time.

This number was MASSIVE, so it's no wonder my brute force wasn't going to finish any time soon...
if only I had just started with the LCM to begin with.

Pretty slick solution, if I say so myself.

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        1 |              19 |              00:07:24 | 1193 |
| **Part Two** |        3 |             109 |              00:34:17 | 2140 |


# Original puzzle
### --- Day 8: Haunted Wasteland ---
You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about **ghosts** a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of **network** of labeled nodes.

It seems like you're meant to use the **left/right** instructions to **navigate the network**. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: `AAA` and `ZZZ`. You feel like `AAA` is where you are now, and you have to follow the left/right instructions until you reach `ZZZ`.

This format defines each **node** of the network individually. For example:
```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
```
Starting with `AAA`, you need to **look up the next element** based on the next left/right instruction in your input. In this example, start with `AAA` and go **right** (`R`) by choosing the right element of `AAA`, **`CCC`**. Then, `L` means to choose the **left** element of `CCC`, **`ZZZ`**. By following the left/right instructions, you reach `ZZZ` in **`2`** steps.

Of course, you might not find `ZZZ` right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: `RL` really means `RLRLRLRLRLRLRLRL...` and so on. For example, here is a situation that takes **`6`** steps to reach `ZZZ`:
```
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
```
Starting at `AAA`, follow the left/right instructions. **How many steps are required to reach `ZZZ`**?

### --- Part Two ---
The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take **significantly more steps** to escape!

What if the map isn't for people - what if the map is for **ghosts**? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in `A` is equal to the number ending in `Z`! If you were a ghost, you'd probably just **start at every node that ends with `A`** and follow all of the paths at the same time until they all simultaneously end up at nodes that end with `Z`.

For example:
```
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
```
Here, there are two starting nodes, `11A` and `22A` (because they both end with A). As you follow each left/right instruction, use that instruction to **simultaneously** navigate away from both nodes you're currently on. Repeat this process until **all** of the nodes you're currently on end with `Z`. (If only some of the nodes you're on end with `Z`, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

* Step 0: You are at `11A` and `22A`.
* Step 1: You choose all of the **left** paths, leading you to `11B` and `22B`.
* Step 2: You choose all of the **right** paths, leading you to `11Z` and `22C`.
* Step 3: You choose all of the **left** paths, leading you to `11B` and `22Z`.
* Step 4: You choose all of the **right** paths, leading you to `11Z` and `22B`.
* Step 5: You choose all of the **left** paths, leading you to `11B` and `22C`.
* Step 6: You choose all of the **right** paths, leading you to `11Z` and `22Z`.

So, in this example, you end up entirely on nodes that end in `Z` after **`6`** steps.

Simultaneously start on every node that ends with `A`. **How many steps does it take before you're only on nodes that end with Z**?
