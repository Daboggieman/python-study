# Integer ↔ String Conversion — A Manual Walkthrough

This is a from-scratch conceptual lecture on how to convert an integer to a string and a string back to an integer, **without using any built-in conversion function**. The goal is that you understand the mechanics well enough to implement it yourself in any language, from first principles.

---

## Part 0 — The Core Insight You Need First

A computer stores an integer as a *number* (a binary value in memory/registers). A string is a *sequence of characters*, and characters like `'0'` through `'9'` are themselves just numbers under the hood (their character codes), which happen to sit **consecutively** in every common encoding (ASCII, UTF-8, Unicode Basic Latin block):

```
'0' → 48
'1' → 49
'2' → 50
...
'9' → 57
```

Because they are consecutive, there is a beautifully simple relationship:

> **digit_character = digit_value + code_of('0')**
> **digit_value = digit_character − code_of('0')**

Every technique below is built entirely on this one fact, plus basic arithmetic (division, remainder/modulo, multiplication, addition).

You do **not** need to memorize the number 48. You only need to know that `'0'` is a character whose code is some fixed number, and every digit character after it increases by exactly 1 per digit. Subtracting `'0'` from any digit character gives you its numeric value; adding a digit value to `'0'` gives you back the character.

---

## Part 1 — Converting an Integer → a String

### 1.1 The core idea: peel off digits from the *right* using division and remainder

Take the number `4930`. Ask yourself: "What is the last digit of this number?" You get the last digit of any base-10 integer by taking it **modulo 10** (remainder after dividing by 10):

```
4930 mod 10 = 0     ← this is the last digit
```

Now remove that last digit from the number by doing **integer division by 10** (division that drops the remainder/fraction):

```
4930 ÷ 10 = 493     ← the number with its last digit chopped off
```

Repeat this process on `493`:

```
493 mod 10 = 3      ← next digit (second-to-last of the original number)
493 ÷ 10 = 49
```

Repeat on `49`:

```
49 mod 10 = 9
49 ÷ 10 = 4
```

Repeat on `4`:

```
4 mod 10 = 4
4 ÷ 10 = 0          ← once the quotient hits 0, you are done
```

### 1.2 What you just produced

Collecting the digits **in the order you extracted them**, you got: `0, 3, 9, 4`.

Notice this is **backwards** — you pulled the *last* digit first, because modulo/division-by-10 always exposes the rightmost digit. The original number reads `4930`, but you extracted `0, 3, 9, 4`.

This is the single most important thing to internalize about integer→string conversion: **the digits come out in reverse order**, and you must reverse them at the end (or build the string by prepending instead of appending — see 1.4).

### 1.3 Turning each digit value into a digit character

For each numeric digit you extracted (0, 3, 9, 4), convert it to a character using the formula from Part 0:

```
digit_character = digit_value + code_of('0')
```

So `0 → '0'`, `3 → '3'`, `9 → '9'`, `4 → '4'`. (In this base-10 case the character looks trivially like the digit, but this same formula is what lets you handle any base later — see the companion document on base conversion for digits beyond 9.)

### 1.4 Assembling the final string — two valid strategies

**Strategy A: Collect then reverse.**
Push each character onto the *end* of a growing sequence as you extract it, so you build `"0","3","9","4"`, then reverse the whole sequence at the end to get `"4930"`.

**Strategy B: Prepend instead of append.**
Instead of adding each new character to the end, add it to the *front* of the growing string each time. First iteration: string is `"0"`. Second: `"30"`. Third: `"930"`. Fourth: `"4930"`. This avoids a separate reversal step, at the cost of prepend being a slightly less common/less efficient string operation.

Either is correct. Pick whichever fits the tools you have.

### 1.5 The zero edge case

If the input integer is exactly `0`, the loop above ("divide until quotient is 0") never executes even once, because the number is *already* 0 before you start — so a naive loop that says "while number is not 0, extract a digit" would produce an **empty string**, which is wrong. `0` should become the string `"0"`.

