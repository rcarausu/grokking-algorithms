"""
  Hash tables

They use a function called 'hash function' that given a string (sequence of bytes) it returns
a number. It always returns the same number for a given string. This way we can use hash functions
to associate strings with array values, which are accessed via the numbers returned by the function
"""

# Which of these hash functions are consistent?

# 5.1 f(x) = 1 <-- Returns "1" for all input
# Consistent but doesn't map different strings to different numbers

# 5.2 f(x) = rand() <-- Returns a random number every time
# Not consistent

# 5.3 f(x) = next_empty_slot() <-- Returns the index of the next empty slot in the hash table
# Not consistent, doesn't take into account the input

# 5.4 f(x) = len(x) <-- Uses the length of the string as the index
# Consistent but different strings map to the same number

"""
  Collisions

It's impossible for hash tables to store all the items in existence, so collisions can occur 
(depending on how good your hash functon is). A collision is when two elements are assigned
to the same spot. 
There are several solutions for this, for example by instead of a slot in an array, using a linked 
list when inserting in an already occupied slot.

Load factor = nr of items / total nr of slots

  Performance

Best case: Read, Write, Insert take O(1) constant time
Worst case: Read, Write Insert take O(n), linear time

Performance depends on how good the hash function is, by distributing items evenly in memory.
"""

# Exercises

# You have the following hash functions:
# A. Return "1" for all input
# B. Use the length of the string as index
# C. Use the first character of the string as the index. So all strings starting with a are hashed together,
# and so on
# D. Map every letter to a primer number: a = 2, b = 3, c = 5, d = 7, e = 11, and so on. For a string,
# the hash function is the sum of all the characters modulo the size of the hash. For example, if your
# hash size is 10, and the string is "bag", the index is (3 + 2 + 17) % 10 = 22 % 10 = 2.

# Which of these hash functions provides a good distribution for the following cases:

# 5.5 A phonebook where the keys are names and values are phone numbers.
# The names are as follows, Esther, Ben, Bob and Dan.
# Answer: The C function would be best. Also D would give a good distribution.

# 5.6 A mapping from battery size to power. The sizes are A, AA, AAA and AAAA.
# Answer: The B and D functions would be best.

# 5.7 A mapping from book titles to authors. The titles are Maus, Fun Home and Watchmen.
# Answer: The B, C and D functions would be best.
