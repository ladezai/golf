# Code golfing in python

### Conditions

```python
if condition(a,b):
    return a
else: 
    return b
```
is similar in most cases as
```python
return(b,a)[condition(a,b)]
```
since an Iterable I, `I[True] = I[1]` and `I[False] = I[0]`.


### List unpacking

Since strings are _lists_ (if you use Haskell's definition)
using the following code allows to unpack a string back into a list. 

```python
*s, = 'longstring'
s
>>> ['l', 'o', 'n', 'g', 's', 't', 'r', 'i', 'n', 'g']
```

note that this trick works as well for all iterable, i.e. for ranges.

```python
*s, = range(5)
s
>>> [0, 1, 2, 3, 4]
```

### List indexing

By using `~i` you get the `L-i-1` element of a list of length `L`.

```python
*s, = range(5)
s[~0]
>>> 4
```


### Math floor and ceil 

The following common functions `math.floor(n)` and `math.ceil(n)` 
are, respectively, the same as `n//1` and `-(-n//1)`.


# Bibliography

1.https://codegolf.stackexchange.com/questions/54/tips-for-golfing-in-python



