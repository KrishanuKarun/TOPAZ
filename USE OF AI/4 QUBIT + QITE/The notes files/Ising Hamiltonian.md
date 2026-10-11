basically, the [[QUBO]] converts into a [[Hamiltonian]].

so you start with some spins, $s_i$ they have two states, 
{-1, 1} or $s_{i}\in\{-1,1\}$ 
so the [[QUBO]] translates to this $$\hat{H}(s)=\sum_{i}h_{i}s_{i}+\sum_{i<j} j_{ij}s_{i}s_{j}$$ by the relation between spin and bits as $$x_{i}=\frac{s_{i}+1}{2}$$ with h being the field around the individual spins, how much the energy wants spin up vs spin down
 and j being the coupling spin fields, how much the energy wants each spin to align or antialign

- to bring this [[Ising Hamiltonian]] to [[QC]], the spin system is converted into pauli matrices with [[eigenvalue]]s being the spin value, and [[eigenstate]]s being 0 and 1. they are equivalent, just now operable. that is the pauli Z gate


so you get $$\hat{H}=\sum_{i}h_{i}Z_{i}+\sum_{i<j}j_{ij}Z_{i}Z_{j}$$
and here $J_{ij}$ = $\frac{1}{4} Q_{ij}$ and $h_{i}=\frac{1}{2} Q_{ii}+\frac{1}{4} \sum_{i≠j} Q_{ij}$
