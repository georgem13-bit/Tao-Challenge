# An explicit tenth-discriminant bound from Guo's zero gap via Kimura's Proposition 9

**Result.** Let $K$ be an imaginary quadratic field with fundamental discriminant
$D_K$, $d = |D_K|$. Then

$$h(K) = 1 \ \Longrightarrow\ d < e^{17.3} = 32{,}605{,}775.72\ldots$$

i.e. any tenth class-number-one discriminant satisfies $d \le 32{,}605{,}775$.
(Note: `compute_bound.py` prints the ceiling 32,605,776 as its "safe integer
bound"; that is safe but weaker by one. The sharp integer consequence of
$d < e^{17.3}$ is $d \le 32{,}605{,}775$, used here and in the paper.)
With the stronger constant of Guo's Remark 1.2 / Appendix A in place of his
Theorem 1.1 headline constant, the same derivation gives

$$h(K) = 1 \ \Longrightarrow\ d < e^{16.35} = 12{,}609{,}991\ldots$$

**Status of the inputs.** The derivation is a three-step chain in which every
non-elementary step is a cited, fully explicit statement from a named source.
No unverified computation (in particular not the Lu–Zaman–Zhao small-conductor
computation that Banks's all-conductor corollary rests on) is used.

## Step 1 — the zero gap (Guo)

Guo, *An explicit elementary proof of no Landau–Siegel zeros*, arXiv:2610.30476
(v1, 21 Oct 2026), **Theorem 1.1**: for every primitive quadratic Dirichlet
character $\chi$ of conductor $q \ge 3$, every real zero $\beta \in (0,1)$ of
$L(s,\chi)$ satisfies
$$(1-\beta)\log q \;>\; \tfrac{1}{100}.$$
In Kimura's terminology (arXiv:2610.21511, §2): the *zero gap* $(c, T)$ holds if
$(1-\beta)\ell \ge c$ for every primitive real character of conductor $q \ge 3$
with $\ell = \log q \ge T$ and every real zero $\beta$. Since Guo's inequality
holds for **all** $q \ge 3$, the zero gap $(c, T)$ holds with $c = 1/100$ for
**every** $T$.

(Guo, Remark 1.2: the same elementary argument also yields $c = 1/64$, with a
verification in his Appendix A; the headline constant $1/100$ is retained in
his Theorem 1.1 "so that a single choice of parameters covers all conductors".
Our variant below uses $c = 1/64$ and is labelled accordingly.)

## Step 2 — from the zero gap to $L(1,\chi)$ (Kimura, Proposition 9)

Kimura, *Imaginary quadratic fields of class number at most 2000*,
arXiv:2610.21511 (v2, 22 Oct 2026), **Proposition 9**: let $c > 0$ and $T \ge 2$
with $c/T \le 1/2$, and suppose the zero gap $(c,T)$ holds. Let $A > 0$ with
$AT \ge e$, let $V \ge 1$ be an integer, and put
$$\sigma_T = 1 - \frac{c}{T}, \qquad
  P = c\left(1 + \frac{\log(2VAT)}{T}\right),$$
$$\varepsilon = e^{c}\!\left(\frac{(AT)^{c/T} V^{c/T}}{cA} + \frac{4}{(AT)^{\sigma_T}}\right)
   + \frac{e^{P}}{cA} + \frac{4e^{P}}{V^{\sigma_T}} + \frac{e^{P}}{AT}.$$
If $\varepsilon < 1$, then every primitive real character $\chi$ of conductor
$q \ge 3$ with $\log q \ge T$ satisfies
$$\sqrt{q}\, L(1,\chi) \;\ge\; (1-\varepsilon)\, c\, e^{-P}\, \frac{e^{T/2}}{T}.$$
(The five terms of $\varepsilon$ are the statement's five fractions; the $e^c$
grouping of the first two follows Kimura's proof, where they arise as
$e^c (A\ell)^{c/\ell} V^{c/\ell}/(cA)$ and $4e^c (A\ell)^{-\sigma}$. Proposition 9
is the explicit form of Hecke's theorem that a zero gap gives
$L(1,\chi) \gg 1/\log q$; it is proved in Kimura's paper via his Lemma 8
(Dirichlet hyperbola + partial summation) and the surrounding results feed his
Lean-proved Theorem 10.)

## Step 3 — the class number formula (Kimura, eq. (4))

For a fundamental discriminant $-d$, Dirichlet's class number formula
(Davenport, Ch. 6, (15)) gives $2\pi h(-d) = w_K \sqrt{d}\, L(1, \chi_{-d})$,
where $w_K \ge 2$ is the number of roots of unity. Hence
$$\pi\, h(-d) \;\ge\; \sqrt{d}\, L(1, \chi_{-d}).$$
The character $\chi_{-d}$ is primitive of conductor $d$. So if $\log d \ge T$,
Step 2 applies and
$$\pi\, h(-d) \;\ge\; (1-\varepsilon)\, c\, e^{-P}\, \frac{e^{T/2}}{T}.$$
If the right-hand side exceeds $\pi$, then $h(-d) > 1$. Contrapositively,
$h(-d) = 1$ forces $\log d < T$.

## The arithmetic (all values computed and interval-certified; see `compute_bound.py`)

**Headline** ($c = 1/100$, $T = 17.3$, $A = 10^5$, $V = 10^4$; constraints
$c/T \le 1/2$ and $AT \ge e$ are satisfied with room to spare):

| quantity | value |
|---|---|
| $\sigma_T = 1 - c/T$ | $0.99942197$ |
| $P = c(1 + \log(2VAT)/T)$ | $0.02402724$ |
| $\varepsilon$ term 1: $e^c (AT)^{c/T}V^{c/T}/(cA)$ | $1.0239\times10^{-3}$ |
| $\varepsilon$ term 2: $4e^c/(AT)^{\sigma_T}$ | $2.3548\times10^{-6}$ |
| $\varepsilon$ term 3: $e^P/(cA)$ | $1.0243\times10^{-3}$ |
| $\varepsilon$ term 4: $4e^P/V^{\sigma_T}$ | $4.1191\times10^{-4}$ |
| $\varepsilon$ term 5: $e^P/(AT)$ | $5.9209\times10^{-7}$ |
| $\varepsilon$ (sum) | $0.00246309 < 1$ ✓ |
| $(1-\varepsilon) c e^{-P} e^{T/2}/T$ | $3.21436540$ |
| $\pi$ | $3.14159265$ |

Since $3.21436540 > \pi$ (margin $+0.0728$), $h(-d) > 1$ for all $\log d \ge 17.3$,
i.e. $h(-d) = 1 \Rightarrow d < e^{17.3} \approx 3.2606\times 10^{7}$.

**Variant** ($c = 1/64$ per Guo Remark 1.2/App. A, $T = 16.35$, $A = 10^5$, $V = 10^4$):
$P = 0.03876208$, $\varepsilon = 0.00175279$, and
$(1-\varepsilon) c e^{-P} e^{T/2}/T = 3.25884426 > \pi$ (margin $+0.1173$), giving
$d < e^{16.35} \approx 1.2610\times 10^{7}$.

Both final inequalities were re-verified in interval arithmetic (mpmath `iv`,
50-digit working precision): the certified enclosures satisfy $\varepsilon < 1$
and $\mathrm{LHS} > \pi$ with the displayed digits stable.

**Optimality within this route.** A grid search over
$A \in [10^3, 10^8]$, $V \in [10^2, 10^6]$, $T \in [12, 22]$ (see
`compute_bound.py`, Part B) finds the thresholds $T = 17.250$ (for $c = 1/100$)
and $T = 16.270$ (for $c = 1/64$); the certified values $17.3$ / $16.35$ above
are round choices just past the optima, trading a hair of tightness for
comfortable margins.

## Validation of the machinery (why the ε/P reconstruction is trusted)

Before using Proposition 9 with a new input, we reproduced Kimura's own
**Theorem 10** with our implementation of his $\varepsilon$ and $P$: taking
$A = 10^6$, $V = 10^4$ and his Table 1 pairs $(T_N, c_N)$, the computed
log-margins $\log\big[(1-\varepsilon) c_N e^{-P} e^{T_N/2} / (T_N N \pi)\big]$ are
$0.0199, 0.0313, 0.0092, 0.0237, 0.0720$ for $N = 100, 200, 500, 1000, 2000$ —
Kimura states the margins lie between $0.009$ (at $N = 500$) and $0.072$ (at
$N = 2000$), with $\varepsilon < 7.8\times10^{-4}$ throughout; we get
$\varepsilon \le 7.73\times10^{-4}$ and matching extrema locations. As a second
cross-check, running the same machinery with Kimura's grid constant
$c = 0.004401$ near $\ell = 19$ reproduces the threshold $T \approx 19.06$,
matching Rudolph's independent extraction $|D| < e^{19.0591}$ (comment 698480
on Tao's challenge post) to three decimals.

## Comparison with previously posted extractions through this route

Murphy's survey comment (698799, 26 Oct 2026) tabulates the Kimura-chain
extractions at $d < 6.47\times10^{7}$ (his "chain 58") and $d < 1.23\times10^{8}$
("chain 59", the input of Rudolph's $e^{19.0591} \approx 1.89\times10^{8}$
extraction). The present bound improves on all of these, by a factor of
$\approx 2$–$6$ (headline) or $\approx 5$–$15$ (variant). The improvement comes
solely from inserting Guo's constant ($1/100$, resp. $1/64$) — larger than
Kimura's grid constants in this range ($c \approx 0.0044$ near $\ell = 19$) —
into Kimura's Proposition 9. It does not compete with the determinant-method
bounds (Murphy $q < 565$; twinheterodox $q < 570$; Chung/rStation $D \le 331$)
or the quasi-Riemann Chowla–Selberg bounds (LemmaLab $d \le 653$); it is an
extraction record for the zero-gap $\to$ $L(1,\chi)$ route, of the kind the
challenge explicitly invites for each approach.

## What this does not do

* It is a *bound*, not a classification: the finite range $d < e^{17.3}$ is not
  enumerated here. (The classification in that range is in any case already
  known by other methods — Watkins 2004 covers class number $\le 100$ — but
  pairing the two is a separate step we do not claim.)
* It depends on Guo's preprint (v1, unrefereed) for the zero gap. Kimura's
  Proposition 9 and class-number-formula step are from a paper whose main
  theorems are Lean-proved; Guo's argument is elementary with all constants
  explicit and its numerical comparisons stated as rational inequalities, but
  it has not, to our knowledge, been formally verified or refereed. If Guo's
  constant were to fall, the same computation with Kimura's own grid constants
  recovers $d < e^{19.06} \approx 1.9\times10^{8}$ (Rudolph's bound), and with
  Banks + Lu–Zaman–Zhao ($c = 0.003$) a bound of the same shape at a larger $T$.
* Notation: $d$ here is always $|D_K|$, the absolute fundamental discriminant,
  which equals the conductor of $\chi_{-d}$. Some challenge comments use $q$
  for the conductor and some for a prime $\equiv 19 \pmod{24}$; we avoid $q$
  for the discriminant entirely.

*AI assistance disclosure: this derivation and its computation were produced
with AI assistance (Muse, Meta), working from the published sources
cited; the arithmetic was checked by interval arithmetic and by reproduction
of Kimura's Theorem 10 and Rudolph's threshold as independent controls.*
