# Approach
### Data format
Well, since the data are listed with timestamps in `yyyy-MM-dd` format, doing a simple "alphabetical sort" on them
will leave them in chronological order (hence, why that's the only valid date format!). So the data are just
read in and sorted in an array.

### Part 1
> _What is the ID of the guard you chose multiplied by the minute you chose?_

Just run through every single entry and create a chart similar to what the example showed. Since it's already ordered chronologically,
we just need to add a guard to each minute tht they're present. We then can just go over the chart and find the guard number
that has the highest count and find which minute it was.

### Part 2
> _What is the ID of the guard you chose multiplied by the minute you chose?_

Pretty much the same strategy as part 1, but actually easier as we don't have to add up the counts over the whole input.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |               1 |
