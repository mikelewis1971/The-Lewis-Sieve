import pandas as pd
import math
from sympy import primerange,isprime  # Removed isprime and concurrent.futures

# Expand pandas output to see all rows/columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


class LewisSieveFullAnalysis:
    def __init__(self, number):
        """Initialize with the base number and set up the sieve with recursive propagation."""
        self.base_number = number  # Starting point for factorization
        self.window_size = int(math.sqrt(number)) * 2  # Window size
        self.lower_bound = self.base_number - self.window_size
        self.upper_bound = self.base_number + self.window_size
        self.propagation_map = {}  # Stores numbers and their discovered factors
        self.reduced_map = {}  # Stores numbers after full reduction
        self.missing_numbers = []  # Numbers that never got any factors
        self.processed_numbers = set()  # Track numbers already processed in recursion
        # Precompute a list of small primes for trial division
        self.primes_to_test = list(primerange(2, self.window_size))

    def fully_reduce(self, num, factor):
        """Repeatedly divide num by factor until it no longer divides evenly."""
        while num % factor == 0 and num != factor:
            num //= factor
        return num

    def propagate_factors(self, number, factors):
        """
        For each factor, propagate it to every multiple in the window.
        This 'labels' numbers with the factors discovered.
        """
        for factor in factors:
            for num in range(number, self.upper_bound + 1, factor):
                if num not in self.propagation_map:
                    self.propagation_map[num] = set()
                self.propagation_map[num].add(str(factor))

    def peel_off_primes(self):
        """Single-threaded trial division over the entire window."""
        for num in range(self.lower_bound, self.upper_bound + 1):
            found_factors = set()
            for prime in self.primes_to_test:
                if num % prime == 0:
                    found_factors.add(prime)
            if found_factors:
                self.propagation_map[num] = found_factors

    def multiply_and_reduce(self):
        """Using the discovered factors, fully reduce each number in the propagation map."""
        for num, factors in self.propagation_map.items():
            reduced_num = num
            for factor in sorted(map(int, factors)):
                reduced_num = self.fully_reduce(reduced_num, factor)
            self.reduced_map[num] = reduced_num

    def find_missing_numbers(self):
        """Identify numbers in the window that never appeared in the propagation map."""
        found_numbers = set(self.propagation_map.keys())
        all_numbers_in_window = set(range(self.lower_bound, self.upper_bound + 1))
        self.missing_numbers = sorted(all_numbers_in_window - found_numbers)

    def recursive_propagation(self):
        """
        For each missing number, try to factor it using trial division.
        If factors are found, propagate them into the window.
        This recursive loop continues until no new factors are discovered.
        """
        new_factors = True
        while new_factors:
            new_factors = False
            # Update the list of missing numbers
            self.find_missing_numbers()
            for num in self.missing_numbers.copy():
                if num not in self.processed_numbers:
                    self.processed_numbers.add(num)
                    factors = []
                    n = num
                    for prime in self.primes_to_test:
                        if n % prime == 0:
                            while n % prime == 0:
                                factors.append(prime)
                                n //= prime
                        if n == 1:
                            break
                    if factors:
                        self.propagate_factors(num, factors)
                        new_factors = True

    def run_sieve(self):
        """Run the full sieve, then output the derived data and missing numbers."""
        # Step 1: Single-threaded factorization of the window
        self.peel_off_primes()

        # Step 2: Use the discovered factors to reduce numbers
        self.multiply_and_reduce()

        # Step 3: Identify numbers that were not hit initially
        self.find_missing_numbers()

        # Step 4: Recursively try to factor missing numbers and propagate any factors found
        self.recursive_propagation()

        # Format the derived propagation data
        formatted_data = []
        for idx, (num, factors) in enumerate(sorted(self.propagation_map.items())):
            factor_list = ", ".join(sorted(map(str, factors))) if factors else "N/A"
            reduced_value = self.reduced_map.get(num, num)
            formatted_data.append({
                "Index": idx + 1,
                "Original Number": num,
                "Factors": factor_list,
                "Reduced Number": reduced_value
            })

        # Build DataFrames for the output
        df_formatted = pd.DataFrame(formatted_data, columns=["Index", "Original Number", "Factors", "Reduced Number"])
        df_missing = pd.DataFrame({"Missing Numbers": self.missing_numbers})

        print("Formatted Lewis Sieve Output:")
        print(df_formatted)
        print("\nNumbers Not in Derived List (Missing Numbers):")
        print(self.missing_numbers)
        count = 0
        for x in self.missing_numbers:
            if isprime(x):
                count+=0
            else:
                count+=1
        print(f"Missing Number that are not Prime: {count}")


# Run the sieve on 3252 (you can change this value as needed)
sieve = LewisSieveFullAnalysis(20123)
sieve.run_sieve()
