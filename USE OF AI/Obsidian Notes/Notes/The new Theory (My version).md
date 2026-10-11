# DLA to show how LPTE is a better ansatz than HEA


Instead of entanglement increasing the general ansatz’s expressivity, we’ll show how it helps 
LPTE more than HEA: 
	HEA is extremely expressive, which gets bad pretty fast due to existence of barren plateaus
	the DLA of HEA approaches close to SU($2^N$)
	
LPTE DOES NOT increase DLA if it is strictly local without a chain. $$\left[X_{1}X_{2}, Y_{1}Y_{2}\right]=0$$ for all local pairs as $$\{X_{i}X_{i+1},Y_{i}Y_{i+1}, Z_{i}Z_{i+1}\}$$
these form an Abelian Subalgebra
a single LPTE block is highly constrained, predictable, and doesn’t explore more of the hilbert space. 

BUT: 
if you take an LPTE chain: eg. $$[X_{1}X_{2}, Y_{2}Y_{3}]$$ forms a new operator, and this new operator chains itself further, forming even more newer operators. 
when you chain more overlapping pairs, the commutators generate more and more new non-local directions, and causes DLA to grow, expanding the reachable manifold, but this time, structured, and strategically. 
This allows TOPAZ to prune out entire local chains without changing the overall reachable manifold.





# The Structural Well: 

## What it is: 
### the parameter space $$\chi=\left[0,1\right]^M \times\left[0,\tau_{max}\right]^M$$
this is compact (closed and bounded)

### EVT (extreme value theorem):
if a function that is continuous is defined on a compact space, it will have global extrema. 
$L(U)$ is continuous, and defined on the compact parameter space $\chi$, so IT HAS AT LEAST ONE MINIMUM.

### How entanglement makes more minima:
by injecting non-commutative components, entanglement causes non-linearity of $L(U)$ and causes more minima locally and forces the loss landscape to become non-convex.
- it is SUFFICIENT, and NOT STRICTLY ESSENTIAL 
- but more entanglement means more minima, but at the cost of possibly introducing more barren plateaus

### different well floors:
this is a feature of the pruning mechanism, and is observed across different seeds because the regularizer optimizer may prune out different groups of operators depending on when its needed

## The explicit math
For a function: $f:A\rightarrow B$ $$M=\left\{x_{i}^{*}\vert_{k=1}^n \vert \nabla f(x_{i}^*)=0\vert \nabla^{2}f(x_{i}^*)>0 \right\}$$ which is the set of all minima
the family is: $$W= \left\{B(x_{i}^*)\vert x_{i}^* \in M\right\}$$
where: $$B(x_{i}^*) \cap B(x_{j}^*) = \phi \text{ }; \forall \text{ }i\neq j$$
$$\bigcup_{i=1}^kB(x_{i}^*)=A  \setminus \delta$$ where $\delta$ is all maxima, inflection and saddle points

for TOPAZ: 
the function has domain: $$X=[0,1]^M \times[0, \tau_{max}]^M$$ where M is the no. of entangling pairs 

the function is the loss function: $$L: X \rightarrow \mathbb{R}\text{ as } L(\rho, \tau)=1-|\bra{\psi_{ideal}}U_{safe} (\rho,\tau)\ket{\psi_{0}}|^2  $$
a sublevel set is defined as: $$S_{c}(L)=\{(\rho,\tau)\vert L(\rho,\tau)\leq c\}$$
a single well is defined as: $$B_{c}(x^*)\subseteq S_{c}(L)$$
if $x \in B_{c}(x^*)$, and $\nabla f(x) = 0$ then $x=x^*$

