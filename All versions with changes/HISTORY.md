# HISTORY AND THE COMPLETE ARC OF TOPAZ


**The Final Paper** [`Versions/Final_paper_1.pdf`](Versions/Final_paper_1.pdf)

(Version submitted to QIP). The master version it was cut from is
`Versions/NPJ_Final_FINAL_5.pdf`.

  
**How to read it:** Each entry below says: *what it was* → *what was wrong* → *what we did about it*. Fixes are tagged so you can tell what is actually done versus still open:

---
## the very beginning: (includes PTE:UPTE, Continuous Interpretation of Quantum Circuits)

### 1. `Parametric Trotterized Expression`/`PTE:UPTE` 
- **What it was:** Deriving the *Parametric Trotter Expression* (PTE) and its unitary form (U-PTE). It started with how we could implement Topology Optimization that usually applied to a single body that is meshed onto multiple discrete quantum gates. Took inspiration from parametrization and PQCs (parametrized quantum circuits) 

- **What was wrong:** Textbook ingredients (weighted sums, polar projection) were presented as if original. No numerical results, no circuit-cost comparison, no implementation.

- **What we fixed:** This became background material, **not** a standalone paper.

- **Finally:** kept as a starting idea finally, or a short concept we’d come back to
  

### 2. `A Continuous Topological Interpretation of Quantum Circuits (CTI)` 

- **What it was:** A geometric way of thinking: circuits as continuous shapes, entanglement as "more room" in the landscape, noise as a deformation of that shape. basically studied VQE and QAOA, and saw essences of what I wanted to formally establish as a single unified interpretation of quantum circuits.

- **What was wrong:** No rigorous new result, no experiment, very little engagement with existing literature. Big claims (entanglement, smoothing) were asserted, not shown.

- **What we fixed:** Nothing at this stage — later drafts demoted CTI to background and stopped trying to prove all its original claims. It is now for future work.

- **Net:** kept as framing, not headlining.

---

  

## TOPAZ

  

### 3. `TOPAZ — Noise Resilience Framework`

- **What it was:** Combined PTE/UPTE and MMA. Named **TOPAZ** (Topology OPtimization Ansatz with Zoning). First 2–8 qubit numerical runs. Three custom noise channels; made for correlation noises.

- **What was wrong:** No standard baselines to compare against. The two showcased runs ended at 0.371 vs 0.838 — inconsistent story. No seed distribution. Simulated virtual distillation was called experimental. Speculative and unvalidated 50–500 qubit claims. Unvalidated correlated-noise handling, a large timing step, inconsistent improvement numbers, and no reproducible code. **AND LATER, I FIND OUT THAT THE NUMBER MEASURED ON THE REAL COMPUTER (1071% improvement) WAS FAKE DUE TO THE NATURE OF HOW THE LOSS FUNCTION WAS CONSTRUCTED**

- **What we fixed:** added baselines, seeds, and real device data; dropped the speculative scale claims.

- **Net:** First application of the idea, but not yet trustworthy. and the biggest problem that was integral and the most critical number to the entire project even though it was fake, the 10x improvement number on fidelity.

  

### 4. `TOPAZ_V2`

- **What it was:** Extended TOPAZ to a calibrated noise model (**FakeFez**) and a live IBM device (**ibm_fez**, 156-qubit Heron r2). Added the dual-MMA optimizer that separates intensity from timing.

- **What was wrong:** The LiH energy result was off (30.78 vs 27.20 mHa). Duplicate rows (10-/12-qubit), wrong active-space reference. Literature-estimated CDR/VD numbers were shown next to real measurements. The "single well floor" claim was contradicted by the 0.371/0.838 runs. A density-matrix complexity claim (`O(2^N)`) was simply wrong. There was a gap between the optimizer's projected operator and the circuit actually executed.

- **What we fixed:** FakeFez ←→ hardware reuse was kept as a *reported* same-device transfer, not a general one.

- **Net:** Real hardware content arrives; many loose ends open.

  

---

  

## Mega Manuscripts

These merged CTI + PTE + TOPAZ into one paper and grew steadily. Many problems survived several versions because they were patched in rather than re-run.
aimed to support the weak spots of having three different independent papers by consolidating into a single paper to present as a single narrative.

  

