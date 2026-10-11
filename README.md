# TOPAZ
Canonical scripts and reproducible workflows for the TOPAZ research project.

### Noise-aware quantum circuit design through continuous topology optimization

TOPAZ is the research repository for **TOPAZ**, a framework that explores topology optimization as a way to design quantum circuits. It contains the final manuscript, standalone experiment scripts, the project's revision history, and documentation of how AI was used during the work.

Instead of treating circuit structure as entirely fixed, TOPAZ introduces continuous intensity and timing variables for candidate entangling terms. Relaxed blocks are mapped back to unitary operators through **polar projection**, and a dual **Method of Moving Asymptotes (MMA)** optimizer searches the resulting landscape. The experiments here instantiate the framework using **Local Parametric Trotter Expressions (LPTE)** on nearest-neighbour chains.

**This is an exploratory research codebase, not a packaged quantum-computing library.** Its central contribution is the relaxed design framework and the structure of its optimization landscape, not a claim of universal benchmark superiority.

## Start here

- **Read the paper:** [Final manuscript (PDF)](FINAL%20PAPER/Final_paper_1.pdf) · [LaTeX source](FINAL%20PAPER/Final_paper_1.tex)
- **Run experiments (in case needed):** [Final Codes](Final%20Codes/)
- **Understand the revisions:** [Project history](All%20versions%20with%20changes/HISTORY.md)
- **Browse reported numbers:** [FACTS.md](FACTS.md), a compact summary. Use the final paper for definitions, qualifications, and any differences between summaries.
- **Read the AI-use disclosure:** [USE OF AI.md](USE%20OF%20AI/USE%20OF%20AI.md)

## Research scope and reported results

The final paper is titled **“Exploring Topology Optimization as a Framework for Noise-Aware Quantum Circuits through Geometric Wells in the Parameter Landscape.”**

Selected results reported in the manuscript:

| Setting | Reported result | How to read it |
| --- | --- | --- |
| 8-qubit FakeFez simulation | LPTE density-matrix fidelity: **0.737 ± 0.066** over 10 seeds | Exact preparation under the same noise and 2Q gate budget reaches **0.924 ± 0.003**. LPTE does not outperform that reference. |
| Noise-model transfer | Structural-well transfer across **6 noise models**, with **η = 0.9943** | Evidence for the tested models, not a general guarantee for arbitrary device noise. |
| 8-qubit live IBM hardware | Target-echo: **28.83% ± 3.94%**, approximately **2.9×** the optimized matched-budget product baseline | A single-path demonstration on `ibm_fez`. The advantage is representational, not a demonstrated improvement in noise retention. |
| 16-qubit live IBM hardware | Unmitigated target-echo: **0.65%** | The separately reported **383×** gain is in simulated return probability, not hardware fidelity. |

Important boundaries:

- **TOPAZ is the framework; LPTE is the ansatz used here.** HEA denotes a hardware-efficient ansatz, HVA a Hamiltonian variational ansatz, and PPTE the product-PTE baseline.
- **Term-level suppression is not edge deletion.** At the paper's operating threshold, `τ_κ = 0.05`, all seven edges of the 8-qubit chain survive. The identity-anchored block needed for principled edge removal is specified but not implemented in this study.
- **LPTE does not beat HEA on matched-budget VQE energies.** The narrower reported advantage is compatibility with error-mitigation post-processing.
- **Target-echo, density-matrix fidelity, and noiseless one-way fidelity are different observables.** Do not compare them as interchangeable scores. A self-echo of `U†U` is not a target-representation test.
- The timing cluster near `π/2` is associated with a **SWAP fixed point**, not a maximally entangling gate.

See the final manuscript for protocols, uncertainty conventions, comparisons, and limitations.

## Repository structure

