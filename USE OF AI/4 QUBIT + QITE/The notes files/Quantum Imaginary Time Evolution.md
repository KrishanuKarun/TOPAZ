[[Quantum Imaginary Time Evolution|QITE]] basically starts like this:

start with [[time-evolution operator]]: $$\ket{\psi(t)}=U(t)\ket{\psi_{0}}$$
and $$U(t)=e^{-i\hat{H}t}$$
now, take time to behave like a spatial axis. if time scales by -i as in $$t=-i\beta$$$$U(t)=e^{-\beta \hat{H}}$$
so then now, instead of showing how the energy of some [[state]] evolves under some real time, it now shows how the energy of some [[state]] decays with time

so take an example of a energy [[eigenstate]] $\ket{E_{k}}$ with energy $E_{k}$ 
so in real time: $$e^{-i\hat{H}t}\ket{E_{k}}=e^{-iE_{k}t} \ket{E_{k}} $$ this gives you a matrix, it shows where the state E_k goes to after t-time
but in imaginary time, $$e^{-\beta \hat{H}}\ket{E_{k}}=e^{-\beta E_{k}}\ket{E_{k}}  $$
this is all real factors. This is a decay function. the larger the value the faster E_k will drop. 

so now. take a [[quantum system]] $$\ket{\psi}=\sum_{k} c_{k}\ket{E_{k}}  $$ where the [[state]]s are [[eigenstate]] of the [[Hamiltonian]]. and the state should have _some_ component in the direction of the ground state, so that the whole [[quantum system]] can decay to it by some point. 
so $$e^{-\beta \hat{H}}\ket{\psi}=\sum_{k}c_{k}e^{-\beta E_{k}}\ket{E_{k}} $$
as it is linear. so for each energy E_k, it will decay the [[state]] and for higher energy, it will decay faster. 


the only problem with this is the result is [[non-unitary]]

the way we do that is by constructing multiple unitary operators at intervals so that the whole thing is a [[Unitary operator]] that approximates the imaginary time evolution. 

so basically you select the local qubits, D, so then the Pauli [[Basis]] has $4^D$ pauli strings which only act on that domain, from which $$e^{-\tau H}$$ you set new [[operators]] $$A_{m}=\sum_{i}c_{i}\sigma_{i}$$ and $$e^{-i\Delta tA_{m}} \approx e^{-\tau H}$$
the actual thing [[Quantum Imaginary Time Evolution|QITE]] does is that it finds $c_{i}$ for which the real time operators approximate the imaginary time operators. 
