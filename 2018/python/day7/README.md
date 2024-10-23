# Approach
### Data format

I store a list of all of the steps, and which steps can follow them once completed. Likewise, I keep a list of the steps
that are required BEFORE a step can be completed. This way I can do a lookup both directions, to get the next
possible steps as well as being able to check if all prerequisites have been met or not.

Finally, I decided to keep a list of available next steps in the same map, since I needed to find the "original" starting
point anyways.

### Part 1
> _In what order should the steps in your instructions be completed?_

The code is really ugly, but the idea is pretty simple: just iterate through the "available" next steps. Use the lookup
map to find which ones can be done after it is complete, but only add them if every item in the "prerequisite" map
is also already complete. Just keep the "available" list sorted alphabetical.

Once you are out of items in the available list, then we're done.

### Part 2
> _With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?_

Since we now have multiple workers, each processing at their own "speeds", I figured it was time to rewrite my part
1 solution so that it was class-based. I created a `Worker` class that basically stored which value it is currently
working on and how much time that value will take to complete.

Then, I pretty much just do the same loop as I originally did on part one, but I loop over every worker and let each one
pull any available letters from the queue if it is ready to work.

I ran into quite a bit of trouble keeping track of which ones are ready to work and which ones have been completed and
everything -- but once I finally kept proper track of it all, it made a lot of sense.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              40 |
| **Part Two** |              28 |
