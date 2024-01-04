# Approach
### Data format

I read each line of the input file and build a map of each reindeer which maps to a list of attributes.
Parsing the data works because every line is formatted the exact same way:
```
{name} can fly {speed} km/s for {time}, but then must rest for {rest} seconds
```

The end result is something like this:
```
{
  "Vixen": {
    "s": 8,
    "t": 8,
    "r": 53,
    "p": 0
  },
  "Blitzen": {
    "s": 13,
    "t": 4,
    "r": 49,
    "p": 0
  }
}
```
The `p` key was added for part to account for the points they have accumulated. I just initialize them to `0`.

### Part 1
> _Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?_

You can think of each "cycle" of a reindeer's flight to be time flying at full speed plus the time resting. That really gives
their "true speed" after a given amount of time.

For example, if a reindeer has a speed of 10 km/s for 20 seconds and must rest for 5 seconds after flying, then they have a 25 second
"cycle" where they will fly 200 km in the first 20 seconds, and then rest in the next 5. This will repeat over and over
until we're at the time limit.

So for each reindeer we first divide the end time by this total cycle time. There will likely be SOME remainder of time left.
Since they are doing all their flying at the beginning of their cycle, we can check if the remainder is more than the time
they're able to fly. If it is, then they have flown their full distance for that last cycle...otherwise, we just return the
remainder because that's all they were able to fly.

So do that for all of the reindeer and then return the maximum to find the winner.

### Part 2
> _Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?_

For this part, I just calculate the distance for each reindeer after every second and whichever one is in the lead, I add one
point to their "points" counter. At the end of 2503 seconds, I return the highest point score.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |              17 |
