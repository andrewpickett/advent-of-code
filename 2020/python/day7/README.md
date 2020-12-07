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