### 5. `Mega_Manuscript_1`

- **What it was:** First merge of the three threads into a single paper.

- **What was wrong:** The merge weakened it: duplicated weak CTI/PTE material, contradictory statements, figure placeholders. All the v2 number problems remained.

- **What we fixed:** Treated as a structure problem — later versions cut duplication and fixed positioning.

- **Net:** good step forward, but still a long way to go.

  

### 6. `Mega_Manuscript_2`

- **What it was:** Added **LPTE** (local PTE), HEA/optimizer ablations, 10-seed statistics, Hamiltonian analysis, H₂ VQE, path-matched hardware, and mitigation stacking. Admitted global PTE failed and separated the inversion test from direct fidelity.

- **What was wrong:** LiH contradictions remained. H₂ numbers shifted (70.6 vs 143.35 mHa). Product fidelities 0.6416/0.6329/0.739 inconsistent. "200 vs 40 iterations" language. Unmeasured LiH CDR/VD. Placeholders. 

- **What we fixed:** Continued in later versions; LiH later removed entirely in place for a more controlled 8 qubit system as H4.

- **Net:** Added LPTE, but made a bunch of stuff worse

  

### 7. `Mega_Manuscript_3`

- **What it was:** Added a Bonferroni ablation, five-seed sparsification, six-model transfer, and an honest VQE failure distribution.

- **What was wrong:** Abstract called polar projection unimportant even though the ablation found it important. Best result 0.9085 was called "conservative" even though a ten-seed mean of 0.737±0.066. η=0.9943 was over-read. H₂ was much worse than HEA. Budgets were unequal. Old LiH issues persisted.

- **What we fixed:** Polar projection is now treated as vital; best-seed vs mean separated.

- **Net:** More data, but not consistent or clean
  

### 8. `Mega_Manuscript_4` / `Mega_4.5` / `Mega_5.0`

- **What it was:** Condensed PTE to a family/ ansatz subclass story. Fixed the abstract/polar contradiction. Removed a conflicting H₂ baseline and a misleading MMA-vs-Adam headline. 5.0 was the same science with broken citations that were repaired.

- **What was wrong:** LiH CDR/VD estimates lost their disclosure. LiH duplicates, floor ambiguity, complexity claims, transfer over-reading, best-seed framing, unequal budgets, and missing figures all remained. The 4.5→5.0 chain showed two PDFs with identical science.

- **What we fixed:** Condensation helped presentation but the underlying issues were the same

- **Net:** Cleaner paper, same open problems

  

### 9. `Mega_Manuscript_6.0` / `6.1`

- **What it was:** 6.0 the unreliable LiH table and its CDR/VD claims, added H₂/H₄ VQE, H₄ → TFIM hamiltonian negative transfer, and hardware Loschmidt echo.

- **What was wrong:** H₂ changed between versions without a stated protocol change. The "floor" ambiguity persisted. η uncertainty and optimizer mismatch. Unsupported 100–200 qubit extrapolation. The echo "square-law ceiling" entered here and is questionable. 6.1 fell in quality by deleting the Hessian/sparse-well analysis while keeping the "structural well" headline.

- **What we fixed:** The Hessian/well section was later restored and i worked on fixing and researching on the discrepencies

- **Net:** Improved by fixing the vqe targets/ objectives, but still a bad experience to read and get the real numbers and stuff.

  

### 10. `Mega_Manuscript_7`

- **What it was:** Added the π/2 → SWAP calculation, DLA framing, and a simulator ↔ circuit equivalence bound. Clarified the one-way value was simulated.

- **What was wrong:** The theorem block used a depolarizing result to explain a "noise-induced well" — logically incompatible without extra conditions. Non-unital extension unjustified. BUT: the correct SWAP calculation was described as "maximally entangling" (btw it is not)

- **What we fixed:** Much later "maximally entangling" removed and reworded, worked on the results and framing and understanding how to frame it all correct.

- **Net:** New math, new mistakes. tried correcting in the future versions.

  

### 11. `Mega_Manuscript_8` / `9` / `10`

- **What it was:** 8 scoped the unital/ non-unital framing and stories and restored the Hessian section 9. rewrote as a single TOPAZ article with a direct tone and better-scoped propositions. 10 gave the first explicit pure-state `O(2^N)` vs dense-density-matrix `O(2^(2N))` correction.

