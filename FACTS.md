# This file contains and summarizes all the final numbers and results of the TOPAZ research project
---
### Simulation
8 qubits (FakeFez)

### Density-matrix fidelity: 
0.737 ± 0.066 (10 seeds)
Best seed: 0.9085
Exact-preparation reference, same 2Q budget: 0.924 ± 0.003
### VQE — final energies (mHa)
H₂, LPTE, noisy: 71.96 ± 16.8
H₂, LPTE, noiseless: 26.72 ± 14.5
H₂, LPTE + ZNE + CDR: 26.16 ± 14.8
H₄, LPTE, noisy: 235.15 ± 77.4
H₄, LPTE, noiseless: 83.82 ± 74.5
H₄, LPTE + ZNE + CDR: 83.75 ± 74.4
### Hardware — ibm_fez (156-qubit Heron r2)
8-qubit target-echo: 28.83% ± 3.94% (2.9× matched-budget baseline)
16-qubit target-echo: 0.65%
16-qubit simulated return-probability improvement: 383×
### Structure
Noise-model transfer: 6 models, η = 0.9943
Seed-distinct suppression sets: 49/50 (ρ < 0.05)
Active Pauli terms: 6–14 of 21 (mean 9.2)
Hessian effective rank at converged point: 3.12 (42 parameters)
Timing attractor: τ = π/2 (SWAP fixed point)
DLA generators: 3(N−1); closure computed exactly to N = 8
Scaling
Gradient-variance slope vs N: −1.55
Lie-closure dimension: 4^(N−1) − 1
### Depth
Compiled 2Q gates: 19 (per-pair circuit)
Noiseless one-way fidelity: 0.5662
### Improvement factors
2.9× — vs. MMA-optimized matched-budget baseline
6–7× — vs. untuned/random initialization
