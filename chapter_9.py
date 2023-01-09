"""
9. DYNAMIC PROGRAMMING

Dynamic programming starts by solving sub-problems and builds up solving the main problem.

All dynamic programming algorithms start with a grid, which is used to calculate the "values" of all sub-problems.

The final answer is a combination of some sub-problems solved in the firsts steps.

The formula to calculate each cell of the grid is:

                    | 1. The previous max (value at cell[i-1][j]
cell[i][j] = max    |
                    | 2. Value of current item + value o the remaining space -> cell[i-1][j - item's weight]

    i = row
    j  = column

## FAQ

- We can add items (new rows) since the algorithm builds up progressively on your estimate.
- The order of the rows doesn't change the result.
- Filling the grid column-wise or row-wise may change the results of some problems, it depends. For some, it may be
better.
- Smaller items (when added) change the granularity of the problem, so we need to recalculate the whole grid.
- It doesn't work with fraction of an item, but for that we can use greedy algorithms.
- Dynamic programming only works when each sub-problem is discrete, when it doesn't depend on other sub-problems.

## Main takeaways of dynamic programming (so far)

- It's useful when trying to optimize something given a constraint.
- We can use it when the problem can be broken into sub-problems, and they don't depend on each other.

It can be hard to come up with a DP solution. Some tips:

- Every DP problem involves a grid.
- The values in the cells are usually what you're trying to optimize.
- Every cell is a sub-problem, so think how to divide the main problem.

## How to make a grid?

You need to answer these questions:
- What are the values of the cells?
- How do you divide this problem into sub-problems?
- What are the axes of the grid?

In dynamic programming, you want to 'maximize' something. That's what you want to calculate.

The values of the cells are usually what you're trying to optimize.

## Filling the grid

There's no easy way to calculate the formula. You have to experiment and try to find something that works.

Algorithms are a framework that you build on top of.

For some problems, the final solution might not be the final cell!

(See the longest common substring and the longest common subsequence examples in the book for more details).

"""
