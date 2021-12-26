# Approach
### Part 1
> _What is the least energy required to organize the amphipods?_

Alright! Let's parse this ASCII diagram into a data structure that makes sense and then add the rules allowed for movement.
Now we can iterate over all possible moves until we find a minimum...

...
...
...

Yeah, I ended up just writing this one out by hand. It took me about 5 minutes to do by hand and find the mimimum energy
required.

I equate this problem to a Towers of Hanoi -like problem: extremely easy to solve by hand once you know the pattern and
valid moves...but it's a pain in the ass to actually program.

So, I just didn't...I did it by hand, and it worked. I'll eventually go back and write the code to actually solve it...
some day...

### Part 2
> _Using the initial configuration from the full diagram, what is the least energy required to organize the amphipods?_

So, I just did the exact same thing I did for the first part: solved it by hand. It took a LITTLE bit longer, but still
much less time than it would have to program it. It took a few attempts, as my first couple tries apparently weren't
the most efficient, but they were close, and each time I was able to find small improvements until I finally got the
correct answer.

Again, I plan on coming back to this and solving it programmatically some day...

# Results

|              |     Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-----------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |      13495 |        2 |             N/A |             ~00:05:00 | 5745 |
| **Part Two** |      53767 |        5 |             N/A |             ~01:40:00 | 6603 |

# Original puzzle

### --- Day 23: Amphipod ---

A group of amphipods notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, "surely you can help us with a question that has stumped our best scientists."

They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: Amber (A), Bronze (B), Copper (C), and Desert (D). They live in a burrow that consists of a hallway and four side rooms. The side rooms are initially full of amphipods, and the hallway is initially empty.

They give you a diagram of the situation (your puzzle input), including locations of each amphipod (A, B, C, or D, each of which is occupying an otherwise open space), walls (#), and open space (.).

For example:
```
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
```
The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted A-D going left to right, like this:
```
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
```
Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of energy to move one step: Amber amphipods require 1 energy per step, Bronze amphipods require 10 energy, Copper amphipods require 100, and Desert ones require 1000. The amphipods would like you to find a way to organize the amphipods that requires the least total energy.

However, because they are timid and stubborn, the amphipods have some extra rules:

* Amphipods will never stop on the space immediately outside any room. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)
* Amphipods will never move from the hallway into a room unless that room is their destination room and that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)
* Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)

In the above example, the amphipods can be organized using a minimum of `12521` energy. One way to do this is shown below.

Starting configuration:
```
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
```
One Bronze amphipod moves into the hallway, taking 4 steps and using 40 energy:
```
#############
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########
```
The only Copper amphipod not in its side room moves there, taking 4 steps and using 400 energy:
```
#############
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########
```
A Desert amphipod moves out of the way, taking 3 steps and using 3000 energy, and then the Bronze amphipod takes its place, taking 3 steps and using 30 energy:
```
#############
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########
```
The leftmost Bronze amphipod moves to its room using `40` energy:
```
#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########
```
Both amphipods in the rightmost room move into the hallway, using `2003` energy in total:
```
#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########
```
Both Desert amphipods move into the rightmost room using `7000` energy:
```
#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########
```
Finally, the last Amber amphipod moves into its room, using `8` energy:
```
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
```
What is the least energy required to organize the amphipods?

### --- Part Two ---

As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:
```
#D#C#B#A#
#D#B#A#C#
```
So, the above example now becomes:
```
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
```
The amphipods still want to be organized into rooms similar to before:
```
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
```
In this updated example, the least energy required to organize these amphipods is `44169`:
```
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#
  #########

#############
#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#
  #########

#############
#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#
  #########

#############
#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#.#.###
  #D#B#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#A#
  #########

#############
#AA.D.....AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#.#
  #########

#############
#AA.......AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #.#B#C#.#
  #D#B#C#D#
  #A#B#C#D#
  #########

#############
#AA.D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #.#B#C#D#
  #A#B#C#D#
  #########

#############
#A..D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
```
Using the initial configuration from the full diagram, what is the least energy required to organize the amphipods?
