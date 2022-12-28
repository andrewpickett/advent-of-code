# Approach
### Part 1
> _What is the surface area of your scanned lava droplet?_

I love when the inputs are super easy to read and parse! At least that part of this puzzle only took a couple seconds.

For this first part, my initial thought was just to find how many sides of each coordinate were covered by other cubes.
I start with the fact that every cube has 6 "exposed" sides. I then just loop over every other cube in the list and if any 2
of the coordinates match and the third is only off by 1, I know that that side of the cube is covered by another cube.
So in this case, I lower the number of exposed sides by 1. Once I have done that with all of the cubes, I can just sum
up all of the exposed sides for the answer.

### Part 2
> _What is the exterior surface area of your scanned lava droplet?_

So...basically I needed to rethink how this needed done for this point. Basically I now need to find all of the "gaps" inside
of the solid. So how do I do that? Well, the idea is that I can check the neighbors of a given point. If a neighbor is not
occupied, I then need to determine if it is "inside" the solid, or if it eventually escapes out to the open. I did this using
a simple flood-fill algorithm: For every neighbor that is "unoccupied" add it to a queue. Then pop off locations from the queue,
repeating that process until eventually either:
1. There are no cubes left on the queue.
   1. This means that all of the space is enclosed (doesn't flood out to the open).
   2. We can then effectively ignore those exposed sides as they are inside and will not get cooled by water.
2. The list just keeps growing and doesn't slow down.
   1. This means the water is flowing out into space, and therefore part of the "exterior".
   2. We can count that as 1 exposed side, as the water will eventually hit it and cool it.

Once we have done the flood-fill on all of the point's neighbors, we will have a total sum. The tricky part here is to figure out
at what point we consider the queue as "growing and not getting smaller" to identify when it floods out.

I started at an arbitrarily large number (around 100000), and then slowly started lowering it until I found my answer starting to
change -- at which point, it obviously was restricting more than it should. I ended up at 5000 as my limit. I'd like to have
a better way to identify it, but this works just fine for this purpose.

I could have probably gone back and redid part 1 in a similar way, which would have sped it up, but I kind of liked my
solution -- even though it's slower. So, in the end, this is one puzzle where part 2 will just run faster than part 1!

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |   3576 |        1 |            2779 |              00:13:47 | 1836 |
| **Part Two** |   2066 |        4 |             239 |              00:25:41 | 1334 |


# Original puzzle
### --- Day 18: Boiling Boulders ---
You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting!
Fortunately, the lava seems to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave,
you can see the lava landing in a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it might be forming obsidian! The cooling
rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).

Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates
the shape of the lava droplet with 1x1x1 cubes on a 3D grid, each given as its `x`,`y`,`z` position.

To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube.
So, if your scan were only two adjacent cubes like `1`,`1`,`1` and `2`,`1`,`1`, each cube would have a single side covered
and five sides exposed, a total surface area of `10` sides.

Here's a larger example:

```
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
```

In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is `64`.

### --- Part Two ---
Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also
included the surface area of air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond.
The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava droplet (at `2`,`2`,`5`), so the exterior
surface area of the lava droplet is `58`.