and finally $$- \nabla f(x)\cdot n(x)<0 \text{ } \forall\text{ } x \in \partial B_{c}(x^*)$$
the family is: $$W= \left\{B(x_{i}^*)\vert x_{i}^* \in M\right\}$$ 
## how it reduces noise: 
### The polar projection form 
$$B=QP$$
with a small perturbation $$B+\delta B=(Q+\delta Q)(P+\delta P)$$
$$\delta B=\delta QP+Q\delta P$$
now $P=P^{\dagger}$, so $\delta P = \delta P^{\dagger}$
and $Q^{\dagger}Q=\mathbb{I}$, so by the product rule: $Q^{\dagger}\delta Q+\delta Q^{\dagger}Q=O$
let $Q^{\dagger}\delta Q=\Omega$, so $\delta Q^{\dagger}Q=\Omega ^{\dagger}$$$\Omega+\Omega ^{\dagger}=O$$
so the polar form becomes: $$Q^{\dagger}\delta B=(Q^{\dagger}\delta Q)P+(Q^{\dagger}Q)\delta P$$
$$Q^{\dagger}\delta B=\Omega P+\delta P$$so $\delta P=Q^{\dagger}B-\Omega P$

now take the full conjugate transpose: $$\delta P^{\dagger}=(Q^{\dagger}\delta B)^{\dagger}-(\Omega P)^{\dagger}$$
$$\delta P=\delta B^{\dagger}Q+P\Omega$$
you solve, you get $$Q\Omega=\delta Q$$
if $B^{\dagger}B\approx \mathbb{I}$
$$\delta Q=\frac{1}{2}(\delta B-B\delta B^{\dagger}B)$$
and then if $\delta B$ is purely stretching: 
$\delta B=Q\delta P$
$\delta B=B\delta p$
so $$\delta Q=(B\delta P-B(B\delta P)^{\dagger}B)= O$$if the change is primarily stretching, it causes no change in state in the well where B is almost unitary.


### Gradient Invariance:
differential of pure quantum fidelity:
let $$U_{safe}(\rho,\tau)\ket{\psi_{0}}=\ket{\phi}$$
$$\delta \ket{\phi}= \delta U_{safe}\ket{\psi_{0}} $$
$$\delta \bra{\phi}=\bra{\psi_{0}} \delta U_{safe}^{\dagger} $$


fidelity: $$F=|\bra{{\psi_{ideal}}} \ket{\phi}|^2$$
loss function is 1 - F or $$L=1-\bra{\psi} \ket{\phi} \bra{\phi} \ket{\psi}$$
taking a derivative: $$\delta L=-\bra{\psi}\ket{\phi}\cdot\delta \bra{\phi}\ket{\psi}+\delta \bra{\psi}\ket{\phi}\cdot \bra{\phi}\ket{\psi}$$
which simplifies to: $$\delta L(\rho,\tau)=-2\mathrm{Re}(\bra{\phi}\ket{\psi}\cdot \bra{\psi}\delta U_{safe}(\rho,\tau)\ket{\psi_{0}})$$
now $\delta U_{safe}=D\text{ }P_{U}[\delta B]$
because noise is only perturbations that stretch, $\delta B = 0$ and $D\text{ }P_{U}[0]=O$ therefore $\delta U_{safe}=O$ and $\delta L=O$
meaning the GRADIENTS of the loss function are invariant.


### Diffeomorphism:
$$\nabla L_{noisy}=\nabla L_{ideal}+\nabla \nu_{noise}$$
but for perturbations that purely stretch, $\nabla \nu_{noise}=0$
so $\nabla L_{ideal}=\nabla L_{noisy}$ (or more accurately $\nabla L_{noisy}\approx \nabla L_{ideal}$)

so the map between them is $M=\nabla L_{ideal}+c=\nabla L_{noisy}$
and so $J(\nabla L_{ideal})=J(\nabla L_{noisy})$, so the map is differentiable. SO
$\nabla L_{ideal}$ is approximately diffeomorphic to $\nabla L_{noisy}$, showing diffeomorphic invariance.
### Homeomorphism:
Two structures are homeomorphic if the map between them is bijective, continuous and invertible, and are diffeomorphic if they are further, smooth and differentiable, meaning all diffeomorphisms are homeomorphisms, so $\nabla L_{ideal}$ is approximately homeomorphic to $\nabla L_{noisy}$ as well.
THEREFORE, all topological properties are invariant between the two, meaning the well transfers from the ideal loss landscape to the noisy landscape too.

