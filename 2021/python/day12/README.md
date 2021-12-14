# Approach
### Part 1
> _How many paths through this cave system are there that visit small caves at most once?_

I approached this just like I do any "map traversal" problem: build a map linking the nodes. The map's keys are each
node, and the values are an array of nodes they can connect to. Now, since you can travel both directions between
the nodes, when you add one neighbor node to the map, you have add another for the opposite direction.

Ok, so once the map is built, it's a matter of recursively going through from the `start` node and just "traveling" to
each of the nodes in it's "neighbor" list. For this part of the puzzle, since we can only visit a lowercase letter
once, if we move to a lowercase cave, we then need to remove that cave from every other neighbor map, so we don't
go back there.

Now, as we're traversing through the map, we build our "map path", which is really just a string (instead of an array
because string comparisons are much easier than array comparisons) showing which nodes we have traversed.

If we ever get to the `end` node, or a node that has no "neighbors", we are done...but only return the successful map path
if we reach `end`.

Once it has gone through the entire map/tree along all possible routes, we just count the number of map paths.

I was actually quite amazed at how easily this one came together.

### Part 2
> _Given these new rules, how many paths through this cave system are there?_

This one was a little harder to wrap my head around, because I was struggling how to ever get past the FIRST lowercase
without counting it as a double hit. But as I wrote it out on physical paper, I realized that there wasn't much different
than the first part, except that we just need to keep track of all of the lower case caves we've visisted. Once we go into
any of them a second time, we then need to remove ALL of them from all of our "neighbor" lists and proceed exactly like
part 1.

I originally had it all broken into two different traversal methods, but was able to re-work it down to just one with a
simple boolean to determine which use case we're currently in.

Now, this approach worked, and solved the puzzle just fine...however it is definitely not fast. Taking more than 10 seconds
is not what I like to see, so I'm sure there's a faster/better approach to it...but I just don't think I care that much
right now.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) |  Rank |
|--------------|-------:|---------:|----------------:|----------------------:|------:|
| **Part One** |   5252 |        1 |             433 |              00:36:40 |  3337 |
| **Part Two** | 147784 |        1 |           12627 |             ~01:00:00 | 32485 |

# Original puzzle

### --- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:
```
start-A
start-b
A-c
A-b
b-d
A-end
b-end
```
This is a list of how all of the caves are connected. You start in the cave named `start`, and your destination is the cave named `end`. An entry like `b-d` means that cave `b` is connected to cave `d` - that is, you can move between them.

So, the above cave system looks roughly like this:
```
    start
    /   \
c--A-----b--d
\   /
end
```
Your goal is to find the number of distinct paths that start at `start`, end at `end`, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like `A`) and small caves (written in lowercase, like `b`). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

Given these rules, there are `10` paths through this example cave system:
```
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
```
(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

Note that in this cave system, cave `d` is never visited by any path: to do so, cave `b` would need to be visited twice (once on the way to cave `d` and a second time when returning from cave `d`), and since cave `b` is small, this is not allowed.

Here is a slightly larger example:
```
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
```
The `19` paths through it are as follows:
```
start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
```
Finally, this even larger example has `226` paths through it:
```
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
```
How many paths through this cave system are there that visit small caves at most once?

### --- Part Two ---
After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

Now, the `36` possible paths through the first example above are:
```
start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
```
The slightly larger example above now has `103` paths through it, and the even larger example now has `3509` paths through it.

Given these new rules, how many paths through this cave system are there?