**Fix:** special-case it. Before running the loop, check: if the input is 0, the answer is just the single character `'0'`, and you stop there. This is the single most common bug in manual integer-to-string code.

### 1.6 Handling negative numbers

Negative numbers need one extra step:

1. Remember the sign separately (a simple true/false "was this negative?" flag) before you do any digit extraction.
2. Convert the *magnitude* (the absolute value, i.e. the number with the sign stripped) using the exact process above. Note: modulo and integer division on a negative number can behave inconsistently across systems (some give negative remainders), which is precisely why you strip the sign first and work with a positive number throughout.
3. Once you have the digit string for the magnitude, if the original number was negative, place a `'-'` character at the very front of the final string.

Worked example: `-407`
- Flag: negative = true
- Work with magnitude `407`
- `407 mod 10 = 7`, `407 ÷ 10 = 40`
- `40 mod 10 = 0`, `40 ÷ 10 = 4`
- `4 mod 10 = 4`, `4 ÷ 10 = 0` → stop
- Extracted in order: `7, 0, 4` → reversed: `4, 0, 7` → `"407"`
- Prepend the sign: `"-407"`

### 1.7 Full worked trace (positive number), step by step

Convert `2049` to a string.

| Step | Current number | number mod 10 (digit) | number ÷ 10 (new number) | Digits collected so far (extraction order) |
|---|---|---|---|---|
| 1 | 2049 | 9 | 204 | 9 |
| 2 | 204 | 4 | 20 | 9, 4 |
| 3 | 20 | 0 | 2 | 9, 4, 0 |
| 4 | 2 | 2 | 0 → stop | 9, 4, 0, 2 |

Reverse `9,4,0,2` → `2,0,4,9` → convert each digit value to a character → `"2049"`. ✔

### 1.8 Why this works in *any* base, not just base 10

Nothing about this method is special to base 10 except the number `10` itself. If you replace "mod 10" and "÷ 10" with "mod B" and "÷ B" for some other base `B`, you get exactly the digit-extraction half of general base conversion — this is the bridge to the companion document, "base convert to and from."

---

## Part 2 — Converting a String → an Integer

Now go the other direction: given a string like `"4930"`, reconstruct the integer `4930` using only character inspection and arithmetic.

### 2.1 The core idea: build up the number from *left to right*, one digit at a time

Unlike integer→string (which naturally works right-to-left because of how modulo/division expose digits), string→integer works most naturally **left to right**, because that's the order the characters already appear in.

The trick is called an **accumulator pattern**. You keep a running total, initialized to 0. For each character in the string, from left to right, you do:

```
running_total = running_total × 10 + digit_value_of(current_character)
```

Why multiply by 10 each time? Because every time you read one more digit, every digit you've already accumulated shifts one place to the left (its place value gets ten times bigger) to make room for the new digit in the ones place. Multiplying the whole accumulator by 10 performs that shift for you, all at once, for every digit already in there.

### 2.2 Getting the digit value from a digit character

Use the inverse of the Part 0 formula:

```
digit_value = digit_character − code_of('0')
```

### 2.3 Full worked trace

Convert the string `"4930"` to an integer.

| Step | Character read | digit_value | Calculation | running_total after this step |
|---|---|---|---|---|
| start | — | — | — | 0 |
| 1 | `'4'` | 4 | 0×10 + 4 | 4 |
| 2 | `'9'` | 9 | 4×10 + 9 | 49 |
| 3 | `'3'` | 3 | 49×10 + 3 | 493 |
| 4 | `'0'` | 0 | 493×10 + 0 | 4930 |

Final result: `4930`. ✔ Notice this reconstructs the exact number, and — pleasantly — you never needed to reverse anything, because you're reading the string in its natural left-to-right order and each step correctly re-weights everything accumulated so far.

### 2.4 Handling a leading sign

Before starting the accumulator loop:

