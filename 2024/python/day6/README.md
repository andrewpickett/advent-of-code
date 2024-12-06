# Approach
### Data format

NOW it's time for me to dust off the old `Grid` class. Finally!

I decide to read in the input to my `Grid` so that I can "traverse" really easily. After going through part 1 and running
into some issues with lack of sleep causing me to overthink things, I came back and also just saved the starting position
so that I can easily "reset" the board for round 2.

### Part 1
> _How many distinct positions will the guard visit before leaving the mapped area?_

So today's puzzle is a very clear example of lack of sleep making my life much harder than it should be...

Part one was really very easy, I just keep track of my current position on the board (starting at the "start" location
found in the data setup), and move forward until I either end off of the board or hit an obstruction. If I hit an
obstruction, I just turn right and continue on. My `Grid` has methods for all of these actions, so it was really
very easy...

However, my brain was just not firing. I literally just kept making typos or making the logic so much more complicated
than it should be. I knew it was going to be ugly going into part 2...but part 1 finished fairly quickly, so whatever...

### Part 2
> _How many different positions could you choose for this obstruction?_

Yep, this one was also pretty simple in concept with my `Grid`. Like, seriously, all I would have to do is loop over
every point that is a `.`, set it to `#`, and run my part 1 logic. If it loops, then count it, otherwise, don't.

Alright, so...step 1: how do you determine a "loop"? This is where my lack of sleep started hitting me. I mean, it was pretty
clear to me that "if you traverse 2 consecutive steps twice", then you're going to be in a loop. So I started keeping track
of the path, and whenever I go to a new node and figure out my next position, I was trying to check my path so far
to see if my current and the next are next to each other in the visited list...but somehow my logic just wasn't working
out. My code was getting really ugly...I was not too happy...After a bunch of blurry-eyed debugging, I realized a slight
simplification made things a whole lot easier: "_if you land on any spot you've been on, travelling in the same direction as you
were last time_" then you're in a loop. While a small distinction, it meant I just had to keep track of the points AND the
direction I was travelling at those points in my path. Then just see if my current point/direction is in the path. Loop
detection done.

Next step: which points do I need to try putting obstacles? First thought was just to put it on all `.` positions one
at a time. Here's where it fell apart. I kept running the code and it wasn't working correctly. I realized I wasn't
"resetting" the board after each iteration. Specifically: the last direction travelled, the current_position, I was
still using the `^` character to denote my current position, which was making some positions no longer a `.`, which took
them out of the running, etc...So I decided to try to reset the board by just making a new copy of the original using
`deepcopy`. This started causing `RecursionErrors`. So I tried manually copying...this was a nightmare. I tried just
re-parsing the input for every new run of the algorithm...this was so slow and broke how I do these puzzles. My brain wasn't
firing, things were blurry...I was getting frustrated.

Finally, I took a 5 minute break, and came back with a slightly clearer head. I realized I don't need to actually change
the character of my current position, and I could just set the obstacle on the SINGLE board and then reset it when I'm done.
Then just reset the direction each loop and now I have a brand new grid to run. This started working, but it was really slow.

I then realized I don't have to check most of the `.` points. By definition, a new obstacle would only change the path
if that obstacle is ON THE PATH itself. So I just needed to run through the points on the path.

In order to do this more efficiently, I decided to save the path from the first part of the puzzle and pass it to the second
part so I didn't have to re-do it. In doing this, I ran it, and it finished in about 30 seconds. Not great, and I know
there are quite a few other optimizations I could do...but I needed to go to sleep. So I called it a day.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              16 |
| **Part Two** |           38957 |
