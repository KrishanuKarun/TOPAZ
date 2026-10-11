![[Understanding QITE and varQITE.pdf]]


- lets start with expression (1):
	- it says that the chosen energy eigenstate should not be orthogonal to the groundstate.
- expression (2):
	- basically the says that the state needs to be normalized and the denominator is the normalization factor.
- expression (3):
	- its basically saying that the imaginary time evolution state applied to the initial state is approximately equal to real time evolution with the operator applied to the ground state.
	- $\frac{1}{c}$ is the renormalization constant
- expression (4):
	- its basically saying that to find the next state approximation, we would evolve the previous state with a real time approximation of the imaginary time evolution on that state.
- expression (5):
	- and its just saying that the operator used in the real time evolution is just represented as the Pauli [[Basis]]
- expression (6-7):
	- this basically just talks about how you would define the difference between a state and its successor, where U is the difference in unitary evolution, and H is the difference in imaginary time evolution. $$(\bra{\Delta U}-\bra{\Delta H})(\ket{\Delta U}-\ket{\Delta H})$$
	- this basically finds the difference between the two states and sees how much they have similar components, whether they are orthogonal or not
	- then they show that $\ket{\Delta U}$ is the average of $\ket{\phi_{m}}$ and  $\ket{\phi_{m-1}}$ with respect to time. $$\ket{\phi_{m}}-\ket{\phi_{m-1}} = \left(e^{-iA_{m}\Delta\tau}-\mathbb{I}\right)\ket{\phi_{m}-1}$$
	  then to linearize (turn function from wonky to a linear polynomial approximation)$$e^{-iAx}\approx \mathbb{I}-iAx+ \dots$$ so 
	  $$e^{-iAx}-\mathbb{I}\approx -iAx$$, knowing this, you get $$\ket{\phi_{m}}-\ket{\phi_{m-1}}=-iA_{m}\Delta \tau \ket{\phi_{m-1}}$$
	  to turn into average change with respect to time $\Delta U$, divide by Δτ,$$\frac{\ket{\phi_{m}}-\ket{\phi_{m-1}}}{\Delta \tau}=-iA_{m}\ket{\phi_{m-1}}$$   
	$$\ket{\Delta U}=-iA_{m}\ket{\phi_{m-1}}$$
	- now the cost function is $$(\bra{\Delta U}-\bra{\Delta H})(\ket{\Delta U}-\ket{\Delta H})$$ 