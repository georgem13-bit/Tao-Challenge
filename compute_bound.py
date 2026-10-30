#!/usr/bin/env python3
"""
Tenth-discriminant bound extraction:  Guo (zero gap)  +  Kimura Proposition 9.

Pipeline (every step sourced):
  * Guo, arXiv:2610.30476, Theorem 1.1: for every primitive quadratic Dirichlet
    character chi of conductor q >= 3, every real zero beta of L(s,chi) satisfies
    (1-beta) log q > 1/100.  Hence Kimura's "zero gap (c,T)" holds with c = 1/100
    for EVERY T.  (Guo Remark 1.2 + Appendix A: the same argument yields c = 1/64;
    we compute that variant separately and label it as such.)
  * Kimura, arXiv:2610.21511, Proposition 9: if the zero gap (c,T) holds, then for
    A > 0 with AT >= e and integer V >= 1, with
        sigma_T = 1 - c/T,
        P       = c * (1 + log(2*V*A*T)/T),
        eps     = e^c * [ (AT)^(c/T) * V^(c/T) / (cA) + 4 / (AT)^sigma_T ]
                  + e^P/(cA) + 4 e^P / V^sigma_T + e^P/(AT),
    if eps < 1 then every primitive real chi of conductor q >= 3 with log q >= T
    satisfies   sqrt(q) * L(1,chi) >= (1-eps) * c * e^{-P} * e^{T/2} / T.
    (The eps formula is the statement's five fractions; the grouping of e^c over
    the first two terms follows Kimura's proof, where those two terms arise as
    e^c (A l)^{c/l} V^{c/l}/(cA) and 4 e^c (A l)^{-sigma}.)
  * Kimura, eq. (4) (Dirichlet class number formula, Davenport Ch.6 (15)):
        pi * h(-d) >= sqrt(d) * L(1, chi_{-d})
    for a fundamental discriminant -d (since 2 pi h = w sqrt(d) L(1,chi), w >= 2).
  Therefore, if (1-eps) c e^{-P} e^{T/2} / T > pi, then h(-d) > 1 for every
  fundamental discriminant with log d >= T, i.e.
        h(-d) = 1   ==>   d < e^T.

Part A validates the eps/P reconstruction by reproducing Kimura's Theorem 10
(A = 10^6, V = 10^4; his paper states eps < 7.8e-4 and log-margins between
0.009 (N=500) and 0.072 (N=2000)).
Part B optimises (A, V, T) for c = 1/100 and for c = 1/64.
Part C re-verifies the chosen parameter sets in interval arithmetic (mpmath.iv).
"""
import math
import json
from mpmath import mp, mpf, iv

mp.dps = 80
iv.dps = 50


def prop9(c, T, A, V, exp=math.exp, log=math.log, pi=math.pi):
    """Return dict with P, eps, LHS = (1-eps) c e^{-P} e^{T/2} / T."""
    sigma_T = 1 - c / T
    P = c * (1 + log(2 * V * A * T) / T)
    eps = (exp(c) * ((A * T) ** (c / T) * V ** (c / T) / (c * A)
                     + 4 / (A * T) ** sigma_T)
           + exp(P) / (c * A)
           + 4 * exp(P) / V ** sigma_T
           + exp(P) / (A * T))
    lhs = (1 - eps) * c * exp(-P) * exp(T / 2) / T
    return {"sigma_T": sigma_T, "P": P, "eps": eps, "lhs": lhs}


print("=" * 78)
print("PART A -- validation: reproduce Kimura Theorem 10 (A=1e6, V=1e4)")
print("=" * 78)
table1 = [  # (N, T_N, c_N) from Kimura Table 1
    (100, 28.6787, 0.005506),
    (200, 30.1458, 0.005622),
    (500, 32.0058, 0.005759),
    (1000, 33.4757, 0.005861),
    (2000, 35.0131, 0.005965),
]
margins = {}
for N, T, c in table1:
    r = prop9(c, T, 1e6, 1e4)
    margin = math.log(r["lhs"] / (N * math.pi))
    margins[N] = margin
    print(f"N={N:5d}  T={T:8.4f}  c={c:.6f}  eps={r['eps']:.3e}  "
          f"P={r['P']:.5f}  log-margin={margin:+.4f}")
print(f"eps < 7.8e-4 for all rows: {all(prop9(c,T,1e6,1e4)['eps'] < 7.8e-4 for _,T,c in table1)}")
print(f"min margin at N=500: {min(margins, key=margins.get) == 500}; "
      f"max margin at N=2000: {max(margins, key=margins.get) == 2000}")
print(f"margin range: [{min(margins.values()):.4f}, {max(margins.values()):.4f}]"
      "   (Kimura states 0.009 .. 0.072)")

print()
print("=" * 78)
print("PART B -- our extraction: minimise e^T s.t. LHS > pi  (h(-d)=1 => d < e^T)")
print("=" * 78)

