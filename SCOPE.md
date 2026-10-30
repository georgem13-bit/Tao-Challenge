# SCOPE — Tao's "tenth discriminant" challenge

*Phase 1 deliverable. Compiled 2026-10-30 from primary sources: Tao's challenge
post and proof-sketch post (full HTML + all 89 comments, saved in `sources/`),
and the full texts of the Banks, Kerr, Green, Kimura, Guo and van Dijk papers
(PDFs + extracted text in `sources/`).*

## 1. The task, in Tao's own terms

Terence Tao, "An experimental AI-math challenge: using tenth discriminant
bounds to explore arguments ruling out Siegel zeroes", *What's New*,
20 October 2026:
https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/

Preceded by "A sketch of the proof of non-existence of Siegel zeroes"
(19 October 2026), an exposition of Green's determinant argument.

The challenge: for each new manuscript or digestion relating to the
quasi-Riemann hypothesis or the Landau–Siegel zero problem, or by a novel
argument, **use an AI tool to work out an effective upper bound for a
hypothetical tenth discriminant, without using Heegner's methods, and make
best efforts to optimise the constant.**

Background: the nine known Heegner discriminants are
d = 1, 2, 3, 7, 11, 19, 43, 67, 163 (fields Q(√−d) of class number one).
If d is a Heegner number and χ its quadratic character, the class number
formula gives L(1,χ) = π/√d, and one can produce a Landau–Siegel zero
β with 1 − β ≍ 1/√d. A strong explicit zero-free result therefore bounds d.
Historical effective bounds quoted by Tao: Goldfeld's method, d ≤ e^7000;
Oesterlé's improvement, d ≤ e^55. (Commenter Aleksei Kulikov corrected the
attribution: the explicit constants are Oesterlé's; 7000 came from optimising
Goldfeld with the Gross–Zagier curve, 55 from the Brumer–Kramer curve.)

### Rules / norms (from the post)

- Contribute bounds **in the comments** of the challenge post.
- Any amount of AI use is permitted **so long as it is disclosed**.
- Large outputs should be posted as **links** (e.g. a GitHub repository) with
  a human-generated summary in the comment text.
- Building on previous contributions is appropriate, **with attribution**.
- Do **not** prioritise speed over quality; the intended spirit is
  collaborative / Polymath-style, not a race.
- Formal verification (e.g. Lean) is **not insisted on**, but anyone
  submitting a purely AI-generated solution should do due diligence, e.g.
  check the output with an independent AI tool.
- Tao explicitly welcomes bounds from **any specific approach**, even if
  worse than Goldfeld/Oesterlé, and "negative" results where a method gives
  a large bound are still scientifically useful.

## 2. Current best posted bound (the number to beat)

**D ≤ 331** — Stephen Chung / rStation agents (dualverse-ai), comment
698892, 28 October 2026, via sharpening the full-rank step in the
interpolation-determinant method. Progression: D ≤ 499 → D ≤ 498
(698855, 27 Oct) → D ≤ 331. Write-ups:
https://github.com/dualverse-ai/tenth_discriminant (folders `bound-331/`,
`bound-498/`); raw agent papers at rstation.ai. Stated external rechecks by
GPT-6 Astra and Claude Opus 5.5 — AI verification, not human peer review.

### Participant catalogue (89 comments, latest 28 Oct 2026)

Notation warning: participants use q inconsistently — sometimes the
conductor |disc|, sometimes a prime. Our derivation uses d = |D_K|
throughout.

- **Silberman** (698449/698451): inert-prime/Mertens extraction; first pass
  q < 10^15 corrected to **q < 10^45**. Preliminary.
- **twinheterodox** (Banks/Green determinant series, Codex/GPT-6-Astra,
  AI-disclosed): v1 q < 10^10 → v2 q < 5×10^7 → v3 q < 10^6 → v4 q < 4000 →
  v5 q < 2000 → v6/v6.1 **q < 570** (Green determinant + van Dijk auxiliary
  inert prime + Pratt norm-count ideas; audited by Larsson, 698516/698595) →
  v7 (698809) same bound, single unified proof. Elementary companion:
  **q < 2^15 = 32,768**. GRH comparison: q ≤ 200 under GRH (Stopple's
  Chowla–Selberg exposition).
- **Tao's own extraction** (698471, SAIR model): Selberg–Chowla gives a zero
  β ≥ 1 − 3.2/√d for d ≥ 655; with the 7/8 quasi-RH, **d < 655**; with the
  11/12 quasi-RH, **d < 1475**.
