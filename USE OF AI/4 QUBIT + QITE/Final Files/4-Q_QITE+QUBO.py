import numpy as np
from scipy.linalg import expm, eigh

# -------------------------------------------------
# 1. QUBO -> ISING (x = (1 - z)/2)
# -------------------------------------------------
Q = np.array([
    [-400, 198, 200, 198],
    [   0, -400, 200, 198],
    [   0,   0, -400, 198],
    [   0,   0,   0, -400]
], dtype=float)

n   = 4
dim = 2**n
names = ["Alice", "Bob", "Charlie", "Debbie"]

h = np.zeros(n)
for i in range(n):
    row_sum = np.sum(Q[i, i+1:])
    col_sum = np.sum(Q[:i, i])
    h[i] = -Q[i, i]/2 - (row_sum + col_sum)/4

J = np.zeros((n, n))
for i in range(n):
    for j in range(i+1, n):
        J[i, j] = Q[i, j] / 4

# -------------------------------------------------
# 2. HAMILTONIAN H AND LOCAL BASIS
# -------------------------------------------------
I2 = np.eye(2, dtype=complex)
X  = np.array([[0, 1], [1, 0]], dtype=complex)
Y  = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z  = np.array([[1, 0], [0, -1]], dtype=complex)
H1 = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)

def kron_all(ops):
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out

Z_ops = [kron_all([Z if q == i else I2 for q in range(n)]) for i in range(n)]

H_op = np.zeros((dim, dim), dtype=complex)
for i in range(n):
    H_op += h[i] * Z_ops[i]
for i in range(n):
    for j in range(i+1, n):
        H_op += J[i, j] * (Z_ops[i] @ Z_ops[j])

diag_H = np.real(np.diag(H_op))
true_min_idx = np.argmin(diag_H)
print(f"Verified: ground state of H is |{format(true_min_idx, '04b')}>")

# local basis: X, Y, Z on each qubit (3n operators)
basis = []
labels = []
for qubit in range(n):
    for op_label, op in zip(["X", "Y", "Z"], [X, Y, Z]):
        ops = []
        for q in range(n):
            ops.append(op if q == qubit else I2)
        basis.append(kron_all(ops))
        labels.append(f"{op_label}{qubit}")
k = len(basis)
print(f"Using {k} local basis operators:", labels)

# -------------------------------------------------
# 3. INITIAL STATE |+>^⊗4
# -------------------------------------------------
phi = kron_all([H1] * n) @ np.array([1] + [0]*(dim-1), dtype=complex)
phi /= np.linalg.norm(phi)

# -------------------------------------------------
# 4. QITE HELPERS
# -------------------------------------------------
def compute_S(phi, basis):
    S = np.zeros((k, k), dtype=complex)
    for i in range(k):
        psi_i = basis[i] @ phi
        for j in range(i, k):
            val = np.vdot(psi_i, basis[j] @ phi)
            S[i, j] = val
            S[j, i] = np.conj(val)
    return S

def compute_b_exact(phi, H, basis, dt):
    E  = expm(-dt * H)
    E2 = expm(-2 * dt * H)
    c  = np.sqrt(np.vdot(phi, E2 @ phi))

    E_phi = E @ phi
    b = np.zeros(k, dtype=complex)
    for i in range(k):
        sigma = basis[i]
        term  = E @ (sigma @ phi) - sigma @ E_phi
        b[i]  = (1j / (c * dt)) * np.vdot(phi, term)
    return b

def energy(phi, H):
    return np.real(np.vdot(phi, H @ phi))

def solve_a_eig(S, b, eps=1e-8):
    """
    Manual pseudoinverse via eigendecomposition for Hermitian S_sym.
    Avoids lstsq/pinv SVD drama.
    """
    S_sym = S + S.conj().T
    # Hermitian → use eigh
    w, V = eigh(S_sym)
    # build diagonal pseudoinverse with cutoff
    w_inv = np.zeros_like(w, dtype=complex)
    for i, val in enumerate(w):
        if abs(val) > eps:
            w_inv[i] = 1.0 / val
        else:
            w_inv[i] = 0.0
    S_pinv = V @ np.diag(w_inv) @ V.conj().T
    return S_pinv @ (-b)

# -------------------------------------------------
# 5. QITE LOOP
# -------------------------------------------------
dt    = 0.05
steps = 40

print("\nStarting QITE (exact b, eig-based pseudoinverse)...")
print(f"Initial energy: {energy(phi, H_op):.6f}")

for step in range(steps):
    S = compute_S(phi, basis)
    b = compute_b_exact(phi, H_op, basis, dt)

    a = solve_a_eig(S, b, eps=1e-8)

    A = np.zeros_like(H_op, dtype=complex)
    for coeff, sigma in zip(a, basis):
        A += coeff * sigma

    U   = expm(-1j * A * dt)
    phi = U @ phi
    phi /= np.linalg.norm(phi)

    if step % 10 == 0 or step == steps-1:
        print(f"  Step {step:2d}: energy = {energy(phi, H_op):.6f}")

# -------------------------------------------------
# 6. FINAL RESULT
# -------------------------------------------------
probs    = np.abs(phi)**2
best_idx = np.argmax(probs)
best_bs  = format(best_idx, "04b")

print("\n" + "="*30)
print(f"FINAL RESULT (most probable bitstring): {best_bs}")
print("="*30)
for bit, name in zip(best_bs, names):
    print(f"{name:8}: {'INVITED' if bit == '1' else 'not invited'}")

print("\nState probabilities (non-negligible):")
for i, p in enumerate(probs):
    if p > 1e-6:
        print(f"|{format(i, '04b')}> : {p:.8f}")


'''import numpy as np

Q = np.array([
    [-400, 198, 200, 198],
    [   0, -400, 200, 198],
    [   0,   0, -400, 198],
    [   0,   0,   0, -400]
], dtype=float)

def cost(bitstring):
    x = np.array([int(b) for b in bitstring], dtype=float)
    return x @ Q @ x + 600

best = None
best_strings = []

for i in range(16):
    b = format(i, "04b")
    c = cost(b)
    print(b, c)
    if best is None or c < best:
        best = c
        best_strings = [b]
    elif np.isclose(c, best):
        best_strings.append(b)

print("\nBest cost:", best)
print("Best bitstrings:", best_strings)'''