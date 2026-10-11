- ![[QUBO.pdf]]

- stands for **Quadratic Unconstrained Binary Optimization** (problem)
- so basically:
  you have n-bits $X=\{x_{1},x_{2},x_{3}\dots x_{n}\}$
  and each bit does a separate thing. so changing $x_{i}\in X$ 
  0 → 1 costs resources, so each bit has its own weight.
  
  [[QUBO]] is basically a function$$F(x)=C+\sum_{i} a_{i}x_{i}+\sum_{i<j} b_{ij}x_{i}x_{j}$$here $x_{i}\in \{0,1\}$ and a and b are the weights, a shows how much changing $x_{i}$ from 0 → 1 costs and b shows how much it would cost to turn both $x_{i}x_{j}$ from 0 → 1. 

- i<j cuz if ij AND ji, its double counted as $x_{i}x_{j}=x_{j}x_{i}$

- these are basically the penalty terms, so for example, i want to enforce x1 = 1, i can do that by adding a penalty term $P(1-x_{1})$. if the optimizer keeps $x=0$ the penalty term is added. that is kept very high. if the main goal is to minimize the cost, the optimizer will say ew and try to keep $x_{1}$ = 1. 
  for multiple bits, just keep multiple single bit penalties for enforcing different rules. 
 




this can be compressed into the linear algebraic form:
- $F(x)=x^{T}Qx$
- $x$ is the vector of all bits, its transpose is $x^{T}$ 
- Q is all the weights, $q_{ii}$, or the diagonal elements are linear weights, $q_{ij}$, or the off-diagonal elements are the quadratic weights. and Q is NxN for N = no. of bits.
	- `Q is usually taken symmetric, with diagonals from the linear terms and off‑diagonals built from the pairwise weights (sometimes with a 1/2 factor depending on convention)
  simplifying all of this gives you the quadratic bit string
- this form is the simpler form, it is easier for solvers to accept
- forms the definition of QUBO: minimise F(x) as: $$F(x)=x^TQx; \text{ } x_{i}\in\{0,1\}$$
or in words, it minimizes the cost function over binary x.