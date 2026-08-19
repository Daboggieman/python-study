# Base Conversion — A Manual Walkthrough (Any Base to Any Base)

This lecture builds on the integer↔string document, but generalizes everything from "base 10" to **any base B**. By the end you should be able to manually convert a number from any base to any other base — decimal to hex, binary to octal, base-7 to base-13, anything — using nothing but division, remainder, multiplication, and addition.

---

## Part 0 — What a "Base" Actually Means

A base (also called a *radix*) is simply: how many distinct digit symbols exist, and what each position in a number is worth.

In base 10, there are 10 symbols (`0`–`9`), and each position to the left is worth 10× the position to its right:

```
"present position weights" for the number 4 0 5 in base 10:
   4        0        5
 ×100     ×10       ×1
 (10²)    (10¹)     (10⁰)
```

This generalizes directly. For **any** base `B`, a number written as digits `d_n d_(n-1) ... d_1 d_0` represents the value:

```
value = d_n × B^n + d_(n-1) × B^(n-1) + ... + d_1 × B^1 + d_0 × B^0
```

Every digit `d_i` must be a value between `0` and `B−1`. That's the entire definition of a positional numeral system — everything else in this document is just mechanically applying that one formula in each direction.

### 0.1 — Digit symbols for bases larger than 10

Base 10 only needs ten symbols, `0`–`9`. Once a base exceeds 10 (like hexadecimal, base 16), you run out of numerals and conventionally continue with letters:

```
0 1 2 3 4 5 6 7 8 9 A B  C  D  E  F  ...
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ...
```

So in hex, the digit `'A'` has the *value* 10, `'B'` has value 11, and so on up through `'Z'` for value 35 (this lets you represent any base up to 36 using digits 0–9 and letters A–Z). The mapping is exactly analogous to the `'0'`-offset trick from the integer/string document, just extended:

- If a digit character is `'0'`–`'9'`, its value is `character − '0'` (giving 0–9).
- If a digit character is a letter `'A'`–`'Z'` (or lowercase `'a'`–`'z'`), its value is `10 + (character − 'A')` (giving 10–35).

Keep this mapping firmly in mind — it's used constantly below.

---

## Part 1 — Converting FROM Base 10 TO Any Other Base

This is the "decompose" direction, and it works exactly like the integer→string process from the companion document, except you divide by `B` instead of by 10.

### 1.1 The algorithm

1. Let `N` be the decimal number you're converting, and `B` be the target base.
2. Compute `remainder = N mod B`. This remainder (0 through B−1) is the **rightmost, least-significant digit** of the answer. Convert this remainder to its digit symbol using the table in 0.1 (0–9 stay as-is; 10–35 become A–Z).
3. Compute `N = N ÷ B` (integer division, dropping any fractional remainder).
4. Repeat steps 2–3 using the new, smaller `N`, collecting digit symbols as you go.
5. Stop once `N` becomes 0.
6. Because — exactly as before — each digit you extract is the *next* less significant one, meaning they come out **right-to-left**, you must **reverse** the collected digits at the end to get the correctly-ordered result.

### 1.2 Worked example: 202 (base 10) → base 16 (hex)

| Step | N | N mod 16 | digit symbol | N ÷ 16 |
|---|---|---|---|---|
| 1 | 202 | 10 | `A` | 12 |
| 2 | 12 | 12 | `C` | 0 → stop |

Collected in extraction order: `A, C`. Reverse: `C, A`. **Answer: `"CA"`** (in hex, CA = 12×16 + 10 = 192+10 = 202 ✔).

### 1.3 Worked example: 202 (base 10) → base 2 (binary)

| Step | N | N mod 2 | digit | N ÷ 2 |
|---|---|---|---|---|
| 1 | 202 | 0 | 0 | 101 |
| 2 | 101 | 1 | 1 | 50 |
| 3 | 50 | 0 | 0 | 25 |
| 4 | 25 | 1 | 1 | 12 |
| 5 | 12 | 0 | 0 | 6 |
| 6 | 6 | 0 | 0 | 3 |
| 7 | 3 | 1 | 1 | 1 |
| 8 | 1 | 1 | 1 | 0 → stop |

Extraction order: `0,1,0,1,0,0,1,1`. Reversed: `1,1,0,0,1,0,1,0`. **Answer: `"11001010"`**.

Check: 128+64+0+0+8+0+2+0 = 202 ✔.

### 1.4 Worked example: 202 (base 10) → base 7

| Step | N | N mod 7 | digit | N ÷ 7 |
|---|---|---|---|---|
| 1 | 202 | 6 | 6 | 28 |
| 2 | 28 | 0 | 0 | 4 |
| 3 | 4 | 4 | 4 | 0 → stop |

Extraction order: `6,0,4`. Reversed: `4,0,6`. **Answer: `"406"`** (base 7).
Check: 4×49 + 0×7 + 6×1 = 196+0+6 = 202 ✔.

