# Execute Brainfuck 

A tiny brainfuck executer in about 512 bytes (~584 bytes).

### Explanation

`bf.py` translates every instruction from Brainfuck to Python.
That means that it creates a script in Python and then run it,
using the following dictionary of instructions

```python
INS = {">":"P+=1", 
       "<":"P-=1", 
       ".":"print(chr(S[P]),end='')",
       ",":"S[P]=ord(input())", 
       "+":"S[P]+=1", 
       "-":"S[P]-=1",
       "[":"while S[P]:",
       "]":"pass"}
```

where `P` is the pointer and `S` is a list of length `30000`.

The following function works as a parser, 
furthermore it translates from a list of Brainfuck 
commands to Python commands preserving loops.  

```python
def R(t):
    I=[]
    while len(t):
        c,*t=t;I.append(INS[c]);
        if c=='[':q,t=R(t);I.append(q);
        if c==']':return (I,t);
    return I
```

while the following function formats and indents the list of 
instructions in order to be compatible with python identation

```python
def F(n,i=0):
    k=""
    for x in n:
        if type(x)==list:I=F(x,i+1);k+=I;
        else:k+="\t"*i+x+"\n";
    return k
```


### Usage

Use python version `>=3.7` and type 

    python bf.py path/to/file.bf

### Examples

Those examples are from the [Brainfuck wikipedia page](https://en.wikipedia.org/wiki/Brainfuck)