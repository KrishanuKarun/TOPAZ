# Why:
The file aims to cleanly state the boundaries and use of AI for a two main reasons: 
- to prevent or clear any suspicions about the role of AI during the making of the project
- to prevent me taking credit for aspects about the project that honestly are not mine, WHILE at the same time preventing AI/ LLMs taking credit for work that is honestly mine.
---


# What:
I used multiple models of AI/ LLMs throughout the whole journey of TOPAZ.

---
# Where:
I used AI in three primary directions:
1) _Learning concepts_ (through research papers, 3Blue1Brown and MIT OpenCourseWare as resources): 
   - I needed to get a lot of skills and concepts that weren’t expected of me. I used AI to test my knowledge, to teach me new concepts that were hard to grasp myself, and to clarify doubts. This happened majorly till around may of 2025, following which, I used it here and there when I came across a problem.
   - I also needed to learn some concepts that weren’t involved in quantum computing conventionally (specifically topology optimization and the Method of Moving Asymptotes)
2) _Idea formulation and formalization_: 
   Ideas started in my Obsidian vault, in my words, always before any discussion. Then, roughly weekly, I'd put what I'd already formed in front of an AI mostly to ask: whether this already exist? what is the surrounding literature? am I about to walk into a dead-end someone with more knowledge would see immediately? Is there other research that already solves this problem i.e. is the problem standard in the field or industry?
   The role of AI was a faster search engine, and the direction — topology optimization for circuit-design — was purely mine. Not more, nor less.
3) _Coding and framework implementation_:
   I used AI quite heavily in coding. **However I would like to explicitly state that** I did not “vibe-code” the framework in the general sense. I first recorded my idea completely in math terms, and then translate it as close as possible through AI. I tried to ensure I understood as much as I could when I made a file through AI, and this method proved to keep me as accountable as I could. However it also meant that in some places, the code isn’t as clean or as efficient as conventional or preferred. I would like to say this cleanly and openly.
   
   3.1) _PROOF:_ 
   
   Readers will find a 4 Qubit QUBO + QITE side project with the math.md file and then the code file for proof. Readers should be able to see parallelisms between the files.   
   They will also see: first the original handwritten notes then the MD files for the second last version of the background theory governing the paper (still has problems, but the point for these files specifically isn't for the correctness of the notes, it is for proof that I did the work myself)



4) _parallel checking and sanity testing_: 
   Used different models to test and check integrity of math and code files. (the different models were to prevent any output distortion due to common AI problems, eg. hallucinations and biasness/ sycophancy towards users)
   HOWEVER, it wasn't taken for word. for any and all AI-flagged issues, I tried to verify against the actual runs, the hardware data, and my own derivations.
---

# where not: 
I did NOT use AI for the following: 
- the proofs or derivations, those are entirely mine.
- writing any content of the paper
- generating or adjusting any reported number


# Peer review/ Validation:
One of the most important interactions with peers/ mentors is the three researchers who went through my first version of the 8-Q preservation test line by line, found the flaw I couldn't see, and forced the rebuild. 
They know exactly what is mine, because they attacked it and it cause the overhaul of the entire prioject. 