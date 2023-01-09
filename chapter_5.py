"""
5. HASH TABLES

They use a function called 'hash function' that given a string (sequence of bytes) it returns
a number. It always returns the same number for a given string. This way we can use hash functions
to associate strings with array values, which are accessed via the numbers returned by the function.

- They need to be consistent.
- They should map different words to different numbers.

## Collisions

It's impossible for hash tables to store all the items in existence, so collisions can occur 
(depending on how good your hash functon is). A collision is when two elements are assigned
to the same spot. 
There are several solutions for this, for example by instead of a slot in an array, using a linked 
list when inserting in an already occupied slot.

Load factor = nr of items / total nr of slots

## Performance

Best case: Read, Write, Insert take O(1) constant time
Worst case: Read, Write Insert take O(n), linear time

Performance depends on how good the hash function is, by distributing items evenly in memory.
"""
