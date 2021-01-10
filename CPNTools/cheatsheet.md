# Standard ML cheat sheet
standard ML is functional programming language
strong typed 
## Table of content
- Variable declaration and standard data types
- Operators
- Functions
- List comprehensions and operations
- Records
- Patterns
- Local declaration
- Examples
- Resources


### Notation 
result of some of the codes are given using syntax
val it = 2.0 : real
under the command
or by using 
=> and variable names in the last command



### Variable Delcaration
SML have Integers , reals , booleans , Strings , Lists , Tuples , Records , ...

value binding examples
```
val x = 10; 
val y = 1.0; 
val z = "abc"; 
val u = #"a"; 
val pair = (1,"abc")
val triple = (1,true,2.0)

```
and comments can be written inside (* comment here *)

### Operators
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

:: : add an element to a list
```
val l = [1,2,3];
5::l
```

@ : concatenate two list
```
[1,2,3]@[4,5,6]
```

### Functions
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
function binding examples
```
fun fac n = if (n=0) then 1 else n*(fac(n-1));
```
polymorphic functions
```
fun mklist x = [x]
```
function as parameter
```
fun map f [] = [] | map f (h::t) = (f,h)::(map f t);

map (fn x=> x+1) [1,2,3]
val it = [2,3,4]

map 

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

### Records

```
val car = {make="Ford" , year = 1910};
val mk = #make car;
val yr = #year car;

```

### Patterns
a form to decompose compund values, commanly used in value bindings and function arguments

```
val list = [1,2,3];
val fst::rest = list
```
fst = 1 , rest = [2,3]

```
val list = [1,2,3];
val [x,_,y] = list
```
x=1 , y=3

match rule : pat => exp
when a match is applied to a value v , we try rules from left to right, looking for the first pattern matches v.we then bind the variable
in the pattern and evaluate the expression

pat1 => exp1 | ... | patn => expn

**case** exp **of** match

fn match

fun f pat1 = exp1 | f pat2 =  exp2 | ... | f patn = expn


```
fun length l = (case l 
                of [] => 0 
                | [a] => 1
                | _::r => 1 + length r
                (* end case *))

```
same function using another notation
```
fun length [] = 0 
    | length [a] = 1
    | length (_ :: r) = 1 + length r

```
more examples 
```
fun even 0 = true
    | even n = odd(n-1)

fun odd 0 = false
    | odd n = even(n-1)
```

### Local declaration
let <decl> in <exp> end
```
let val x=3
    fun f y = (y , x*y)
in
    f(4+x)
end
```




### Examples
function append two list
```
fun app nil l = l | 
                app(h::t) l = h::(app t l); 

app [1,2,3] [4,5,6]
val it = [1,2,3,4,5,6]
```

### Resources
[Waterloo](https://www.cs.princeton.edu/courses/archive/fall08/cos441/notes/lect-SMLNJ.pdf)
[uchicago](https://www.classes.cs.uchicago.edu/archive/2007/winter/22610-1/docs/sml-tutorial.pdf)