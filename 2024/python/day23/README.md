# Approach
### Data format

Graph algorithms time. I decided to create a simple graph using a dictionary where each key just maps to all of its
connected nodes as a set. I make sure to add both directions of the connection for each line in the file.

### Part 1
> _How many contain at least one computer with a name that starts with t?_

Alright, this one was pretty simple...It's not super efficient, but I just loop over every 3 nodes and check if they all
exist in one of their lists of connections. Since I stored all of the connections as `sets`, I was able to make use of the
`set` operations (like `difference`). Once I have all of the sets with 3 common nodes, I just return the number that have
any that start with `t`.

### Part 2
> _What is the password to get into the LAN party?_

Enter finding cliques! So, I immediately recognized this problem from previous years (in fact, it may have been a day 23
last year?) and knew that it was going to be a clique-finding problem. So I knew exactly what needed done. I also knew I
could use `networkx` and make this pretty much a trivial problem...

So I did that first...so I could get the answer really fast (the `networkx` package actually has a `find_cliques` method
that literally returns the largest clique).

Once I got the answer and submitted it, I decided to go back and try to implement my own solution, since I'm trying to
do all of these puzzles without using any libraries outside of the python core.

It's not pretty, and it's pretty slow...but given that it's an NP-complete problem, I'm pretty happy with my solution
(basically loop through all the connections, and continue to grow the common groups manually, keeping track of the
largest one). You can easily find any number of implementations of this algorithm if you look and need more explanation...
Like I said, once you know what the problem is (and the name of it!) it's fairly trivial.
I should probably look into the `networkx` codebase to see how it does things so much more efficiently, but
for now, I'm good with how this one works.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              60 |
| **Part Two** |           17267 |
