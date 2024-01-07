# Approach
### Data format

For this one, I knew I wanted to read each line into an object of subnets and hypernets as arrays...so something like this:
```
[
	{
		"subnets": ["abcd", "efgh", "ijkl"],
		"hypernets": ["mnop", "qrst", "uvwx"]
	}
]
```

This was relatively easy with the format of the input file, because if you just split the line on the `[` and `]`
characters, every odd element is a subnet and every even element is a hypernet. I'm sure there's a better/more pythonic
way to do what I did, but it's fine and pretty quick, so, I'm fine with it.

### Part 1
> _How many IPs in your puzzle input support TLS?_

Really, I just go through each of the objects as defined above and count the number of "abba" strings there are the
list of subnets and hypernets...if there are any in the subnets and none in the hypernets, I count it as valid and
in the end just return the total number counted. Pretty simple!

### Part 2
> _How many IPs in your puzzle input support SSL?_

Basically the same idea, but this time, I would iterate over the supernets first, find any parts of the data that matched the `aba`
pattern. Whenever I found one, I then lopped over ALL hypernets in the input to find if there were any `bab`. If I found one,
I could count it valid and stop processing.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              23 |
| **Part Two** |              17 |
