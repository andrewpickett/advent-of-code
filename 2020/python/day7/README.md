# Approach

This was really the first puzzle where the entire solution rested on how you structured your data. Pretty much
the entire challenge came from parsing the input into a format that you can easily use, instead of just a
basic array-type structure.

In reading the puzzle, the first thing that came to my mind was a tree-like structure...something like this:
```
                  BAG 1
                /       \
        3xBAG 2           5xBAG 3
       /       \                 \
   2xBAG 4  1xBAG 5           ___1xBAG 6____
               |             /      |       \
            4xBAG 7    1xBAG 8   2xBAG 9  7xBAG 10
```

Now that I had my idea of a structure, I looked at the input to decide how to parse it. At firs t it looked tricky,
but the pattern began to pop out pretty quickly and there were really only 2 different cases/formats:

1. {BAG NAME} bags contain no other bags.
2. {BAG NAME} bags contain {#} {BAG_NAME}, {#} {BAG_NAME}, ..., {#} {BAG_NAME}.

In both of those formats, the first bag name (aka, the node of a tree) is always everything up to "bags contain",
so that part's easy. Everything after "bags contain" are the children of that node; if it's "no other bags" then
there are no children...otherwise it's a comma-separated list of {#} {BAG_NAME}.

So now I had to decide how I wanted to represent it in the code. With Python,
I typically try using a basic `dict()` for most structures at first because it's so easy to work with,
so that's where I started. My idea was something like this:
```
{
	BAG 1: {
		BAG 2: 3,
		BAG 3: 5
	},
	BAG 2: {
		BAG 4: 2,
		BAG 5: 1
	},
	BAG 3: {
		BAG 6: 1
	},
	BAG 4: {},
	BAG 5: {
		BAG 7: 4
	}
	...
}
```

This allows me to simply represent the tree as a 1-level map. So now that I had the data represented in the code, I
moved on to the first part of the puzzle.

### Part 1
> _How many bag colors can eventually contain at least one shiny gold bag?_

I could have approached this part one of two ways: top down or bottom up. I decided to go with the bottom up
approach: starting with 'shiny bag' find any bags that have it as a child. Then for each of those bags, find any
bags that have them as children. Keep doing this until no new bags are identified. Then count how many were found.

For this, I created a `set()` which contains all of the bag names I run into while traversing up the tree.
I start by adding 'shiny bag' and just keep adding parents. Once I go through an entire iteration with no new
bags added to the set, I know I have all of them.

The last part would be to remove 'shiny bag' from the set, as we don't actually want to count it, since it can't
contain itself.

### Part 2
> _How many individual bags are required inside your single shiny gold bag?_

This part of the problem lent itself to the top down approach. Because of the data structure I used, it ended up
pretty easy: start with 'shiny bag' as a the "root node" of the tree and recursively traverse through the entire
tree, multiplying the number at each node by the number returned by the children (recursive call).

Then, once it's done, just add "1" to account for the node itself.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 185  | 1  | 2  | 00:20:13  | 1117  |
| **Part Two**  | 89084  | 1  | 2  | 00:31:37  | 1126  |

# Original puzzle

### --- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to
grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their
contents; bags must be color-coded and must contain specific quantities of other color-coded bags.
Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:
```
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
```
These rules specify the required contents for 9 bag types. In this example, every
`faded blue` bag is empty, every `vibrant plum` bag contains 11 bags (5 `faded blue` and 6 `dotted black`),
and so on.

You have a `shiny gold` bag. If you wanted to carry it in at least one other bag, how many different bag
colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at
least one `shiny gold` bag?)

In the above rules, the following options would be available to you:
* A `bright white` bag, which can hold your `shiny gold` bag directly.
* A `muted yellow` bag, which can hold your `shiny gold` bag directly, plus some other bags.
* A `dark orange` bag, which can hold `bright white` and `muted yellow` bags, either of which could then hold your `shiny gold` bag.
* A `light red` bag, which can hold `bright white` and `muted yellow` bags, either of which could then hold your `shiny gold` bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one `shiny gold` bag? (The list of rules is quite long;
make sure you get all of it.)

### --- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous
number of bags you need to buy!

Consider again your `shiny gold` bag and the rules from the above example:

* `faded blue` bags contain `0` other bags.
* `dotted black` bags contain `0` other bags.
* `vibrant plum` bags contain `11` other bags: 5 `faded blue` bags and 6 `dotted black` bags.
* `dark olive` bags contain `7` other bags: 3 `faded blue` bags and 4 `dotted black` bags.

So, a single `shiny gold` bag must contain `1` dark olive bag (and the `7` bags within it) plus `2` vibrant plum bags
(and the 11 bags within each of those): `1 + 1*7 + 2 + 2*11 = 32` bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to
count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:
```
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
```
In this example, a single shiny gold bag must contain `126` other bags.

How many individual bags are required inside your single `shiny gold` bag?
