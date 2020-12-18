# Approach

### Part 1
> _Evaluate the expression on each line of the homework; what is the sum of the resulting values?_

Well, it's been about 15 years since I wrote a lexical parser, and the last time I did, it was a BEAST.

Luckily the rules for this "language" were really simple, and the tokens were very easy to evaluate.

So, the basic idea here is keeping a stack of statements that need evaluated. As you look at the tokens,
when you run across a '(', that signifies a new statement that will need to be evaluated before the one
you are currently running. So that means adding a new stack to the current stack. You do this for every
'(' that you run into. When you hit a ')', that means you need to pop the last statement off of the stack
and evaluate it. Again, do this for every ')' you run across. Using the example they gave
(`1 + (2 * 3) + (4 * (5 + 6))`), this is how it looks internally:
```
[[1, +, [2, *, 3], +, [4, *, [5, +, 6]]]
```
So you can see each of the stacks nested in the other stacks. So you just need to evaluate the stack
whenever you pop it...which would look something like this:
```
[[1, +, [2, *, 3], +, [4, *, [5, +, 6]]]
[[1, +, 6, +, [4, *, [5, +, 6]]]
[[1, +, 6, +, [4, *, 11]]
[[1, +, 6, +, 44]]
[51]
```
Since there is no precedence to the operators, it's pretty easy to just evaluate left to right once there
are no remaining sub-sets (aka statements) to evaluate.

Then just sum all of them together and return the value.

### Part 2
> _What do you get if you add up the results of evaluating the homework problems using these new rules?_

While it sounds like it will complicate matters, it really doesn't change much. You still create the
stack of stacks, it's just your evaluation function changes. The way I decided to implement it is
once you have a "flat" statement, just find all of the '+' and evaluate them one at a time, replacing
the 3 elements (a + b) with one (the actual sum). Continue to do this until there are no more
addition operators left in your flat statement

Once you do that, you know you're left with just a flat statement of multiplication that you need to
evaluate. That can be done with a comprehension and that is that.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 1890866893020  | 1  | 6  | 00:00:00  | 2183  |
| **Part Two**  | 34646237037193  | 1  | 8  | 00:00:00  | 1576  |

# Original Puzzle

### --- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you
are interrupted by the child sitting next to you. They're curious if you could help them with their
math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (`+`),
multiplication (`*`), and parentheses (`(...)`). Just like normal math, parentheses indicate that the
expression inside must be evaluated before it can be used by the surrounding expression. Addition still
finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before
addition, the operators have the same precedence, and are evaluated left-to-right regardless of the
order in which they appear.

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are as follows:
```
1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                   71
```
Parentheses can override this order; for example, here is what happens if parentheses are added to
form `1 + (2 * 3) + (4 * (5 + 6))`:
```
1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
7      + (4 * (5 + 6))
7      + (4 *   11   )
7      +     44
51
```
Here are a few more examples:

* `2 * 3 + (4 * 5)` becomes `26`.
* `5 + (8 * 3 + 9 + 3 * 4 * 3)` becomes `437`.
* `5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))` becomes `12240`.
* `((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2` becomes `13632`.

Before you can help with the homework, you need to understand it yourself. Evaluate the expression on
each line of the homework; what is the sum of the resulting values?

### --- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when
they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're
familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are now as follows:
```
1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
231
```
Here are the other examples from above:

* `1 + (2 * 3) + (4 * (5 + 6))` still becomes `51`.
* `2 * 3 + (4 * 5)` becomes `46`.
* `5 + (8 * 3 + 9 + 3 * 4 * 3)` becomes `1445`.
* `5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))` becomes `669060`.
* `((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2` becomes `23340`.

What do you get if you add up the results of evaluating the homework problems using these new rules?