- **LemmaLab** (698472/698473): evaluate Chowla–Selberg at s = 7/8 directly:
  **h(−d) = 1 ⇒ d ≤ 653** (Arb-certified ζ_K(7/8) ≥ 1.39×10^−5 at d = 654);
  11/12 version **d ≤ 1151** (numerical, not certified).
  Code: github.com/LemmaLabMath/qrh-class-numbers.
- **Henric Larsson** (698469): **|D| < 50,000** via Banks + Lu–Zaman–Zhao +
  elementary class-number lower bound; two exact enumerations recover the
  nine fields. Repo: github.com/henlar1975/Tao-tenth-discriminent-bound.
- **Kerr** (698475): hybrid explicit version, cutoff **|Δ| < 11,000**
  (polynomial-lattice refinements give q < 200,000; remaining interval via
  Lu–Zaman–Zhao + sharper Chowla–Selberg sign test).
- **Rudolph** (698480): Kimura-based extraction, **|D| < e^19.0591 <
  189,348,540**, using Kimura Prop. 9 with c = 0.004401, T = 19.0591,
  A = 2,000,000, V = 17,550; CRT sieve to 89 clears candidates above 163.
  States he did not independently replay Kimura's Lean certificates.
- **Peter W. Murphy**: two kernel-checked Lean 4 proofs of the full
  class-number-one classification (7/8 zero-free region + Chowla–Selberg;
  and a determinant proof with endpoint q < 2^15, no L-function constants in
  the dependency closure; independently rebuilt by Antoine Olivier, 698668).
  Survey + sharpening (698799): **q < 565**, Arb-certified, not
  kernel-checked. Survey numbers: zero-free Chowla–Selberg family floor is
  64π²e^(−2γ) = 199.1208…; Banks gives d < 10^10; Kimura zero-gap chains
  give d < 6.47×10^7 ("chain 58") and d < 1.23×10^8 ("chain 59");
  twinheterodox's q < 570 has equivalent zero-free abscissa 0.861.
- **Jesús / Dojo-1** (698807/698839/698904): Lean theorems (only propext,
  Classical.choice, Quot.sound): full classification for Q(√−d), and for any
  totally complex quadratic field with h(K) = 1, **|disc K| < 5×10^10**;
  h(K) ≤ 2 ⇒ |disc K| < 2^52. Route: Green Gram determinant + residue-class
  sieve checked by the Lean kernel to 7×10^11.
  Repo: github.com/Dojo-1/tenth-discriminant.
- **Anonymous / Tom Joel Roltsch** (698759): bound **187** with a
  ResearchGate DOI but **no derivation in the thread**; Murphy lists it as
  NR (not reproducible). It lies below the 199.12 floor of the zero-free
  Chowla–Selberg family, so it would need a different input entirely.
- **Kyle Pratt's Kimi experiments** (698526/698682): q < 54,000 claimed with
  flawed numerics; audit suggested q < 160,000; Pratt's verdict "mixed" —
  treat as unreliable. Durable contributions: a tenth discriminant q > 163
  is prime ≡ 3 (mod 4) (genus theory), in fact q ≡ 19 (mod 24), with CRT
  refinements (q ∈ {43, 67} mod 120).

## 3. Source proofs — explicit chains

- **OpenAI**, *Uniform exclusion of Landau–Siegel zeros* (1 Oct 2026):
  asserts (1−β) log q ≥ c for an absolute c > 0, **no numerical value** in
  the abstract. Family 003 (quasi-Riemann hypothesis) claims zero-freeness
  for Re s > 7/8; its Lean comparator states 1 − β ≥ c/log q with **no
  explicit c**. Usable only via fixed-point (Chowla–Selberg at 7/8)
  arguments, as LemmaLab/Murphy do.
- **Banks**, arXiv:2610.15483, Thm 1.1: q_0 = 10^10, δ_0 = 3.0×10^−3:
  (1−β) log q ≥ δ_0 for all primitive real χ of conductor q ≥ q_0; extended
  to all q ≥ 3 via Lu–Zaman–Zhao's computation (for q ≤ 10^10, no real zero
  β ≥ 1 − 1/(5 log q)). Clean explicit constant, but the small-conductor
  side rests on a cited computation.
- **Lu–Zaman–Zhao** (cited as Banks's ref. [5], *Numerical computations
  concerning Landau–Siegel zeros*): the finite-range computation behind
  Banks's all-conductor extension. (The file `sources/2610.29018.*` is a
  different, related paper: Dave Platt, *Zeros of quadratic Dirichlet
  L-functions*, arXiv:2610.29018 — L(σ,χ) ≠ 0 for σ > 0 when q ≤ 10^9
  (even χ) / q ≤ 10^10 (odd χ). Neither is used by our route.)
