# Approach
### Data format

I decided to read the data into two sections: the rules and updates. The rules section is a map where the key is a given
page, and the value is a set of all valid updates for that page. The updates is just a list of lists of each of the updates.
So in the end, I have a data structure that looks like this:
```
{
	"rules": {
		1: {5, 7, 10, 13, 22, ...},
		4: {7, 3, 4, 1, 11, ...},
		...
	},
	"updates": [
		[47, 54, 23, 22, 11, ...],
		[66, 1, 23, ...],
	]
}
```
A couple of notes:
* We don't care about the "order" of the updates. Because of this, I used a `set()` for this data structure, because lookups are much faster and I can use `issubset()` later on...
* Because there are pages that have no pre-requisites, but might be updated, we have to make sure to add any pages to our "rules" map, even if the set is empty.

### Part 1
> _What do you get if you add up the middle page number from those correctly-ordered updates?_

The first step was just to identify which rows are valid, obviously. So I check validity by going through each element
in the update list and check that the set up updates AFTER it are ALL present in the rule for that given element. This is where
storing those valid updates as a `set()` made things really simple, as I can just use `.issubset()` to determine if a list
of elements is completely contained within the rules...

So, if I make it through the entire list of updates, it is a valid set. I then store it in a list of "valid" updates,
and if it fails at any point, I store it in a list of "invalid" updates.

Now, for part 1, I just need to take all of the elements in the "valid" list and get the middle elements and sum them up.
I do that by using integer division, since the arrays are all 0-based and an odd number, it works out that integer division
on the length by 2 will always give the middle element.

Add them up, and we're done.

### Part 2
> _What do you get if you add up the middle page numbers after correctly ordering just those updates?_

So it's not efficient, and I'm sure I could do it better, but basically, for each element in the "invalid" updates,
I iterate over each element until I find where it breaks the rules and I swap that element. I then restart and try again.

This means it's doing a lot of looping, when I could PROBABLY figure out a better approach...but it still finishes
in a few milliseconds, so I think it's good enough.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               3 |
| **Part Two** |              22 |
