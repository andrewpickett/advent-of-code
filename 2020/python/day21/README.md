# Approach

### Part 1
> _How many times do any of those ingredients appear?_

Alright, so, this puzzle certainly sounded very simple at first. As I started writing different ways of storing the
input (2 sets, one dict, one list, etc), nothing was completely working how I wanted.

Basically I realized that I had to take an allergen listed, find all of the lines that had that allergen, then see
if there were any words common on ALL of those lines. If ever there was only ONE common word across all of the lines,
then I knew what the allergen --> ingredient mapping was.

So, I basically just took a stab at writing that using some sets and loops, and using the union funcitonality of Python
`set`s and tried it on the input. It worked, so I just figured, why not TRY it on my actual input.

Lo-and-behold, it worked right away. I fully expected my implementation to end up in an infinite loop on the puzzle input
because I just say "keep doing this until there are no more unmatched allergens". In the end, though, it neatly found
a map of ingredient to allergen.

Then I just removed all of those ingredients form the input, and counted how many remaining there were.

...little did I know...

### Part 2
> _What is your canonical dangerous ingredient list?_

So, I don't know how they expected you to solve part one, but I must have lucked into my solution, because at the end
of part one, I already had all of the allergens mapped out. All I had to do was order my list by the allergen and output
the ingredient associated with it. Super easy.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 2798  | 3  | 7  | 01:22:55  | 2815  |
| **Part Two**  | gbt,rpj,vdxb,dtb,bqmhk,vqzbq,zqjm,nhjrzzj  | 1  | 6  | 00:04:39  | 2586  |

# Original Puzzle

### --- Day 21: Allergen Assessment ---
You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't
even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your
journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed
in a language you do understand. You should be able to use this information to determine which ingredient contains
which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's
ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't
always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that
contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen
isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or
maybe it was labeled in a language you don't know.

For example, consider the following list of foods:
```
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
```
The first food in the list has four ingredients (written in a language you don't understand):
`mxmxvkd`, `kfcds`, `sqjhc`, and `nhms`. While the food might contain other allergens, a few allergens the food
definitely contains are listed afterward: `dairy` and `fish`.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list.
In the above example, none of the ingredients `kfcds`, `nhms`, `sbzzf`, or `trh` can contain an allergen. Counting
the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each
except `sbzzf`, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those
ingredients appear?

### --- Part Two ---
Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient
contains which allergen.

In the above example:
```
mxmxvkd contains dairy.
sqjhc contains fish.
fvjkl contains soy.
```
Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical
dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the
above example, this would be `mxmxvkd,sqjhc,fvjkl`.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