- **Kerr**, arXiv:2610.21099, Thm 1: (1−β) log|q| ≥ c for an absolute c —
  **no numerical value given**; explicitness only in combination with
  finite-range inputs (hence his 11,000 hybrid).
- **Green**, hexagon:2610.00311 (v2): determinant argument in Q(√d);
  Thm 1.1 gives an inert-prime sum ≤ (1/2 + O(1/C)) log X + O_C(1) —
  constants **not numerically explicit**. The engine behind the best
  determinant bounds, but requires substantial extra work to make explicit
  (twinheterodox, Murphy, Jesús did exactly that).
- **Kimura**, arXiv:2610.21511 (v2): Thm 1: (1−β) log q ≥ 5.811×10^−4 for
  all q ≥ 3; ≥ 5.965×10^−3 once log q ≥ 35.0131. **Prop. 9** converts a zero
  gap (c, T) into an explicit lower bound
  √q L(1,χ) ≥ (1−ε) c e^(−P) e^(T/2)/T with a fully explicit five-term ε
  (see `DERIVATION.md` / the paper for the formula). Eq. (4) is the class
  number formula 2πh(−d) = w_K √d L(1,χ_{−d}). Thm 10 (table of (N, T_N,
  c_N)) and Thm 1 are **proved in Lean**. Thm 2: exactly 16,453,493 imaginary
  quadratic fields have class number ≤ 2000.
- **Guo**, arXiv:2610.30476 (v1): Thm 1.1: (1−β) log q > **1/100** for every
  primitive quadratic χ, q ≥ 3 — the zero gap (c, T) = (1/100, any T).
  Remark 1.2: the same argument yields **c = 1/64** (Appendix A verification;
  q ≥ 7 via x = q^46, y = q^4; q = 3, 4, 5 by positive-block grouping).
  Elementary (Dirichlet hyperbola + character-sum positivity), explicit
  constants throughout, **but an unrefereed v1 preprint, not formally
  verified** as far as we know.
- **van Dijk**, hexagon:2610.00409 (v2), Cor. 2: h(K) = 1 ⇒ D < 8×10^9,
  self-contained determinant argument with an auxiliary largest inert prime.

## 4. The mathematical pipeline (our route)

1. **Zero gap.** Guo Thm 1.1: every primitive quadratic χ of conductor
   q ≥ 3 and every real zero β satisfy (1−β) log q > c with c = 1/100
   (variant: c = 1/64, Guo Remark 1.2 / Appendix A). Hence Kimura's zero gap
   (c, T) holds for every T.
2. **Zero gap ⇒ L(1,χ) bound.** Kimura Prop. 9: for A > 0 with AT ≥ e and
   integer V ≥ 1, with σ_T = 1 − c/T, P = c(1 + log(2VAT)/T), and ε the
   explicit five-term expression in Prop. 9, if ε < 1 then every χ with
   log q ≥ T satisfies
   √q L(1,χ) ≥ (1−ε) c e^(−P) e^(T/2)/T.
3. **Class number formula.** Kimura eq. (4) (Davenport, Ch. 6 (15)):
   2πh(−d) = w_K √d L(1,χ_{−d}), and w_K ≥ 2, so πh(−d) ≥ √d L(1,χ_{−d}).
4. **Contradiction at h(−d) = 1.** If (1−ε) c e^(−P) e^(T/2)/T > π, then no
   fundamental discriminant with d ≥ e^T (and d ≥ 3) has h(−d) = 1.
5. **Optimise** (A, V, T) by grid search, then **certify** the final
   inequality in interval arithmetic (mpmath `iv`, 50-digit precision).