- **What was wrong:** Non-unital suppression was assumed, not shown. The Fréchet lemma was too broad. Figure/complexity/seed issues remained. 9 had the wrong dense-DM` O(2^N) `complexity (didn’t remove that stuff cleanly, or even at all in the 9th version specifically). The theory did not actually establish real-device noise invariance.

- **What we fixed:** The density-matrix complexity was corrected in 10.

- **Net:** Complexity fixed but the other claims still conditiona and stuff

  

---

  

## Journal Specific versions

- THE GOAL was that I wanted to submit to NPJ QI or PRX Quantum. But those journals were really hard and I had a lot of small problems here and there, either in framing or in presentation, in format, and more in general. (These would have gotten me desk rejected)



### 12. `NPJ_Draft_1` / `2` 

- **What it was:** First journal-format drafts. Introduced the Loschmidt/two-way echo, FakeFez, and the "geometric wells" story.

- **What was wrong:** The radial/polar lemma was overbroad. The two-way echo 0.1727±0.0060 was incompatible with the raw shot count. "21 terms → 8 native gates" was unexplained. Best seed vs mean not separated. SIMP attribution imprecise. Repo metadata missing. Eq. (1) also showed the start of a normalization/pruning inconsistency (this becomes important later)

- **What we fixed:** Later drafts widened the framing of the lemma honestly (or at least tried to), fixed the raw-echo error bars, and explained the gate counting.

- **Net:** followed the format of the journal, but too many opportunities to get desk rejected. 

  

### 13. `NPJ_Draft_3` 

- **What it was:** shorter ten-page rewrite. Narrows the polar lemma to radial scaling, corrects raw echo SEM to ±0.0085 (z≈17.7), explains gate counting, labels 0.9085 as a best seed vs the 0.737±0.066 mean, says SIMP-inspired instead of saying it IS SIMP (solid isotropic material with penalization) intead.

- **What was wrong:** The stated softmax normalization made the stated pruning rule impossible, which was quite a shocking and negative finding for THIS specific framing (this also becomes important later)
- Polar projection made edge-intensity scaling invisible to the circuit.
- SWAP was still called "maximally entangling."
- Positive weights do not guarantee an invertible block (a counterexample exists).
- The two "exact preparation" baselines conflict (0.924/21 vs 0.8501/42).
- The 0.3315 echo "ceiling" was not established.
- **What we fixed:** Draft 3 corrected several (lemma scope, echo SEM, gate counting, labels) but gave back 6 problems, and became the target items to fix for papers that were Final_4 onward.

- **Net:** 4 steps forward, 6 back. net negative, but direction was right. (net 4 - 6 (+2 for trying))

  

---

  

## REVISIONS

  

This is where the real item fixing happened, driven by purely getting the paper done for submitting and not for new data or science. 

_(Note: `Final_7` was byte-identical to `Final_6`; the effective rounds are `Final_8 → Final_12`.)_

  

### BIG FIX

- **Problem (Round 3):** The headline used a *self-echo* test, which measures `U†U = I` for **any** `U` — so it says nothing about how well the circuit represents the target. The headline was "a circuit that represents the target at ~58% achieves a noise-robust round trip."

- **Fix :** Switched to the target-echo (inversion) test, measuring `|⟨ψ₀|U_target†·U_circ|ψ₀⟩|²`. Added an MMA-optimized product-Trotter control (0.1008) so topology is isolated from optimization. 
  

### Hard times with honest framing

- **Problem (Round 4):** The paper's own Table VII showed TOPAZ was the **least** noise-robust per unit of representation: retention 50.9% (TOPAZ) vs 57.0% (opt.) vs 63.1% (untuned). So the raw-echo improvement was representational, not a noise-resilience gain.

- **Fix:** The retention fractions are now stated explicitly, and the abstract/conclusion

say the hardware advantage is representational; resilience is scoped to simulation. The

title changed accordingly ("**Noise-Aware**", not "noise-resilient").

  

### `Final_8` → `Final_12` 

