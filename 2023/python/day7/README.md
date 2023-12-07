# Approach
### Part 1
> _What are the total winnings?_

So clearly this puzzle is all about being able to sort and compare. My first thought was to have an array of the different
hand types ("full house", "two pair", etc) that are ordered by their strength. The issue becomes how do you represent
each of the hands easily so that you can do a quick lookup and figure out what kind of hand it is. My solution is to
simply count each of the letters in each hand and group them into a sorted tuple that represents the type of hand.

To figure out the final rank of the hands, I first just group all of the hands into buckets of like-types. Once I have those buckets
I go through each bucket of hand types and sort the hands based on their individual cards in the order dealt. The goal is
at the end of this to just have a single list of all of the hands in their ranked order. So then it's just a matter of
multiplying the bid by their index (+1 because of 0-based).

So basically, a hand like `AQTKA` has 2 `A`, 1 `Q`, 1 `T`, and 1 `K` in it, meaning its type can be represented as
`[2, 1, 1, 1]` which equates to "one pair". luckily there's a pretty simple way in Python to get a count of all characters
in a string mapped into a map:
```
{c: hand[0].count(c) for c in set(hand[0])}
```
This gives me a map of characters to counts, so then to get the array representation I care about, I just get the values
and sort them. Now I have every hand represented as that array, and I can do my first level of comparison by just checking the
types against each other.

After that, as I mentioned, just iterate over all the types and do a card-by-card comparison and sort in each bucket.

This leaves me with ordered buckets with ordered hands within each bucket. Just combine them all together into one
giant array and we now have ordered hands in one list!

### Part 2
> _Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?_

Because of how I implemented the "hand types" as numbers, it really was pretty easy to include jokers. The first step
is to change the cards by moving the `J` to the end to make it the lowest valued card. Then all I did was after getting
all of the characters in the hands, take however many `J`s there were and add that to the highest value in the character map
and then remove the `J`s. This will always ensure the `J`s get converted to make it the best hand possible.

So for example:
* Given `AQJJQ`, the character map would be `{"A": 1, "Q": 2, "J": 2}`
* We have 2 `J` cards, which we will simply add to the next highest occurring card (in this case `Q`), which means our resulting map looks like `{"A": 1, "Q": 4}` making it a four of a kind!

Because of the types of hands, this will always be the case that following this will give the best hand from the jokers!

So once we've finished that update, we just run through the same code we did in part 1.

There was one small edge case that needed to be accounted for, which is the `JJJJJ` hand. In this case, we can just keep the
map as `{"J": 5}` meaning it's a five of a kind. So I do have one manual check in there for that, but other that it was
pretty slick!

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        1 |             235 |              00:36:16 | 3510 |
| **Part Two** |        1 |             258 |              00:46:09 | 2353 |


# Original puzzle
### --- Day 7: Camel Cards ---
Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a **cool** airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of **Camel Cards**. Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of **hands**, and your goal is to order them based on the **strength** of each hand. A hand consists of **five cards** labeled one of `A`, `K`, `Q`, `J`, `T`, `9`, `8`, `7`, `6`, `5`, `4`, `3`, or `2`. The relative strength of each card follows this order, where `A` is the highest and `2` is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

* **Five of a kind**, where all five cards have the same label: `AAAAA`
* **Four of a kind**, where four cards have the same label and one card has a different label: `AA8AA`
* **Full house**, where three cards have the same label, and the remaining two cards share a different label: `23332`
* **Three of a kind**, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: `TTT98`
* **Two pair**, where two cards share one label, two other cards share a second label, and the remaining card has a third label: `23432`
* **One pair**, where two cards share one label, and the other three cards have a different label from the pair and each other: `A23A4`
* **High card**, where all cards' labels are distinct: `23456`

Hands are primarily ordered based on type; for example, every **full house** is stronger than any **three of a kind**.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the **first card in each hand**. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the **same label**, however, then move on to considering the **second card in each hand**. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, `33332` and `2AAAA` are both **four of a kind** hands, but `33332` is stronger because its first card is stronger. Similarly, `77888` and `77788` are both a **full house**, but `77888` is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding **bid** (your puzzle input). For example:
```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```
This example shows five hands; each hand is followed by its **bid** amount. Each hand wins an amount equal to its bid multiplied by its **rank**, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

* `32T3K` is the only **one pair** and the other hands are all a stronger type, so it gets rank **`1`**.
* `KK677` and `KTJJT` are both **two pair**. Their first cards both have the same label, but the second card of `KK677` is stronger (`K` vs `T`), so `KTJJT` gets rank **`2`** and `KK677` gets rank **`3`**.
* `T55J5` and `QQQJA` are both **three of a kind**. `QQQJA` has a stronger first card, so it gets rank **`5`** and `T55J5` gets rank **`4`**.

Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (`765` * 1 + `220` * 2 + `28` * 3 + `684` * 4 + `483` * 5). So the **total winnings** in this example are **`6440`**.

Find the rank of every hand in your set. **What are the total winnings?**

### --- Part Two ---
To make things a little more interesting, the Elf introduces one additional rule. Now, `J` cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, **`J` cards are now the weakest** individual cards, weaker even than `2`. The other cards stay in the same order: `A`, `K`, `Q`, `T`, `9`, `8`, `7`, `6`, `5`, `4`, `3`, `2`, `J`.

`J` cards can pretend to be whatever card is best for the purpose of determining hand type; for example, `QJJQ2` is now considered **four of a kind**. However, for the purpose of breaking ties between two hands of the same type, `J` is always treated as `J`, not the card it's pretending to be: `JKKK2` is weaker than `QQQQ2` because `J` is weaker than `Q`.

Now, the above example goes very differently:
```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```

* `32T3K` is still the only **one pair**; it doesn't contain any jokers, so its strength doesn't increase.
* `KK677` is now the only **two pair**, making it the second-weakest hand.
* `T55J5`, `KTJJT`, and `QQQJA` are now all **four of a kind**! `T55J5` gets rank 3, `QQQJA` gets rank 4, and `KTJJT` gets rank 5.

With the new joker rule, the total winnings in this example are **`5905`**.

Using the new joker rule, find the rank of every hand in your set. **What are the new total winnings?**
