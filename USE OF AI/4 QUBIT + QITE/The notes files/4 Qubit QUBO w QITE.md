[[Quantum Imaginary Time Evolution|QITE]] [[QUBO]] [[Ising Hamiltonian]]






# 1. Define Hamiltonian H:
   the toy problem we’ll take is this: 
 alice, bob, charlie and debbie need to come to a party. alice likes debbie and bob, but not charlie, and charlie likes debbie and alice, but not bob. bob and debbie like everyone. and the party must have at least 2 people and at most 3 people. maximize happiness
  
  
  Main function: $$H(x_{i})=x_{a}(x_{b}+x_{d}-x_{c})+x_{b}(x_{c}+x_{d}+x_{a})+x_{c}(x_{a}+x_{d}-x_{b})+x_{d}(x_{b}+x_{a}+x_{c})$$
  and penalty function: $$P(S)=P_{0}(S-2)(S-3)$$ for $S=x_{a}+x_{b}+x_{c}+x_{d}$
  so the total cost function: $$f(x_{1},x_{2},x_{3},x_{4})=P(S)-H(x_{i})$$
solving gives the function:$$f(x_{i})=\left(\begin{bmatrix}x_{1}&x_{2}&x_{3}&x_{4}\end{bmatrix}\cdot Q \cdot\begin{bmatrix}x_{1}\\x_{2}\\x_{3}\\x_{4}\end{bmatrix}\right)+600$$ for P = 100 where: $$Q=\begin{bmatrix}-400&198&200&198\\0&-400&200&198\\0&0&-400&198\\0&0&0&-400\end{bmatrix}$$
this is the [[QUBO]] to solve. we’ll now convert it into an [[Ising Hamiltonian]], so first into spin [[Hamiltonian]]
this is simply: $$\hat{S}=\sum_{i}h_{i}s_{i}+\sum_{i<j}j_{ij}s_{i}s_{j}$$where
$j_{ij}$ = $\frac{1}{4} Q_{ij}$ and $h_{i}=\frac{1}{2} Q_{ii}+\frac{1}{4} \sum_{i≠j} Q_{ij}$

this will get computed. then we will convert into a [[Hamiltonian]] by converting spin qubits to the Pauli Z [[Quantum Gates|Gate]], which has eigenvalues as $s_i$ : $$\hat{H}=\sum_{i}h_{i}\sigma_{i}^Z+\sum_{i<j}j_{ij}\sigma_{i}^Z\sigma_{j}^Z$$
this is our hamiltonian. step 1 is done.



# 2. Define a local Pauli basis on your domain D:
   - because there are only Pauli Z [[Quantum Gates|gate]] the global basis is all combinations of $\mathbb{I} \otimes Z$ in with $2^4$ terms and per qubit, the the local basis is just {I , Z} since they are the only ones acting, we can expand this with tensor products from the global basis. 
   
# 3. Keep the current state as a vector $\phi$   
- the initial state needs at least some overlap with the ground state. usually, $\ket{0000}$ is a good starting point. but a safer one is Hadamard for at least one state towards the ground state.
- $$\ket{\phi_{0}}= H^{\otimes_{4}}\ket{0000} = \frac{1}{4}\sum_{x=\{0,1\}^4} \ket{x} $$


# 4. Compute S
- S is, $$S_{ij}^m=\bra{\phi_{m-1}}\cdot\sigma_{I}\sigma_{J} \cdot \ket{\phi_{m-1}}$$



# 5. Compute b
- b is, $$b_{I}=i\bra{\Delta H}\sigma_{I}\ket{\phi_{m-1}} -i \bra{\phi_{m-1}}\sigma_{I}\ket{\Delta H}$$ which when expanded with $\ket{\Delta H}$
gives you $$b_{I}=\frac{i}{c\Delta \tau}\bra{\phi_{m-1}}e^{-\Delta \tau H} \sigma_{I}-\sigma_{I} e^{-\Delta \tau H}\ket{\phi_{m-1}}  $$

# 6. Solve for `a`.
- you have $$\left(S+S^T\right)a=-b$$


# 7. Build $A_{m}$
- the local [[generators|generator]] $A_m$ is defined as: $$A_{m}=\sum_{I}a_{I}\sigma_{I}$$ where $\sigma_{I}$ is the local Pauli basis
  


# 8. Apply $e^{-iA_m \Delta\tau}$ to update $\phi$
self explanatory.
  
  $$\ket{\phi_{m}}=\frac{e^{-iA_m \Delta\tau}\ket{\phi_{m-1}}}{||e^{-iA_m \Delta\tau}\ket{\phi_{m-1}}||}$$
  
  
  
  
 now
 the code, should be interesting.
 we can probably put all the math down, then solve whatever with black box operations. 
 what we need to solve in a list:
 - Ising parameters, 
 - Sij 
 - bi
 - ai
 - Am
 - phi_m 
 then looped.
 S will be solved with standard  least‑squares / pseudoinverse thingy or whatever. 
 
 
 
 on doing the above, i find that global basis is not enough for getting the correct answer, so exanded to full basis, and it works