# Self Pruning:
the Frobenius norm is the square root of the sum of all (elements$^2$), 
$\mathbb{F}^2=\text{sum of squares}$
if you have a matrix $A$, its frobenius norm squared is $\lvert \lvert A \rvert \rvert_{\mathbb{F}}^2$ $= Tr(A^{\dagger}A)$
the matrix here is $B^{\dagger}B-I$
so now, if you take the derivative of this with respect to B, you get $4B(B^{\dagger}B-I)$
if $B^{\dagger}B \neq I$ then the whole thing has a positive value


now, if a term only stretches the state, without changing the output, it increases error rates, and decreases fidelity, so we’d want to penalize it. 

$$L_{total}=L_{init}+\lambda \sum_{k}\lvert \lvert B^{\dagger}B-I \rvert  \rvert_{F}^2$$
does this by reducing $\rho$ to zero eventually. THIS IS THE PRUNING AT WORK

# The Equivalence Gap
we know that $\lvert L_{ideal}-L_{hardware}\rvert\leq K\cdot D$ where D is the state drift or trace distance. but calculating D is hard, so we use Fuchs-Van de Graafs stuff:
they said $D\leq \sqrt{ 1-F }$
but if there is an error $\epsilon$, we get $F\approx 1-c\epsilon^2$
so $D\leq \sqrt{ 1-(1-c \epsilon^2) }= \sqrt{ c }\cdot \epsilon$
therefore we get:  $\lvert L_{ideal}-L_{hardware}\rvert\leq K \sqrt{ c }\cdot \epsilon$ which is linear

- if $\epsilon$ enough, the well transfers from the ideal landscape to the hardware landscape

# why $\tau$ clusters around $\frac{\pi}{2}$

even though standard quantum mechanics says max entanglement is at $\pi/4$, if you take a local term $B(\tau)=(e^{-i\tau}XX+e^{-i\tau}YY+e^{-i\tau}ZZ)$
if you find B at $\tau=\pi/2$ you should get it to be $-i \cdot SWAP$
which is a MAXIMALLY ENTANGLING GATE.


# Noise model transferability
take the noise to be a vector $\mu=(P_{depol},\gamma_{amp}, \lambda_{phase})$
and the parameters $\chi=(\rho,\tau)$
so the loss function becomes: $L(\chi,\mu)$
if total change from noise is approximately purely stretching, $$\lvert  L(\chi,\mu_{1})- L(\chi,\mu_{2}) \rvert\leq K\lvert  \mu_{1} - \mu_{2} \rvert $$
and polar projection squishes K to almost zero because noise is purely stretching, meaning the well is lipschitz continuous and is $\approx$ invariant to different noise parameters

# The 4 properties: 
for an algorithm to work, the following must be true:
- the parameter space should be compact
- $L(U)$ should be lipschitz continuous by fidelity being lipschitz continuous on the active manifold.
- parameter domain $\chi$ is compact. a compact set in topology is defined to be convex, so $\chi$ is convex. topology also states that a convex set is path connected, and we proved that the well is connected to the sublevel set on $\chi$, (sublevel set is connected too), so the well guarantees path connectedness
- Convexity: $L_{init}$ is non-convex, but the regularizer term: $\sum_{k}\lvert \lvert B^{\dagger}B-I \rvert  \rvert_{F}^2$ call $\lvert \lvert X \rvert  \rvert_{F}^2=f(X)$
- is strictly a convex and quadratic form 
- so the hessian $\nabla^2_{X}f(X)$ is positive definite


BY TIKHONOV REGULARISATION THEORY:
- $\nabla^2 L_{total}= \nabla^2 L_{init}+\lambda \nabla_{X}^2f(X)$, the regularizer term can force its curvature onto L_init even if L_init is not positive definite, as long as lambda is large enough, which would mean any minimum in L_total is strictly a local minimum
