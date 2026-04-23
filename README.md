# Formal-Languages-Failure-Function

Implementation of the failure function for token recognition, based on Aho's Compilers book.

This repository contains a Python implementation of the failure function algorithm (Section 3.4.5 of Compilers: Principles, Techniques, & Tools). It computes the longest proper prefix that is also a suffix for keyword pattern matching during lexical analysis.

# Assignment 1: Failure Function Implementation

## Environment and Tools
* **Operating System:** Windows 10 / Linux Ubuntu (You can adjust this to your actual OS)
* **Programming Language:** Python 3.10
* **Tools Used:** Visual Studio Code, Terminal

## How to Run the Program
1. Make sure you have Python 3 installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `failure_function.py` file is located.
4. Run the script using the following command:
   ```bash
   python failure_function.py

## Explanation of the algorithm
The algorithm computes the values dynamically in a single pass. It initializes a pointer t to keep track of the length of the current matching prefix. As it iterates through the keyword with a pointer s, it checks if the current character b[s] matches the character b[t]. If they match, the matching sequence grows, and f(s) stores the new length. If there is a mismatch, the algorithm uses previously computed values f(t) to safely fall back to the next longest possible matching prefix, preventing redundant comparisons.

Sincerely,

Juan Esteban Torres Peña

Mateo Duque Restrepo
