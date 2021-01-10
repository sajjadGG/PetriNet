# Colored Petri Net 
In this document we go over Colored Petri Net definitoins and concepts
and look at some example.

## Table of Contents
- Definitions
- Examples
- Formal Definition
- Hierachical colored petri net


### Hierachical Colored Petri Net
CPN with modules , benefits -> abstraction and all the advantages of component and modular based designs
it can be done both ways top down or bottom up
modules interact via port places
- input port
- output port
- internal port
- input/output port
we call these modules **substitution transitions**
the places surroundings substitution transitions are **socket places** 
they constitute theb interface for the substitution transitions.
- input port <-> input socket
- output port <-> output socket
- input/output port <-> input/output socket
port and socket that are related to one another constitute different views of single compound place
They have the same marking

Substitution transitions do not have arc expressions and guards
They do not become enabled and they do not occur
Instead they represent the compound behaviour of their submodules

Each instance of a module has its own marking.(like instances of a class)