---

## Part 2 — Converting FROM Any Base TO Base 10

This is the "reconstruct" direction, using the exact same accumulator idea from the string→integer half of the companion document, generalized from ×10 to ×B.

### 2.1 The algorithm

1. Let the source number be a sequence of digit symbols, read **left to right** (most significant digit first), in base `B`.
2. Initialize `running_total = 0`.
3. For each digit symbol, left to right: convert the symbol to its numeric value using the table in 0.1, then compute `running_total = running_total × B + digit_value`.
4. After the last digit, `running_total` is the base-10 value.

This works for the same reason the string→integer accumulator worked: each multiplication by `B` re-weights everything accumulated so far by one more power of `B`, making room for the newly-read digit in the "ones" place of the current partial number.

### 2.2 Worked example: hex `"1A3"` → decimal

| Step | Digit symbol | digit value | Calculation | running_total |
|---|---|---|---|---|
| start | — | — | — | 0 |
| 1 | `'1'` | 1 | 0×16 + 1 | 1 |
| 2 | `'A'` | 10 | 1×16 + 10 | 26 |
| 3 | `'3'` | 3 | 26×16 + 3 | 419 |

**Answer: 419.** Check via the expansion formula: 1×16² + 10×16¹ + 3×16⁰ = 256+160+3 = 419 ✔.

### 2.3 Worked example: binary `"11001010"` → decimal

| Step | Digit | value | Calculation | running_total |
|---|---|---|---|---|
| start | — | — | — | 0 |
| 1 | 1 | 1 | 0×2+1 | 1 |
| 2 | 1 | 1 | 1×2+1 | 3 |
| 3 | 0 | 0 | 3×2+0 | 6 |
| 4 | 0 | 0 | 6×2+0 | 12 |
| 5 | 1 | 1 | 12×2+1 | 25 |
| 6 | 0 | 0 | 25×2+0 | 50 |
| 7 | 1 | 1 | 50×2+1 | 101 |
| 8 | 0 | 0 | 101×2+0 | 202 |

**Answer: 202** — matches the round trip from Part 1.3. ✔

---

## Part 3 — Converting Directly Between Two Non-Decimal Bases

There is no shortcut that skips arithmetic entirely — but there *is* a standard, reliable strategy, plus one very handy special case.

### 3.1 The general method: use base 10 as a bridge

To convert a number in base `B1` directly to base `B2`:

1. **Stage 1:** Use Part 2's method to convert the base-`B1` number *into* base 10 (decimal).
2. **Stage 2:** Use Part 1's method to convert that decimal value *into* base `B2`.

This "bridge through base 10" approach is the universal, always-works method, because Part 1 and Part 2 only ever needed to know how to talk to base 10 — chaining them lets you go from any base to any other base.

### 3.2 Worked example: base 7 `"406"` → base 2