```text
TOPAZ-V2/
├── FINAL PAPER/
│   ├── Final_paper_1.pdf                 # Final manuscript
│   └── Final_paper_1.tex                 # Manuscript source
├── Final Codes/                         # 10 standalone experiment drivers
│   ├── fez_preservation_test.py          # 8-qubit simulation / hardware
│   ├── fez_preservation_test_16q.py      # 16-qubit simulation / hardware
│   ├── run_hea_vqe.py                    # H₂ HEA baseline
│   ├── run_hva_vqe_standalone.py         # H₂ HVA baseline
│   ├── run_lpte_vqe_standalone.py        # H₂ LPTE-TOPAZ
│   ├── run_H4_HEA_vqe.py                 # H₄ HEA baseline
│   ├── run_H4_HVA_vqe.py                 # H₄ HVA baseline
│   ├── run_H4_LPTE_VQE.py                # H₄ LPTE-TOPAZ
│   ├── run_h4_to_tfim_transfer.py        # H₄ → TFIM transfer experiment
│   └── tau_kappa_sweep_selfcontained.py  # Edge-density threshold sweep
├── All versions with changes/
│   ├── HISTORY.md                       # Development arc and corrections
│   └── Versions/                        # 17 PDFs, including the final paper
├── USE OF AI/
│   ├── USE OF AI.md                      # Scope of AI assistance
│   ├── 4 QUBIT + QITE/                   # Separate QUBO/QITE learning project
│   ├── Handwritten Notes/               # Original handwritten notes
│   └── Obsidian Notes/                  # Earlier theory notes
├── FACTS.md                             # Compact reported-results summary
├── LICENSE                              # Apache License 2.0
└── README.md
```

## Setup

Use a Python 3 virtual environment. The experiment scripts import NumPy, SciPy, NetworkX, Qiskit, Qiskit Aer, and Qiskit IBM Runtime. Molecular VQE and H₄ → TFIM runs additionally require Qiskit Nature and PySCF.

```bash
git clone https://github.com/KrishanuKarun/TOPAZ-V2.git
cd TOPAZ-V2

python3 -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install numpy scipy networkx qiskit qiskit-aer qiskit-ibm-runtime

# Required for the molecular VQE and H₄ → TFIM scripts:
python -m pip install qiskit-nature pyscf

cd "Final Codes"
```

**Environment status:** this repository does not currently include a dependency lockfile or tested package-version matrix. The install commands list dependencies inferred from the source; in particular, FakeFez and IBM Runtime API compatibility depends on the installed Qiskit versions.

## Run a reduced simulation

All commands below assume you are in `Final Codes/`. These are reduced-run examples for checking setup, not commands that reproduce the paper's ensembles.

```bash
# 8-qubit per-pair LPTE simulation. No IBM credentials needed.
python fez_preservation_test.py --mode per_pair --seeds 1 --iters 1 --no-zne

# Inspect available controls and mitigation options.
python fez_preservation_test.py --help

# Test one edge-density threshold on one seed.
python tau_kappa_sweep_selfcontained.py --seeds 0 --iters 1 --thresholds 0.05
```

The Fez preservation scripts run **simulation by default**. The `--lpte` flag selects the live-hardware pipeline; it is not required to select per-pair LPTE in simulation.

The 16-qubit driver is `fez_preservation_test_16q.py`. Larger density-matrix simulations can be expensive in both memory and runtime; start with the 8-qubit driver rather than assuming the 16-qubit default is a lightweight test.

## VQE experiments

The molecular Hamiltonians and Hartree–Fock inputs are generated internally. H₂ uses 4 qubits; H₄ uses 8 qubits. The drivers are separate scripts rather than subcommands of a shared application.

```bash
# H₂: reduced LPTE, HEA, and HVA runs
python run_lpte_vqe_standalone.py --seeds 1 --n-outer 1
python run_hea_vqe.py --seeds 1 --n-iters 5
python run_hva_vqe_standalone.py --seeds 1 --n-iters 5

# H₄: reduced LPTE, HEA, and HVA runs
python run_H4_LPTE_VQE.py --seeds 1 --n-outer 1
python run_H4_HEA_vqe.py --seeds 1 --n-iters 5
python run_H4_HVA_vqe.py --seeds 1 --n-iters 5
```

The LPTE drivers default to **10 seeds and 35 outer iterations**. HEA/HVA drivers default to **3 seeds and 500 iterations**, with script-specific depths. These defaults do **not** establish a matched optimization budget. Use the paper's protocol when constructing scientific comparisons.