1. Look at the very first character of the string.
2. If it is `'-'`, remember "this is negative" and start your digit-reading loop from the *second* character onward (skip the sign character itself).
3. If it is `'+'`, similarly just skip it (it doesn't change the sign) and start reading digits from the second character.
4. Otherwise, there is no sign character — start reading digits from the very first character.

After the loop finishes and you have the final `running_total`, negate it (multiply by −1) if you recorded that the string was negative.

### 2.5 Handling invalid or unexpected characters

A robust manual parser should decide, up front, what counts as a valid digit character: only `'0'` through `'9'` (i.e., `digit_value` computed via subtraction from `'0'` must land in the range 0–9). If you encounter:
- **Leading/trailing whitespace** — typically you'd trim/skip whitespace before and after the digits before parsing begins.
- **Any character outside `'0'`–`'9'`** (other than a single leading sign) — this means the string isn't a valid integer. A careful implementation should stop and signal an error (rather than silently producing a wrong number) as soon as it meets such a character.
- **An empty string, or a string that is only a sign with no digits** — also invalid; there's nothing to accumulate.

### 2.6 Overflow — a real manual-conversion concern

Integers stored in a fixed-size register (e.g., 32-bit or 64-bit) have a maximum representable magnitude. Because your accumulator keeps growing (`running_total × 10 + digit`), a long enough digit string will eventually produce a value larger than the maximum the integer type can hold, wrapping around or corrupting the result depending on the system.

A careful manual implementation checks, **before** each multiply-and-add step, whether the operation would exceed the known maximum (or minimum, for negative numbers) for the integer type in use, and stops with an overflow error rather than silently producing garbage. This check is typically done by comparing the current `running_total` against `(max_value − digit_value) ÷ 10`-style bounds *before* performing the multiplication, so you detect the problem before it happens rather than after.

### 2.7 Full worked trace with a sign

Convert `"-286"` to an integer.

1. First character is `'-'` → remember negative = true; begin reading from index 1 (`"286"`).
2. `running_total = 0×10 + 2 = 2`
3. `running_total = 2×10 + 8 = 28`
4. `running_total = 28×10 + 6 = 286`
5. Apply the sign: since negative = true, final result = `−286`. ✔

---

## Part 3 — Practice by Hand (no tools, just paper)

Try tracing these yourself using the tables above as a template before checking the "expected" line.

1. Integer → String: convert `705` to a string.
   *(Expect: extract 5, 0, 7 in that order → reverse → "705")*
2. Integer → String: convert `0` to a string.
   *(Expect: the zero special case → "0")*
3. Integer → String: convert `-19` to a string.
   *(Expect: sign flag set, magnitude 19 → extract 9, 1 → reverse → "19" → prepend "-" → "-19")*
4. String → Integer: convert `"501"` to an integer.
   *(Expect: 0→5→50→501)*
5. String → Integer: convert `"+42"` to an integer.
   *(Expect: skip '+', 0→4→42)*
6. String → Integer: convert `"7a3"` and explain why it should be rejected.
   *(Expect: 'a' is not in '0'-'9', so this is an invalid integer string.)*

---

## Part 4 — Cheat Sheet Summary

**Integer → String**
1. If the number is 0, return `"0"` immediately (special case).
2. Remember and strip the sign; work with the positive magnitude from here on.
3. Loop: `digit = number mod base`, `number = number ÷ base` (integer division), converting each `digit` to a character via `digit + code_of('0')`, collecting digits in extraction order.
4. Stop when `number` becomes 0.
5. Reverse the collected characters (or build by prepending instead of appending).
6. If the original was negative, prepend `'-'`.

**String → Integer**
1. Skip/trim any surrounding whitespace.
2. Check for a leading `'+'` or `'-'`; remember the sign, and skip that character.
3. Initialize `running_total = 0`.
4. For each remaining character, left to right: confirm it's a valid digit character, compute `digit_value = character − code_of('0')`, then `running_total = running_total × base + digit_value`. Check for overflow before each step if working with a fixed-size integer type.
5. Apply the remembered sign to `running_total` at the end.

These two algorithms are mirror images of each other: one *decomposes* a number right-to-left using division/modulo, the other *reconstructs* a number left-to-right using multiplication/addition. Understanding them as inverses of each other is the fastest way to remember both permanently.
