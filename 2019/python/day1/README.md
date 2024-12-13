# Approach
### Data format

Read input as a list of ints. That's it.

### Part 1
> _What is the sum of the fuel requirements for all of the modules on your spacecraft?_

Just have to add up the sum of every value in the list divided by 3 and subtracted by 2. One line of code...done...

### Part 2
> _What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel?_

Now just take that same calculation over and over until we are at zero required and add that up. Nothing fancy here.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