**Stage 1 (base 7 → base 10):** using the accumulator method with B=7:
- `0×7+4 = 4`
- `4×7+0 = 28`
- `28×7+6 = 202`
→ decimal 202 (matches Part 1.4's round trip ✔).

**Stage 2 (base 10 → base 2):** this is exactly the table already worked out in Part 1.3, giving `"11001010"`.

**Answer: base 7 `"406"` = base 2 `"11001010"`.**

### 3.3 Special case shortcut: converting between power-of-two bases

Binary (2), octal (8 = 2³), and hexadecimal (16 = 2⁴) are all powers of two. Because of this, you can convert between *any pair* of these three without going through decimal at all, by grouping binary digits:

- **Binary → Octal:** group binary digits into sets of **3** starting from the right (pad the leftmost group with leading zeros if needed), then convert each group of 3 bits directly to its single octal digit (0–7) using the expansion formula on just those 3 bits.
- **Binary → Hex:** group binary digits into sets of **4** starting from the right, then convert each group of 4 bits directly to its single hex digit (0–F).
- **Octal → Binary / Hex → Binary:** the reverse — expand each octal digit into exactly 3 binary digits (or each hex digit into exactly 4 binary digits), then concatenate.

This works because 8 = 2³ and 16 = 2⁴: each single octal digit exactly represents 3 bits of information, and each hex digit exactly represents 4 bits, with no overlap or remainder — a convenience that does *not* exist between arbitrary bases like 7 and 13, which is why the general bridge-through-decimal method in 3.1 is still required for non-power-of-two pairs.

**Worked example:** binary `"11001010"` → hex, by grouping into 4s from the right: `1100` and `1010` → `1100` = 12 = `'C'`, `1010` = 10 = `'A'` → **`"CA"`** (matches Part 1.2's answer ✔, obtained without touching decimal at all).

---

## Part 4 — Handling Fractional Values (Non-Integer Numbers)

Everything above assumed a whole number. Converting the *fractional part* of a number (what's after a radix point) uses a mirror-image technique.

### 4.1 Fractional part: base 10 → base B (repeated multiplication)

1. Take the fractional part `f` (a value between 0 and 1).
2. Multiply `f × B`. The **integer part** of this result is the next digit (in order, left to right this time — not reversed!). The **remaining fractional part** of this result is carried forward.
3. Repeat step 2 on the new fractional part, collecting digits, until the fractional part becomes exactly 0, or until you've generated as many digits of precision as you need (some fractions never terminate in a given base, exactly like 1/3 never terminates in decimal).

**Worked example:** convert 0.625 (decimal) to binary.
- 0.625 × 2 = 1.25 → digit `1`, carry fractional part 0.25
- 0.25 × 2 = 0.5 → digit `0`, carry 0.5
- 0.5 × 2 = 1.0 → digit `1`, carry 0.0 → stop, fraction is exactly represented

Digits collected in order: `1, 0, 1` → **`0.101` in binary.**
Check: 1×(1/2) + 0×(1/4) + 1×(1/8) = 0.5+0+0.125 = 0.625 ✔.

### 4.2 Fractional part: base B → base 10 (expansion, mirrored)

Each digit after the radix point is worth a **negative** power of the base — position 1 after the point is `B^-1`, position 2 is `B^-2`, and so on. Simply sum `digit × B^-position` for every fractional digit.

**Worked example:** binary `0.101` → decimal:
1×2⁻¹ + 0×2⁻² + 1×2⁻³ = 0.5 + 0 + 0.125 = **0.625** ✔ (matches 4.1's round trip).

### 4.3 A note on non-terminating conversions

Just as 1/3 doesn't terminate in decimal (0.3333...), many "clean" decimal fractions don't terminate in other bases, and vice versa. For example, decimal 0.1 does **not** terminate in binary — it repeats forever. In manual (and real-world programmatic) conversion, you handle this by deciding on a fixed number of digits of precision to compute and then stopping, accepting the small rounding error that results.

---

## Part 5 — Handling Negative Numbers Across Bases

Exactly as in the integer/string document: strip and remember the sign first, run every algorithm above on the positive magnitude only, and reapply the sign (a leading `'-'` character, or a numeric negation) at the very end. None of the digit-extraction or digit-expansion mechanics change based on sign — sign-handling is always a separate wrapper step around the core algorithm.

---

## Part 6 — Practice by Hand

1. Convert decimal `100` to base 8. *(Expect: 100÷8=12 r4, 12÷8=1 r4, 1÷8=0 r1 → reversed "144")*
2. Convert octal `"144"` back to decimal to confirm you get 100. *(Expect: 0×8+1=1, 1×8+4=12, 12×8+4=100)*
3. Convert decimal `59` to base 2, then group the result into 3s to get base 8 directly, and check it matches converting straight from decimal to base 8.
4. Convert base 16 `"FF"` to decimal. *(Expect: 15×16+15 = 255)*
5. Convert decimal fraction `0.75` to binary. *(Expect: 0.75×2=1.5→1, 0.5×2=1.0→1, stop → "0.11")*
6. Convert base 5 `"32"` to base 3 by bridging through decimal. *(Expect: base5 "32" = 3×5+2 = 17 decimal; 17 in base 3 = 17÷3=5 r2, 5÷3=1 r2, 1÷3=0 r1 → reversed "122")*

---

## Part 7 — Cheat Sheet Summary

**Base 10 → Base B (any integer):**
Repeatedly take `remainder = N mod B` (→ next digit, right-to-left) and `N = N ÷ B`, until `N = 0`; reverse the collected digits; map remainder values ≥10 to letters A–Z.

**Base B → Base 10:**
Read digits left to right; `running_total = running_total × B + digit_value` for each digit; map letter digits A–Z back to values 10–35 first.

**Base B1 → Base B2 (general):**
Bridge through decimal: first convert B1 → decimal (accumulator method), then decimal → B2 (division/remainder method).

**Binary ↔ Octal ↔ Hex (special case):**
Skip the decimal bridge — group/expand bits in sets of 3 (for octal) or 4 (for hex), since 8 = 2³ and 16 = 2⁴.

**Fractional part, decimal → Base B:**
Repeatedly multiply the fractional part by `B`; the integer part of each result is the next digit, read left to right (no reversal needed); continue with the leftover fraction.

**Fractional part, Base B → decimal:**
Sum `digit × B^(-position)` for each digit after the radix point, position starting at 1.

**Sign handling:**
Always strip and remember the sign before converting the magnitude; reapply it to the finished result.

Every one of these procedures is built from exactly two primitive moves — dividing-with-remainder to peel a number apart, and multiplying-and-adding to build a number back up — applied consistently in whichever base you're working with.
