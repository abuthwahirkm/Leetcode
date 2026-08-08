# LeetCode 520 - Detect Capital

## 🧩 Problem

Given a string `word`, return `True` if the usage of capital letters in it is correct.

Capitalization is considered correct if one of the following conditions is satisfied:

1. All letters are uppercase.
   - Example: `USA`
2. All letters are lowercase.
   - Example: `leetcode`
3. Only the first letter is uppercase.
   - Example: `Google`

Otherwise, return `False`.

---

## 💡 Examples

### Example 1

**Input:**
```text
word = "USA"
```

**Output:**
```text
True
```

All letters are uppercase, so the capitalization is correct.

### Example 2

**Input:**
```text
word = "FlaG"
```

**Output:**
```text
False
```

The capitalization does not follow any of the three valid patterns.

### Example 3

**Input:**
```text
word = "Google"
```

**Output:**
```text
True
```

Only the first letter is uppercase.

---

## 🧠 Approach

I solved this problem using Python's built-in string methods.

### `isupper()`

```python
word.isupper()
```

Returns `True` if all letters in the word are uppercase.

Example:

```python
"USA".isupper()
```

Output:

```text
True
```

### `islower()`

```python
word.islower()
```

Returns `True` if all letters in the word are lowercase.

Example:

```python
"leetcode".islower()
```

Output:

```text
True
```

### `istitle()`

```python
word.istitle()
```

Returns `True` when the word follows title-case capitalization, such as having the first letter uppercase and the remaining letters lowercase.

Example:

```python
"Google".istitle()
```

Output:

```text
True
```

---

## 🔑 Logic

There are only three valid capitalization patterns:

```text
1. ALL UPPERCASE
2. all lowercase
3. First letter uppercase
```

So I check whether the word satisfies **any one** of these conditions:

```python
word.isupper() or word.islower() or word.istitle()
```

The `or` operator returns `True` if at least one condition is `True`.

If all three conditions are `False`, the answer is `False`.

---

## 💻 Solution

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
```

---

## 🔍 Dry Run

### Case 1: `word = "USA"`

```python
word.isupper()   # True
word.islower()   # False
word.istitle()   # False
```

So:

```text
True or False or False
```

Result:

```text
True
```

---

### Case 2: `word = "leetcode"`

```python
word.isupper()   # False
word.islower()   # True
word.istitle()   # False
```

So:

```text
False or True or False
```

Result:

```text
True
```

---

### Case 3: `word = "Google"`

```python
word.isupper()   # False
word.islower()   # False
word.istitle()   # True
```

So:

```text
False or False or True
```

Result:

```text
True
```

---

### Case 4: `word = "FlaG"`

```python
word.isupper()   # False
word.islower()   # False
word.istitle()   # False
```

So:

```text
False or False or False
```

Result:

```text
False
```

---

## ⏱️ Complexity Analysis

### Time Complexity

```text
O(n)
```

where `n` is the length of the word.

The string methods examine the characters of the word.

### Space Complexity

```text
O(1)
```

No additional data structure is used.

---

## 📚 Python Concepts Used

- String methods
- `isupper()`
- `islower()`
- `istitle()`
- Boolean expressions
- `or` operator
- Return statements

---

## 🎯 Key Takeaway

Instead of manually checking every character, Python's built-in string methods make the solution simple and readable.

The main idea is:

```python
return word.isupper() or word.islower() or word.istitle()
```

### Valid Patterns

```text
USA       → All uppercase      → True
leetcode  → All lowercase      → True
Google    → First letter upper  → True
FlaG      → Invalid pattern     → False
```

---

## 🚀 What I Learned

- How to check uppercase and lowercase strings in Python.
- How `isupper()` works.
- How `islower()` works.
- How `istitle()` works.
- How to combine multiple conditions using `or`.
- How built-in Python methods can make a solution shorter and cleaner.
- How to analyze time and space complexity.

---

## 🔗 Problem

**LeetCode:** 520. Detect Capital

**Difficulty:** Easy

**Language:** Python 3
