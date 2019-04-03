#!/usr/bin/python
from table import Table

table = [["head1", "head2"], ["one", "two"],["three", "four"]]
Table.print_table(table)

table2 = [["head1", "head2", "head3"], ["one", "two", "three"],
 "three four five".split(),
 "six seven eight".split(),
 "nine ten eleven".split(),
 "twelve thirteen fourteen".split()]
Table.print_table(table2)
