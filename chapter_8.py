"""
8. GREEDY ALGORITHMS

A greedy algorithm is simple, at each step, pick the optimal move.
In technical terms, at each step you pick the locally optimal solution, and in the end you're
left with the globally optimal solution (or an approximation).

## The set-covering problem

Suppose a radio show who wants to reach listeners on all 50 states.
You have to decide which stations to play in order to reach all the listeners.
Each station costs money, so you want to minimize that. You have a list of stations.
Each station covers a region, and they can over leap.

How to figure the smallest set of stations to cover all 50 states? This is very hard!

1. List every possible subset of stations. This is called the 'power set', and has 2^n solutions, where n
is the number of stations.

2. From there, pick the set with the smallest number of stations that covers all 50 states.
Problem is that it takes O(2^n) time to calculate each subset, which can translate in a lot of time.

There isn't any algorithm fast enough!

## Approximation algorithms

We can solve it with a greedy algorithm

1. Pick the station that covers the most states that haven't been covered yet. It's ok if it covers some states
that have been covered already.

2. Repeat until all states are covered.

This is an 'approximation algorithm'. They are judged by:

- how fast they are
- how close they are to the optimal solution.

In this case, it runs in O(n^2) time, where n is the number of stations.

## Sets

Basic datastructure where every item appears only once, then don't allow duplicates.
Basic operations are union (|), intersection (&) and difference (-).

## NP-Complete problems

These are famously hard problems (n!) to resolve where (most people) think it is not possible to find an algorithm
to solve them, only approximations. Most famous examples are the travelling-salesperson and set-covering problem.

How to identify NP-complete problems?

- algorithm gets slow when many items are involved.
- "all combination of X" point to NO-Complete problem.
- if it involves a sequence & it's hard to solve.
- if it involves a set & it's hard to solve.
- if it can be restated as the travelling-salesperson or the set-covering problems.

"""

# Example implementation of radio show and states problem


if __name__ == '__main__':
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

    stations = dict()

    stations['kone'] = {'id', 'nv', 'ut'}
    stations['ktwo'] = {'wa', 'id', 'mt'}
    stations['kthree'] = {'or', 'nv', 'ca'}
    stations['kfour'] = {'nv', 'ut'}
    stations['kfive'] = {'ca', 'az'}

    final_stations = set()

    while states_needed:
        best_station = None  # station that covers most of the states, there isn't just one possible solution
        states_covered = set()

        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station  # intersection of sets
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered  # difference of sets
        final_stations.add(best_station)

    print(final_stations)
