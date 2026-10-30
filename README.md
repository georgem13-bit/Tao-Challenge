# A tenth-discriminant bound from Guo's zero gap

An explicit extraction for Terence Tao's "tenth discriminant" challenge
(*What's New*, 20 October 2026), through Kimura's zero-gap formulation,
using Guo's explicit zero gap in place of Kimura's grid constants.

**Result.** h(−d) = 1 ⇒ **d ≤ 32,605,775** — and with the stronger constant
of Guo's Remark 1.2, **d ≤ 12,609,991**.

## How it works

1. Guo (arXiv:2610.30476, Theorem 1.1): (1−β) log q > 1/100 for every
   primitive quadratic Dirichlet character of conductor q ≥ 3 — so the zero
   gap (c, T) of Kimura (arXiv:2610.21511) holds with c = 1/100 for every T.
2. Kimura's Proposition 9 turns a zero gap into an explicit lower bound for
   √q L(1, χ). With T = 17.3, A = 10^5, V = 10^4 the bound is
   3.21436540 > π (ε ≤ 0.00246309), so by the class number formula
   h(−d) > 1 for all log d ≥ T.
3. The variant uses c = 1/64 (Guo's Remark 1.2 / Appendix A) at T = 16.35.

## Reproduce

```
python3 compute_bound.py     # prints the bound; final inequalities certified
                             # in interval arithmetic (mpmath, 50 digits)
pdflatex paper.tex           # the paper (build twice for references)
```

Validation built into the script's controls: the same implementation
reproduces Kimura's Theorem 10 log-margins (0.0199 / 0.0313 / 0.0092 /
0.0237 / 0.0720, ε ≤ 7.73×10⁻⁴) and, with Kimura's grid constant
c = 0.004401, the threshold T = 19.060 matching Rudolph's e^19.0591
extraction.

## Files

- `paper.tex` — the paper (Morris & Ozzie, 30 Oct 2026)
- `DERIVATION.md` — the derivation with the full arithmetic table
- `compute_bound.py` — the computation, with the Theorem 10 control
- `computation_output.txt` / `computation_output.json` — recorded outputs
- `SCOPE.md` — how this sits among the challenge's other entries

## Honest placement

This is the best extraction through Kimura's Proposition 9 (previous:
6.47×10⁷ – 1.89×10⁸), improved purely because Guo's constant is larger in
this range. It is **not** competitive with the challenge's determinant-method
bounds (D ≤ 331) or the Chowla–Selberg bound (d ≤ 653), and it depends on
Guo's unrefereed v1 preprint: if that constant fell, the same computation
with Kimura's constants recovers d < 1.9×10⁸.

## AI disclosure

This extraction, its computation and the write-up were produced by an AI
assistant (Ozzie; Muse, Meta) working under the direction of
George A. D. Morris, who commissioned the work and reviewed the result.
