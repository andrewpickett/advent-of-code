# Approach
### Data format

First step, as usual is parsing the input data into format we can work with. I start by first just creating a list of the
ingredients, which are each a list of their properties. I then create a list of all possible amounts of the 5 ingredients
that add up to 100 -- it's only 176,849 possibilities after all...

It results in a data structure that looks like this:
```
{
	"ingredients": [
		[3, 0, 0, -3, 2],
		[-3, 3, 0, 0, 9],
		...
	],
	"counts": [
		[0, 0, 0, 100],
		[0, 0, 1, 99],
		[0, 0, 2, 98],
		...
		[99, 0, 0, 1],
		[99, 0, 1, 0],
		[99, 1, 0, 0],
		[100, 0, 0, 0]
	]
}
```

### Part 1
> _Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?_

Now that I have a list of all possible ingredients that add up to 100, I just run through every single one and calculate their score.
Then return the maximum!

It's not optimized at all, but it's not bad...

### Part 2
> _Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?_

For this one, we do the exact same thing, but add a step of calculating the calories for each cookie. I then
only need to check values for those that have exactly 500 calories and return the maximum.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             898 |
| **Part Two** |             379 |
