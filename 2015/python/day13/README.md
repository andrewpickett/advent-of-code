# Approach
### Data format

I read each line of the input file and build a map of people to happiness levels for everyone
at the table. Parsing the data works because every line is formatted the exact same way:
```
{name} would {gain|lose} {amount} happiness units by sitting next to {name}
```

So if a line says "lose", we make the value negative, otherwise it's positive, and we just build the map using the names in each line.

The end result is something like this:
```
{
  "Alice": {
    "Bob": -2,
    "Carol": -62
  },
  "Bob": {
    "Alice": 93,
    "Carol": 19
  },
  "Carol": {
    "Alice": -54,
    "Bob": -70
  }
}
```

### Part 1
> _What is the total change in happiness for the optimal seating arrangement of the actual guest list?_

I really just create a map of happiness values between all people at the table. At that point, I brute force the
analysis by getting all permutations of people at the table and then using that map to calculate the total happiness.
I did no optimizations in this, just run through all of them and add up the maximums I get for each.

### Part 2
> _What is the total change in happiness for the optimal seating arrangement that actually includes yourself?_

Just add a `Me` node to the graph and run it again.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             229 |
| **Part Two** |            2256 |
