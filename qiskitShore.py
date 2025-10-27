from qiskit_algorithms import Shor
from qiskit_aer import AerSimulator
from qiskit.primitives import Sampler

def factor_with_shors(n, max_attempts=10):
    """
    Use Shor's algorithm to factor a number.
    
    Args:
        n: The number to factor
        max_attempts: Maximum number of attempts to find a factor
    
    Returns:
        A tuple of factors (a, b) where n = a * b, or None if unsuccessful
    """
    print("=" * 60)
    print("Shor's Algorithm - Integer Factorization")
    print("=" * 60)
    print(f"Attempting to factor: {n}\n")
    
    # Create a simulator backend
    simulator = AerSimulator()
    
    # Create a Sampler primitive for measurement
    sampler = Sampler()
    
    # Create the Shor's algorithm instance
    shor = Shor(sampler=sampler)
    
    # Run Shor's algorithm
    try:
        result = shor.factor(N=n, a_start=2, a_step=1, max_attempts=max_attempts)
        
        print("Results:")
        print(f"  Input number: {result.N}")
        print(f"  Factors found: {result.factors}")
        print(f"  Distinct factors: {result.distinct_factors}")
        
        if result.factors:
            # Get the factors
            factors = result.factors[0]  # factors is a list of lists
            print(f"\n✓ Successfully factored {n}:")
            print(f"  {n} = {factors[0]} × {factors[1]}")
            print(f"  Verification: {factors[0]} × {factors[1]} = {factors[0] * factors[1]}")
            return tuple(factors)
        else:
            print("\n✗ No factors found")
            return None
            
    except Exception as e:
        print(f"Error during factorization: {e}")
        return None

def main():
    """
    Examples of using Shor's algorithm to factor numbers.
    """
    # Example 1: Factor 15 (3 × 5)
    print("\nExample 1: Factoring 15")
    print("-" * 60)
    factors = factor_with_shors(15, max_attempts=10)
    print()
    
    # Example 2: Factor 21 (3 × 7)
    print("\nExample 2: Factoring 21")
    print("-" * 60)
    factors = factor_with_shors(21, max_attempts=10)
    print()
    
    # Example 3: Factor 35 (5 × 7)
    print("\nExample 3: Factoring 35")
    print("-" * 60)
    factors = factor_with_shors(35, max_attempts=10)
    
    print("\n" + "=" * 60)
    print("Shor's Algorithm Examples Complete")
    print("=" * 60)

if __name__ == "__main__":
    main()
