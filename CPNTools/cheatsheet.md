# Standard ML cheat sheet
standard ML is functional programming language
strong typed 
## Table of content
- variable declaration and standard data types
- functions
- list comprehensions and operations
- Examples


### Notation 
result of some of the codes are given using syntax
val it = 2.0 : real
under the command



### variable delcaration
```
val x = 10; int
val y = 1.0; real
val z = "abc"; string
val u = #"a"; char
val pair = (1,"abc")
val triple = (1,true,2.0)

```
### operators
string concatanations using ^^
```
"abc"^^"def";

```
indexing 

```
#3(triple); 
val it = 2.0 : real

val (x,y) = pair
```


### functions
lambda expressions
```
fn x => x+1
val twice = (fn x => 2*x);
```
invoking a function
```
twice y;
```
functions are defined explicitly using keyword **fun**
```
fun fac n = if (n=0) then 1 else n*(fac(n-1));
```


### List 
List constuction
```
1::nil;
val it = [1] : int list

val l = [1,2,3]
```

list operations
- hd : head 
- tl : tail

```
hd l;
val it = 1 : int

tl l
val it = [2,3] : int list
```

### Examples
function append two list
```
fun app nil l = l | 
                app(h::t) l = h::(app t l); 

app [1,2,3] [4,5,6]
val it = [1,2,3,4,5,6]
```
