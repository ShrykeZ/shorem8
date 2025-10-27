import math
import random
from math import gcd

def find_order(a, n, max_order=None):
    """
    Find the order r such that a^r ≡ 1 (mod n).
    This is the period-finding step of Shor's algorithm.
    
    Args:
        a: The base (must satisfy gcd(a, n) = 1)
        n: The modulus
        max_order: Maximum order to check (default: n)
    
    Returns:
        The order r, or None if not found
    """
    if max_order is None:
        max_order = n
    
    result = 1
    for r in range(1, max_order + 1):
        result = (result * a) % n
        if result == 1:
            return r
    
    return None

def shors_algorithm(n, verbose=True):
    """
    Classical simulation of Shor's factorization algorithm.
    
    This is a complete, working implementation that demonstrates
    all the key steps of Shor's algorithm without quantum computers.
    
    Args:
        n: The number to factor (must be composite and odd)
        verbose: Print detailed steps
    
    Returns:
        A tuple of factors (p, q) where n = p * q, or None if unsuccessful
    """
    if verbose:
        print("=" * 70)
        print("Shor's Algorithm - Classical Simulation")
        print("=" * 70)
        print(f"Factoring: {n}\n")
    
    # Step 1: Check if n is even
    if n % 2 == 0:
        if verbose:
            print("✓ Number is even")
            print(f"  Factors: 2 × {n // 2}")
        return (2, n // 2)
    
    if verbose:
        print("Step 1: Check if n is a perfect power")
    
    # Step 2: Check if n is a perfect power
    for k in range(2, int(math.log2(n)) + 1):
        a = round(n ** (1 / k))
        if a ** k == n:
            if verbose:
                print(f"✓ {n} = {a}^{k}")
                print(f"  Factors: {a} × {a**(k-1)}")
            return (a, a ** (k - 1))
    
    if verbose:
        print("✗ Not a perfect power\n")
        print("Step 2: Find a random number a where gcd(a, n) = 1")
    
    # Step 3: Pick a random number a < n
    max_attempts = 10
    for attempt in range(max_attempts):
        a = random.randint(2, n - 1)
        
        # Step 4: Compute gcd(a, n)
        g = gcd(a, n)
        
        if verbose:
            print(f"  Attempt {attempt + 1}: a = {a}, gcd({a}, {n}) = {g}")
        
        if g != 1:
            # We found a factor!
            if verbose:
                print(f"✓ Found factor: {g}")
                print(f"  {n} = {g} × {n // g}")
            return (g, n // g)
    
    if verbose:
        print("✗ Could not find factor via gcd\n")
        print("Step 3: Find the period r (order of a modulo n)")
    
    # Step 5: Find the order of a modulo n (period-finding step)
    # In a quantum computer, this would use Quantum Phase Estimation
    # Here we do it classically
    r = find_order(a, n)
    
    if r is None:
        if verbose:
            print("✗ Could not find order")
        return None
    
    if verbose:
        print(f"✓ Found order: {a}^{r} ≡ 1 (mod {n})\n")
        print(f"Step 4: Use the period to find factors")
        print(f"  a = {a}, r = {r}")
    
    # Step 6: If r is odd, try again
    if r % 2 == 1:
        if verbose:
            print(f"✗ Order {r} is odd, trying another a...\n")
        return shors_algorithm(n, verbose=False)
    
    if verbose:
        print(f"✓ Order is even: r = {r}\n")
        print(f"Step 5: Compute a^(r/2) mod n")
    
    # Step 7: Compute x = a^(r/2) mod n
    x = pow(a, r // 2, n)
    if verbose:
        print(f"  {a}^({r}//2) ≡ {x} (mod {n})\n")
        print(f"Step 6: Check if x ≡ ±1 (mod n)")
    
    # Step 8: Check if x ≡ -1 (mod n)
    if x == n - 1:
        if verbose:
            print(f"✗ {x} ≡ -1 (mod {n}), trying another a...\n")
        return shors_algorithm(n, verbose=False)
    
    if verbose:
        print(f"✓ {x} is not ±1 mod {n}\n")
        print(f"Step 7: Find factors using gcd")
    
    # Step 9: Compute gcd(x ± 1, n)
    factor1 = gcd(x - 1, n)
    factor2 = gcd(x + 1, n)
    
    if verbose:
        print(f"  gcd({x} - 1, {n}) = {factor1}")
        print(f"  gcd({x} + 1, {n}) = {factor2}\n")
    
    # Step 10: Check if we found nontrivial factors
    if factor1 > 1 and factor1 < n:
        if verbose:
            print("=" * 70)
            print(f"✓ Successfully factored {n}:")
            print(f"  {n} = {factor1} × {n // factor1}")
            print(f"  Verification: {factor1} × {n // factor1} = {factor1 * (n // factor1)}")
            print("=" * 70)
        return (factor1, n // factor1)
    
    if factor2 > 1 and factor2 < n:
        if verbose:
            print("=" * 70)
            print(f"✓ Successfully factored {n}:")
            print(f"  {n} = {factor2} × {n // factor2}")
            print(f"  Verification: {factor2} × {n // factor2} = {factor2 * (n // factor2)}")
            print("=" * 70)
        return (factor2, n // factor2)
    
    if verbose:
        print("✗ Could not find nontrivial factors, trying another a...\n")
    
    return shors_algorithm(n, verbose=False)

def main():
    """
    Examples of using Shor's algorithm to factor numbers.
    """
    # Example 1: Factor 15 (3 × 5)
    print("\n" + "█" * 70)
    print("Example 1: Factoring 15")
    print("█" * 70)
    shors_algorithm(15)
    
    # Example 2: Factor 21 (3 × 7)
    print("\n" + "█" * 70)
    print("Example 2: Factoring 21")
    print("█" * 70)
    shors_algorithm(21)
    
    # Example 3: Factor 35 (5 × 7)
    print("\n" + "█" * 70)
    print("Example 3: Factoring 35")
    print("█" * 70)
    shors_algorithm(35)
    
    # Example 4: Factor 91 (7 × 13)
    print("\n" + "█" * 70)
    print("Example 4: Factoring 91")
    print("█" * 70)
    shors_algorithm(91)

if __name__ == "__main__":
    main()
