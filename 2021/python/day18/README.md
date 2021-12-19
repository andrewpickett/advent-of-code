# Approach
### Part 1
> _Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?_

This. Sucked.

I spent about 20 minutes just reading the problem to try to actually understand what it was saying, what the rules were, etc.
After that, I realized it was not going to be at all easy, so I decided to go to bed and just worry about it in the morning.

So, the first hurdle -- and in some ways the most important -- was to just figure out how to model the snailfish. How
to parse the string from the input into some logical data model that could then be manipulated in the ways it describes.

I created a Node class (originally just called it "Pair") to try to just keep track of a left and right value...and I started
to try putting them into a stack of some sort (similar to a call stack), but I just couldn't get it to work right.

Finally it dawned on me to build the input into a binary tree. Every time we encounter a `[` in the input, that means it's a new
Node...every time we encounter a `]`, it's the end of a node and we can assign it to its parent, and then if we get a number
we're on a "leaf". I ignored commas, and assumed all numbers were a single digit (which was true for our input).

SIDE NOTE: this did actually cause me some headaches when trying to run through some samples and my own testing -- but
I wasn't willing to add the extra effort to just accommodate double digit numbers when the input didn't have them.

Ok, So, I built this tree so each node has exactly a left and right child and a single parent. The children could be other
nodes or just integers. Once I had the tree structure build, I read in the lines and output them immediately and sure enough
they matched exactly! So I knew I had the right data structure.

Now, I then started trying to add all of the methods (add, split, explode, etc) to the Node class itself...and while I was
able to get some of them, I found just adding them as utility methods outside of the class was faster and took less thought.
So, now that I had the data structure, I started working out the different methods.

* **Add** - Just take the two nodes, set them as left and right of a new parent node and set their parents to that node. Now
I did also have to increment the "depth" of every node, which required traversing the entire tree...So I implemented a simple
depth-first search approach to travel to all nodes from left to right, and used the same pattern for all of the below methods.
* **Split** - Not too bad: just take nodes that are int values over 9 and create two new nodes with the new values and set them
to the parent.
* **Explode** - Ok, this one was hard...I'm sure there's a better way than what I did, but basically you have to find the
closest left and right neighbors to a given node. Basically to find the left neighbor, you have to traverse up the tree
as far as you can until you can travel further left in the tree. Once you go left once, you go right as far as you can back
down the tree. Hard to explain, but that's the best way I could visualize it. Do the reverse for the right neighbor.

Alright, now that all of the methods are in place, it was a matter of just running through every line of the input and
performing the steps ONE AT A TIME. This caused some major slip-ups for me as I was working through it, but you can
only do one step at a time and then restart your process. Between that and the fact that explode always takes precedence over
splits were the key to getting this part working.

### Part 2
> _What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?_

This part wasn't really that hard once the first part was done and working. The biggest things to realize/figure out
are that you need to run through every combination of 2 and check them both directions. You also need to make sure you're
getting a fresh copy of the data every time you run a comparison, since the entire data structure/tree are manipulated
in place, and so the nodes will be completely different after you run one comparison. So just re-parsing the input
was the easiest way I could do it.

It's so extremely not efficient, and there are a number of places I could improve, but at this point, it's working and
I don't care. I just want done with this...so I am.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) |  Rank |
|--------------|-------:|---------:|----------------:|----------------------:|------:|
| **Part One** |   3734 |        1 |             162 |             ~02:30:00 | 10685 |
| **Part Two** |   4837 |        5 |           15149 |             ~00:20:00 | 10731 |

# Original puzzle

### --- Day 18: Snailfish ---
You descend into the ocean trench and encounter some snailfish. They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his math homework.

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as `[x,y]`, where `x` and `y` are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:
```
[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
```
This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, `[1,2] + [[3,4],5]` becomes `[[1,2],[[3,4],5]]`.

There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

* If any pair is nested inside four pairs, the leftmost such pair explodes.
* If any regular number is 10 or greater, the leftmost such regular number splits.

Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

Here are some examples of a single explode action:

* `[[[[[9,8],1],2],3],4]` becomes `[[[[0,9],2],3],4]` (the `9` has no regular number to its left, so it is not added to any regular number).
* `[7,[6,[5,[4,[3,2]]]]]` becomes `[7,[6,[5,[7,0]]]]` (the `2` has no regular number to its right, and so it is not added to any regular number).
* `[[6,[5,[4,[3,2]]]],1]` becomes `[[6,[5,[7,0]]],3]`.
* `[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]` becomes `[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]` (the pair `[3,2]` is unaffected because the pair `[7,3]` is further to the left; `[3,2]` would explode on the next action).
* `[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]` becomes `[[3,[2,[8,0]]],[9,[5,[7,0]]]]`.

To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, `10` becomes `[5,5]`, `11` becomes `[5,6]`, `12` becomes `[6,6]`, and so on.

Here is the process of finding the reduced result of `[[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]`:
```
after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
```
Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]`.

The homework assignment involves adding up a list of snailfish numbers (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is `[[[[1,1],[2,2]],[3,3]],[4,4]]`:
```
[1,1]
[2,2]
[3,3]
[4,4]
```
The final sum of this list is `[[[[3,0],[5,3]],[4,4]],[5,5]]`:
```
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
```
The final sum of this list is `[[[[5,0],[7,4]],[5,5]],[6,6]]`:
```
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
```
Here's a slightly larger example:
```
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
```
The final sum `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` is found after adding up the above snailfish numbers:
```
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
  = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
  = [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
  = [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
  = [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
  = [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
  = [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
  = [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
  = [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
  = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
```
To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of `[9,1]` is 3*9 + 2*1 = `29`; the magnitude of `[1,9]` is 3*1 + 2*9 = `21`. Magnitude calculations are recursive: the magnitude of `[[9,1],[1,9]]` is 3*29 + 2*21 = `129`.

Here are a few more magnitude examples:

* `[[1,2],[[3,4],5]]` becomes `143`.
* `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]` becomes `1384`.
* `[[[[1,1],[2,2]],[3,3]],[4,4]]` becomes `445`.
* `[[[[3,0],[5,3]],[4,4]],[5,5]]` becomes `791`.
* `[[[[5,0],[7,4]],[5,5]],[6,6]]` becomes `1137`.
* `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` becomes `3488`.

So, given this example homework assignment:
```
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
```
The final sum is:
```
[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
```
The magnitude of this final sum is `4140`.

Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?

### --- Part Two ---
You notice a second question on the back of the homework assignment:

What is the largest magnitude you can get from adding only two of the snailfish numbers?

Note that snailfish addition is not commutative - that is, `x + y` and `y + x` can produce different results.

Again considering the last example homework assignment above:
```
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
```
The largest magnitude of the sum of any two snailfish numbers in this list is `3993`. This is the magnitude of `[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]] + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]`, which reduces to `[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]`.

What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?
