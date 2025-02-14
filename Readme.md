
# Lewis Sieve Full Analysis Teaching Aid

## 1. Introduction

The Lewis Sieve is a custom, interactive tool designed to help you understand factorization and the idea behind sieve algorithms (like the Sieve of Eratosthenes). Instead of only identifying primes, this program digs deeper: it identifies factors of numbers in a specific range, propagates these factors to related numbers, and then reduces numbers by removing all of their small factors.

**What you’ll learn:**
- How a window of numbers is defined and why.
- The process of trial division using small primes.
- How “propagation” of factors helps mark composites.
- How recursive checks catch any factors that might have been initially missed.
- How to interpret the final output in terms of factorization.

---

## 2. Concept Overview

### 2.1. Defining the Window
- **Base Number:** The central number around which you want to explore factors.
- **Window Size:**  
  The window is set from:
  \[
  \text{base\_number} - 2\sqrt{\text{base\_number}} \quad \text{to} \quad \text{base\_number} + 2\sqrt{\text{base\_number}}
  \]
  This design ensures that even for the largest number in the window, every factor up to its square root (a necessary condition for composite numbers) is within the range.

### 2.2. Initial Factorization
- **Trial Division:**  
  The program tests every number in the window against a list of small primes (all primes up to the window size).  
  - **Purpose:** Identify the basic building blocks (factors) of each number.

### 2.3. Factor Propagation
- **Propagation:**  
  When a factor is found for a number, the algorithm “spreads” that factor to all multiples of that factor within the window.  
  - **Idea:** Much like the Sieve of Eratosthenes marks off multiples of a prime, here the factor information is recorded for related numbers.  
  - **Result:** It becomes easier to recognize composite numbers and their factors later in the process.

### 2.4. Fully Reducing Numbers
- **Reduction:**  
  Once the factors for a number are identified, the number is “fully reduced” by repeatedly dividing by each factor until no further division is possible.
  - **Why?** This helps simplify the number to its “core” form, revealing whether it’s completely factored or if some composite structure remains.

### 2.5. Recursive Propagation
- **Revisiting Missing Numbers:**  
  Some numbers might not show any factors in the initial pass. These “missing numbers” are revisited using additional trial division.
  - **Outcome:** This recursive step helps catch any factors that were initially overlooked, reinforcing the concept that thorough factorization sometimes needs multiple passes.

---

## 3. Code Structure & Walkthrough

### 3.1. Class and Attributes
- **Class:** `LewisSieveFullAnalysis`
  - **base_number:** The central number to analyze.
  - **window_size:** Calculated as \(2 \times \sqrt{\text{base\_number}}\), it defines the range around the base number.
  - **lower_bound/upper_bound:** Set from `base_number - window_size` to `base_number + window_size`.
  - **propagation_map:** A dictionary to record each number and its discovered factors.
  - **reduced_map:** A dictionary that will hold the “reduced” (fully factored) version of each number.
  - **missing_numbers:** A list for numbers that didn’t initially get any factors.
  - **processed_numbers:** Helps track which numbers have been processed during the recursive stage.
  - **primes_to_test:** A list of small primes (generated using `sympy.primerange`) to use in trial division.

### 3.2. Key Methods Explained

#### 3.2.1. `fully_reduce(num, factor)`
- **Purpose:** Continuously divide the number by the given factor until it no longer divides evenly.
- **Teaching Point:** Understand how repeatedly dividing by a prime “strips away” its contribution, similar to peeling layers off an onion.

#### 3.2.2. `propagate_factors(number, factors)`
- **Purpose:** Once you find a factor for a number, “mark” every multiple of that factor within the window.
- **Teaching Point:** This mimics the idea behind classical sieves and shows how one piece of information (a factor) can inform the analysis of many numbers.

#### 3.2.3. `peel_off_primes()`
- **Purpose:** Perform an initial pass of trial division for every number in the window.
- **Teaching Point:** Demonstrates how simple divisibility tests can identify potential factors and begin the factorization process.

#### 3.2.4. `multiply_and_reduce()`
- **Purpose:** Using the factors from the propagation map, reduce each number to a simpler form.
- **Teaching Point:** Highlights the concept of fully factoring a number by removing all instances of its discovered factors.

#### 3.2.5. `find_missing_numbers()`
- **Purpose:** Identify numbers in the window that weren’t “hit” by any factor propagation.
- **Teaching Point:** Learn about the special role of primes and stubborn composites that might initially escape factor detection.

#### 3.2.6. `recursive_propagation()`
- **Purpose:** Re-examine the missing numbers using additional trial division. If any new factors are found, they’re propagated.
- **Teaching Point:** Understand that sometimes a single pass is not enough and how iterative refinement helps ensure completeness.

#### 3.2.7. `run_sieve()`
- **Purpose:** The master method that calls all other methods in sequence:
  1. Initial trial division (`peel_off_primes`).
  2. Factor propagation and number reduction (`multiply_and_reduce`).
  3. Identification of missing numbers (`find_missing_numbers`).
  4. Recursive propagation to catch any overlooked factors.
- **Output:**  
  - A formatted table (using pandas DataFrame) listing:
    - Original numbers
    - Their discovered factors
    - Their fully reduced forms  
  - A list of missing numbers with an indication of which might be composite.

---

## 4. Running the Program

### 4.1. Prerequisites
Ensure you have the following Python packages installed:
- **pandas**
- **sympy**

Install them via:
```bash
pip install pandas sympy
```

### 4.2. Execution
1. Save the code in a file (e.g., `lewis_sieve.py`).
2. Run the file:
   ```bash
   python lewis_sieve.py
   ```
3. The program by default uses a base number (e.g., 20123) but you can modify this value in the instantiation:
   ```python
   sieve = LewisSieveFullAnalysis(20123)
   ```

---

## 5. Teaching Points Recap

- **Window Selection:**  
  The window ensures that any composite number’s factors (up to its square root) are considered, illustrating why trial division works.

- **Factor Propagation:**  
  Propagating factors teaches you how knowing one factor can help quickly identify many composites, a strategy inspired by classical sieves.

- **Iterative Reduction and Recursion:**  
  The repeated reduction of numbers and recursive checks demonstrate that factorization can be an iterative process—a key idea in many numerical algorithms.

- **Practical Application:**  
  While the code is “clunky,” it is intentionally written as a learning tool to make these concepts clear. Experimenting with the code, changing parameters, and examining the output can deepen your understanding of both prime sieves and factorization methods.

---

## 6. Final Thoughts

This teaching aid is meant to be a starting point for exploring factorization algorithms. Use it to:
- Visualize how factors are detected and spread.
- Experiment with different base numbers and window sizes.
- Enhance your understanding of classical concepts through modern Python code.

Happy learning and exploring the fascinating world of numbers!

---