A_grid = [10.0 ** (3 + 0.25 * i) for i in range(21)]          # 1e3 .. 1e8
V_grid = [10 ** k for k in range(2, 7)] + [3 * 10 ** 4, 3 * 10 ** 5]
T_grid = [12.0 + 0.005 * i for i in range(2001)]              # 12.000 .. 22.000


def best_for_c(c, label):
    best = None
    for A in A_grid:
        for V in V_grid:
            for T in T_grid:
                if c / T > 0.5:
                    continue
                r = prop9(c, T, A, V)
                if r["eps"] < 1 and r["lhs"] > math.pi:
                    if best is None or T < best["T"]:
                        best = {"c": c, "T": T, "A": A, "V": V, **r}
                    break  # smallest T for this (A,V)
    print(f"\n{label}: c = {c}")
    print(f"  best T = {best['T']:.3f}  (A = {best['A']:.4g}, V = {best['V']:.4g})")
    print(f"  eps = {best['eps']:.4e},  P = {best['P']:.5f},  "
          f"LHS = {best['lhs']:.6f} > pi = {math.pi:.6f}, "
          f"log-margin = {math.log(best['lhs']/math.pi):+.4f}")
    print(f"  e^T = {math.exp(best['T']):,.0f}")
    return best


b100 = best_for_c(0.01, "Guo Theorem 1.1 constant")
b64 = best_for_c(1 / 64, "Guo Remark 1.2 / Appendix A constant")

# Also: Kimura's own grid constant at comparable range (c = 0.004401, the value
# Rudolph read off Kimura's grid at T = 19.0591) for comparison of constants.
bkim = best_for_c(0.004401, "Kimura grid constant near l=19 (comparison only)")

print()
print("=" * 78)
print("PART C -- interval-arithmetic certification of clean parameter choices")
print("=" * 78)


def prop9_iv(c, T, A, V):
    """Interval version. All inputs exact decimals/rationals as strings."""
    c, T, A, V = iv.mpf(c), iv.mpf(T), iv.mpf(A), iv.mpf(V)
    sigma_T = 1 - c / T
    P = c * (1 + iv.log(2 * V * A * T) / T)
    e_c = iv.exp(c)
    e_P = iv.exp(P)
    eps = (e_c * ((A * T) ** (c / T) * V ** (c / T) / (c * A)
                  + 4 / (A * T) ** sigma_T)
           + e_P / (c * A) + 4 * e_P / V ** sigma_T + e_P / (A * T))
    lhs = (1 - eps) * c * iv.exp(-P) * iv.exp(T / 2) / T
    return eps, lhs


def certify(c, T, A, V, label):
    eps, lhs = prop9_iv(str(c), str(T), str(A), str(V))
    pi_iv = iv.pi
    ok_eps = float(eps.b) < 1
    ok_lhs = float(lhs.a) > float(pi_iv.b)
    print(f"{label}: c={c}, T={T}, A={A}, V={V}")
    print(f"  eps in [{float(eps.a):.6e}, {float(eps.b):.6e}]"
          f"  -> eps < 1 certified: {ok_eps}")
    print(f"  LHS in [{float(lhs.a):.8f}, {float(lhs.b):.8f}],"
          f"  pi < {float(pi_iv.b):.8f} "
          f"-> LHS > pi certified: {ok_lhs}")
    eT = math.exp(T)
    print(f"  => h(-d) = 1 implies d < e^{T} = {eT:,.0f}; "
          f"safe integer bound: d <= {math.ceil(eT):,}")
    return {"c": c, "T": T, "A": A, "V": V,
            "eps_hi": float(eps.b), "lhs_lo": float(lhs.a),
            "eT": eT, "certified": bool(ok_eps and ok_lhs)}


# Clean round choices near the optima (T on a 0.05 grid, A/V powers of ten).
certs = []
for c, T, A, V, label in [
    (0.01, 17.30, 1e5, 1e4, "Headline (Guo Thm 1.1, c=1/100)"),
    (1 / 64, 16.35, 1e5, 1e4, "Variant (Guo Rem 1.2/App A, c=1/64)"),
]:
    # confirm with float pipeline first that these choices work, else nudge T
    r = prop9(c, T, A, V)
    while not (r["eps"] < 1 and r["lhs"] > math.pi):
        T = round(T + 0.05, 2)
        r = prop9(c, T, A, V)
    certs.append(certify(c, T, A, V, label))
    print()

summary = {
    "validation_margins": {str(k): v for k, v in margins.items()},
    "best_float": {
        "c_1_100": {k: b100[k] for k in ("T", "A", "V", "eps", "P", "lhs")},
        "c_1_64": {k: b64[k] for k in ("T", "A", "V", "eps", "P", "lhs")},
        "c_kimura_grid": {k: bkim[k] for k in ("T", "A", "V", "eps", "P", "lhs")},
    },
    "certified": certs,
}
with open("computation_output.json", "w") as f:
    json.dump(summary, f, indent=2)
print("Wrote computation_output.json")