Why this route: it is the only fully explicit chain covering **all**
conductors q ≥ 3 with **no unverified finite computation** on our side —
Guo's theorem needs no small-conductor supplement (contrast Banks, whose
all-q constant routes through Lu–Zaman–Zhao), and Kimura's conversion is
Lean-proved on his side. Its weakness is equally clear: the zero-gap →
class-number conversion loses enormously versus determinant or
Chowla–Selberg-at-a-fixed-point arguments, so the resulting bound is
competitive only **within the Kimura Prop. 9 extraction family**
(Rudolph 1.89×10^8; Murphy's chains 6.47×10^7, 1.23×10^8).

## 5. Candidate strategies, ranked (tightness × tractability)

1. **Guo gap + Kimura Prop. 9 extraction** (chosen; executed in Phase 2):
   fully explicit today, one short script, certifiable in interval
   arithmetic. Ceiling ~10^7 — a per-approach contribution of exactly the
   kind Tao invited, not a bid for the overall lead.
2. **Determinant method made explicit** (Green/van Dijk line): the route to
   the current leaders (570 / 565 / 331), but each step (Gram determinant,
   auxiliary inert prime, finite check) is a substantial formalisation
   effort; twinheterodox/Murphy/Jesús/Chung have already mined it hard.
3. **Chowla–Selberg at s = 7/8** (LemmaLab/Murphy): d ≤ 653 posted and
   Arb-certified; the family's floor is 199.12, and beating 653 needs
   either the 11/12 region (1151, worse constant trade-off in practice) or
   new input. Low headroom for us.
4. **Banks + finite range**: d < 10^10 posted by Murphy's survey from
   Banks's theorem directly; Larsson's 50,000 hybrid is the polished
   version. Superseded by (1) for explicitness-per-effort.
5. **Kerr hybrid**: 11,000 posted by Kerr himself; reproducing it means
   redoing his polynomial-lattice computation. Parked.

## 6. Phase 2 — executed (summary; full working in DERIVATION.md + paper)

- Machinery validated two ways: our implementation of Kimura's ε and P
  reproduces his Thm 10 log-margins (0.0199, 0.0313, 0.0092, 0.0237, 0.0720
  for N = 100…2000; Kimura states range 0.009–0.072, ε < 7.8×10^−4; we get
  ε ≤ 7.73×10^−4); and with Kimura's grid constant c = 0.004401 it returns
  threshold T = 19.060, e^T = 189,519,030, matching Rudolph's independent
  extraction e^19.0591 ≈ 1.89×10^8.
- Headline (interval-certified; c = 1/100, T = 17.3, A = 10^5, V = 10^4):
  ε = 0.00246309 < 1; (1−ε) c e^(−P) e^(T/2)/T = 3.21436540 > π
  (margin +0.07277274). Hence **h(−d) = 1 ⇒ d < e^17.3 = 32,605,775.72…, i.e. d ≤ 32,605,775** (the script prints the safe ceiling 32,605,776; the sharp integer bound is 32,605,775).
- Variant (c = 1/64; T = 16.35, A = 10^5, V = 10^4): LHS = 3.25884426 > π
  (margin +0.11725161). Hence **h(−d) = 1 ⇒ d < e^16.35 = 12,609,991.1**.
- Placement: improves every previously posted Kimura-Prop.-9 extraction by
  ~2–6× (headline) / ~5–15× (variant), purely because Guo's constant beats
  Kimura's grid constants in this range. Does **not** compete with the
  determinant bounds (565/570/331) or QRH bounds (653).

## 7. Risks and open questions

- **Guo's status.** The headline rests on Guo's unrefereed v1 preprint.
  Mitigation: Kimura's side is Lean-proved; Guo's argument is elementary
  with explicit constants and rational-inequality numerics, independently
  re-checkable; and if Guo's constant fell, the same script with Kimura's
  grid constants recovers d < e^19.06 ≈ 1.9×10^8. The c = 1/64 variant
  additionally rests on Guo's Appendix A.
- **Bound ≠ classification.** We do not enumerate d < e^17.3; finite-range
  classification is a separate step (Kimura's Thm 2 machinery, or the
  sieves of Larsson/Rudolph/Murphy).
- **Notation collisions** across comments (q as conductor vs prime) —
  handled by fixing d = |D_K| in all our writing.
- **The 187 claim** is unreproducible as posted and below the zero-free
  family's floor; ignore unless a derivation appears.
- **Certification depth.** Our final inequalities are interval-certified
  (mpmath, 50-digit), not Lean-kernel-checked. A Lean formalisation of the
  arithmetic step alone would be feasible (it is elementary real
  arithmetic over explicit expressions) but is future work.

## 8. Files

- `DERIVATION.md` — Phase 2 derivation in full.
- `compute_bound.py`, `computation_output.txt`, `computation_output.json`,
  `breakdown.txt` — reproducible computation.
- `paper/` — the academic write-up (LaTeX + PDF), **ready for George's
  approval; nothing posted anywhere** (final delivery rule, 2026-10-30).
- `sources/` — Tao's posts + all 89 comments; PDFs + text of Banks, Kerr,
  Green, Kimura, Guo, van Dijk, Lu–Zaman–Zhao.
- Programme log: `~/workspace/frontier-math/PROGRAMME.md`.