For the cross-Hamiltonian study, use `run_h4_to_tfim_transfer.py`. It first optimizes an H₄ layout, then compares transferred and fresh optimization on the transverse-field Ising model (TFIM). Run `python run_h4_to_tfim_transfer.py --help` after installing the chemistry dependencies. There is no TFIM-only CLI switch in this driver.

## Live IBM Quantum experiments

Hardware runs require an IBM Quantum account with access to the requested backend. The drivers can use a saved Qiskit Runtime account or credentials supplied through `IBM_QUANTUM_TOKEN` / `IBMQ_TOKEN`. Keep credentials outside the repository and avoid putting tokens directly in command history.

```bash
# Submits real device jobs. Requires configured credentials and backend access.
python fez_preservation_test.py --lpte --backend ibm_fez
```

Backend availability, calibration, queues, and account limits can differ from those at the time of the paper. Running this command is not expected to reproduce the published hardware mean by itself.

To rerun only ZNE, the drivers support `--zne-only --params <saved-result.json>`. The JSON must contain `opt_params` from a matching 8- or 16-qubit run. Check each driver's `--help` before submitting jobs.

## Outputs and reproducibility

- **Preservation experiments:** timestamped JSON files under `results/` by default; override with `--output`.
- **Threshold sweep:** timestamped `tau_kappa_sweep_*.json` files under `results/`; override with `--output-dir`.
- **H₂ / H₄ VQE:** per-seed and combined `.npz` files under `results_h2_vqe/` or `results_h4_vqe/`; override with `--output`.
- **H₄ → TFIM:** `2A_seed_XX.npz` and `2B_seed_XX.npz` under `results_h4_tfim_transfer/` by default.

Output directories are relative to the current working directory. VQE text logs are written beside their scripts and replaced on subsequent runs; copy old logs before rerunning if you need to retain them. Fixed-name VQE result files can also be overwritten, so use distinct output directories for separate experiments.

For a reproducible run, retain the exact repository commit, command line, random seeds, package versions, and output files. For hardware, also retain backend, calibration context, and job identifiers where available.

**Current repository limitations:**

- No pinned dependency environment, automated test suite, or bundled raw-result dataset is present in this tree.
- The LaTeX source references `figures/*.png` files that are not included here. Use the committed PDF to read the paper; compiling the source requires those figure assets.
- The manuscript references a [Zenodo archive](https://doi.org/10.5281/zenodo.19214449) for supporting material. That archive is separate from the contents of this repository.
- Script defaults and reduced examples are not substitutes for the full experimental protocols in the manuscript.

## Development history and AI transparency

[HISTORY.md](All%20versions%20with%20changes/HISTORY.md) records the project's progression from early PTE/continuous-circuit ideas to the final TOPAZ formulation, including failed evaluations, corrected claims, and remaining work. The archived manuscripts preserve that development record; they should not be treated as equally current scientific references.

[The AI-use disclosure](USE%20OF%20AI/USE%20OF%20AI.md) describes assistance with learning, literature checks, implementation, and sanity testing, and distinguishes those uses from the author's stated responsibility for ideas, derivations, manuscript writing, and reported numbers.

The handwritten and Obsidian notes document provenance and intermediate reasoning. They are **not authoritative statements of the final theory** and may contain errors corrected later. The [4-qubit QUBO/QITE project](USE%20OF%20AI/4%20QUBIT%20%2B%20QITE/) is a separate learning and implementation example, not a TOPAZ benchmark.

## Feedback and citation

Questions, bug reports, and reproducibility feedback are welcome through [GitHub Issues](https://github.com/KrishanuKarun/TOPAZ-V2/issues). Include the script, commit, command, package versions, and relevant non-sensitive output. Never include API tokens.

If you use this work, cite the manuscript and identify the repository commit used:

> Krishanu Karun (2026). *Exploring Topology Optimization as a Framework for Noise-Aware Quantum Circuits through Geometric Wells in the Parameter Landscape.* TOPAZ-V2 research repository. https://github.com/KrishanuKarun/TOPAZ-V2

## License

This repository is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) for the terms.
