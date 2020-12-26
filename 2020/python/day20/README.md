# Approach

### Part 1
> _What do you get if you multiply together the IDs of the four corner tiles?_

I don't know why, but when I saw the input, I immediately thought "binary". Since for this part, we only cared about
the edges of the tiles, I went ahead and converted each edge of every tile to a number by converting the string of
`.` and `#` to `0` and `1`. This gave me 4 numbers for each tile. In order to find the corners, I just needed
to find the tiles that had 2 numbers that didn't match any other numbers.

Now, the fact that any of the squares could be rotated any direction caused me a bit of a headache, because I did have to
actually assign 8 numbers to each tile (the 4 original, and then the 4 reversed to account for rotations)...But when
actually CHECKING that, I only had to check the original 4 against all 8 of every other.

Long story short, I was able to find the 4 tiles really quickly and get the result without actually doing anything with
the full arrays of tiles as they were. Win!

### Part 2
> _How many # are not part of a sea monster?_

This part sucked.

So...I was really proud of my part 1 solution, and because it was all mathy and didn't actually do much with the
arrays, I was determined to figure out how to do part 2 with as little array manipulation as I could. So I probably spent
5 or 6 hours trying to complete just the first part of this puzzle using my existing soluation for part 1. I tried
everything to get all my tiles lined up and arranged as the full image using just the integer values for all of
the edges...and I just kept getting error after error.

So, I decided to scrap it completely and go with a straight object-oriented approach to solving it: Create a tile object
and perform rotations, neighbor checks, etc, within that object.

Now, I haven't done a lot of OO work within Python, so I kept fumbling over stupid errors (static variables instead of
instance, etc)...but after another 5 or 6 hours, I came up with a pretty slick solution to build my full image:

* Find the corners, just like we did in part 1.
* Pick any one of them and find all of its neighbors (based on matching the edges).
* Rotate that tile until it aligns to the upper left corner of the image.
* Now, I have the upper left tile in place, and I know its right and bottom neighbors.
* Take the right neighbor and find all of its neighbors.
* Do this until you no longer have any right neighbors...we now have the full top row done.
* Go back to the first tile and find its bottom neighbor...and then repeat going to the right and down until the entire
image is filled.

Now, by now you should know my distaste for multidimensional arrays, so instead of storing the image as a 2d array, I
decided to store it as just a basic array.

Ok, first hurdle complete. Removing the borders was easy (especially since I did it OO). So that wasn't a problem.
Now, combine the whole thing into ONE array of rows. That took a little chicken scratch to map out, but in the end,
I had one array of strings, each entry being a row of the final image.

To find the sea monsters, I started with the left most point of the sea monster and labeled it point `(0,0)`.
I went through and labeled all the other points in relation to it.

Traverse through my entire image and whenever I get to a `#`, I check to see if every other point in the sea monster
is also a `#`. If all are, I count it as a found monster and keep going until I check the whole image.

Now, I wrap all of this in rotation/flipping logic in order to find which orientation actually had any sea monsters,
but thats the basic idea.

Finally done, after about 15 hours or so...ugh.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 7492183537913  | 1  | 25  | ~00:45:00  | 7854  |
| **Part Two**  | 2323  | 1  | 1105  | ~15:00:00  | 10654  |

# Original Puzzle

### --- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since
you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information
Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the
satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they
produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles
(your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random
orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly
with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented
correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other
tiles.

For example, suppose you have the following nine tiles:
```
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
```
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to
line up:
```
#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
```
For reference, the IDs of the above tiles are:
```
1951    2311    3079
2729    1427    2473
2971    1489    1171
```
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this
with the assembled tiles from the example above, you get `1951 * 3079 * 2971 * 1171 = 20899048083289`.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

### --- Part Two ---
Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:
```
.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###
```
Remove the gaps to form the actual image:
```
.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
```
Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:
```
                  #
#    ##    ##    ###
#  #  #  #  #  #
```
When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might
need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after
flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with `O`):
```
.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
```
Determine how rough the waters are in the sea monsters' habitat by counting the number of `#` that are not part of a
sea monster. In the above example, the habitat's water roughness is `273`.

How many `#` are not part of a sea monster?
