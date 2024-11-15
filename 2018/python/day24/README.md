# Approach
### Data format

I originally tried just making a dictionary holding all of the properties, but I was getting into issues with pointers
and finally decided to just create objects.

So basically I just read the input and store all of the groups into custom `Group` classes and then store a list of those
into an `Army` class. Now I can just manipulate the objects in place.

### Part 1
> _As it stands now, how many units would the winning army have?_

Break it up into the different phases:
1. Target Selection
	* Just loop over all the enemies and decide which target each attacker will attack and then set it on the object.
2. Attack
   * Now for each of the targets assigned, just lower the number of units.
3. Reset
   * Clear the targets and just move on.

The only "gotcha" here was to make sure to not account for any groups that had 0 units. I could have removed them from
the list completely, but figured, it didn't hurt to just keep them in there...I just had to add a few checks to make sure
they were never targeted.

End the fighting once either army has no more units in all of the groups.

### Part 2
> _How many units does the immune system have left after getting the smallest boost it needs to win?_

Just brute force it. Start at a `boost` of 1 and try the fight. Check if immunity army wins. If not, then increse the boost
by 1 and try again. Just keep doing this until the immunity army is the one that wins.

The big catch here is that there are times when either army can't kill any more units. Since we discard any "remainder"
attack power, it means they will just continually fight forever not killing each other. So to solve for this, I just put
in a check for how many units are in the fight at the beginning and then how many are at the end. If ever it's the same
number, you know you're deadlocked and we can just quit then and there.

So...doing that, it worked in about 15 seconds. Not bad...and good enough for me.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              84 |
| **Part Two** |           14345 |