- **Final_8:** Abstract now leads with the counterintuitive depth-vs-representation result. Fixed ρ/σ notation. Added the SWAP-cluster paragraph. Added a prior-art/novelty table.

- **Final_9 (the P0 fix):** Added real **scaling measurements** — gradient-variance slopes vs N (LPTE −1.55, product −2.29, HEA −1.96) and exact Lie-closure dimensions (`4^(N−1)−1`). Reported as measurements

- **Final_10:** Added **matched-budget** methodology; the equal-budget H4 re-run *reversed* the apparent ranking, narrowing the claim to mitigation-compatibility.

- **Final_11:** Reverted (a theory-first variant); content rolled into Final_12.

- **Final_12:** Theory-first abstract; Observation→Lemma with proof; removed the missing table reference; reconciled the threshold language; corrected the global-polar `O(2^(3N))`.
 
---

## Final cleanups and the venue versions


### 14. `NPJ_Final_FINAL_1` → `_5`

- **What it was:** The last few npj-targeted revisions.
- This is one of the most important reframes. I started the project with an idea in my mind, and the research was supposed to be me exploring by seeing how I could connect two distinct fields and whether it looked promising enough. But with results, the objective in my head turned into me trying to beat already established algorithms or frameworks. 
  **These few papers reframed the whole paper to become the version it was originally supposed to.**
- I lost a few claims because of this, but I also gained the protection of only exploring and setting the stepping stones for topology optimization applied to quantum circuits and continuous circuit optimization for the future. 


- **FINAL_1:** Added multi-seed ensembles and an ablation table, plus a Python/artifact appendix.

- **FINAL_5 : Final title "Exploring Topology Optimization as a Framework for Noise-Aware Quantum Circuits through Geometric Wells in the Parameter Landscape."**
- Added the two formal Propositions (removal cost is well-posed; intensities alone cannot satisfy it) and the positivity/bound criterion. This is the audited master.

- **What was still open at _5:** τ_κ sensitivity sweep, per-seed release manifest, and a per-row transpile-level annotation in one table.

  

### 15. `PRX_Final_paper_1` / `NPJ_Final_paper_1` / `QIP_Final_paper_1`

- **What it was:** Three forks of the master, one per venue, each with a venue-specific list. This repository only has the version submitted to QIP, and I’ll commit the other two after I get results of my decisions from the respective venues, submitting in the order NPJ submit → NPJ decision → (if completely rejcted in NPJ) → PRX submit.

- **QIP fork (the final paper):** abstract condensed to lead with the two propositions; proposition-first framing.

- **Net:** Same science, three presentations. **`QIP_Final_paper_1.tex` is the destination.**

  

---

  

## What is still open
  
- The identity-anchored block: proved *necessary*, not implemented.

- Future work on the formal "**Continuous Topological Interpretation of Quantum Circuits**"

- Work on compatibility across different Ansatze, (mostly HEA)

- Work on Algorithmic Compatibility (mostly Grover’s algorithm, QAOA and QUBOs)

  

---

  
## Final Words (not related to the history)
  
This project started in 2025 because I didn't know what a qubit was, and that bothered me. No mentor, no lab, nobody around who could even answer my questions — so I just started, on whatever I could understand that week, and fixed things when they broke. A few times it really felt like the project was done for. It never was. The fix was always the same: stop for a few days, come back, see the thing you couldn't see when you were exhausted.

My favorite mistake: early on, my framework appeared to be beating IBM and Google's published numbers by 10–11×. I believed it for about two weeks. Told my parents. Dreamed about a Nobel Prize, honestly. What had actually happened was dumber than that — I'd written an evaluation that quietly leaked its own targets. The framework was grading itself against answers it already had. Three researchers from a quantum startup went through my code line by line and found it in minutes. It took me a year to put that bug there.

I rebuilt everything so that the framework — and its own scoring — can never see the answer it's being tested against. That bug is the reason this repo exists in its current shape.

The early drafts of this paper thought they were setting the paradigm for quantum computing. The final one is more modest, on purpose: two structural results, and it says plainly where the mechanism doesn't fire yet and what I haven't implemented. It runs 8-qubit benchmarks because that's the scale the theory honestly supports. Smaller claims. All of them defensible. That's the upgrade.

**The final paper is `Versions/Final_paper_1.pdf`.**
