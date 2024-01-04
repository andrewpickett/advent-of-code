# Approach
### Data format

Store input as a list of integers.

### Part 1
> _What is the quantum entanglement of the first group of packages in the ideal configuration?_

Alright, this one was fun, but frustrating. The basic steps here are:
1. Figure out the target weight you're looking to have in each compartment (divide total by number of compartments).
2. Get all possible combinations of the weights and select only those that match the target weight
3. For each of the possible combinations, check if there are 2 other combinations that don't overlap with the same weight
4. Return the product of the first group (when sorted by size and quantum entanglement)

### Part 2
> _Now, what is the quantum entanglement of the first group of packages in the ideal configuration?_

Run the same basic code but with 4 compartments instead of 3. I could have tried to make this slicker and more extensible,
but I just hard coded another pass of the combination check.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             151 |
| **Part Two** |              12 |
