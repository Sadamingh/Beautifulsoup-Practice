# Challenge #15

Find all the second table of the following webpage by ```get_table.py``` file.

The url of the online webpage is,
```
https://en.wikipedia.org/wiki/Data_type
```

The output is,
```
<table>
<tbody><tr>
<td>- null is the left and right neutral:</td>
<td>append(null,A) = A, append(A,null) = A.
</td></tr>
<tr>
<td>- for a list, append is associative:</td>
<td>append(append(A,B),C) = append(A,append(B,C)).
</td></tr>
<tr>
<td>- bags add commutativity:</td>
<td>append(B,A) = append(A,B).
</td></tr>
<tr>
<td>- finally, a set is also idempotent:</td>
<td>append(A,A) = A.
</td></tr></tbody></table>
```

To test your result, run:
```
$ source checker.sh
```