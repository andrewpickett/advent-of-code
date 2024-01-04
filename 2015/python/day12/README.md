# Approach
### Data format

Just read the input as a single string. Nothing fancy.

### Part 1
> _What is the sum of all numbers in the document?_

I literally just took the entire document and did a regex and split the content on everything EXCEPT for numbers (and `-`
to account for negative numbers). Then just take the sum of all of them. It really was that simple.

### Part 2
> __

For this portion, I start at the root of the JSON object and recursively dig down into it. If at any point the value of a field
is `red`, I remove that entire object from the tree. Once I have removed all of the `red` fields, I just run the same code
as part 1 and it works.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               9 |
| **Part Two** |               5 |
