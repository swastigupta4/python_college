def sieve_of_eratosthenes(limit):
    # Create a boolean array "prime[0..limit]" and initialize all entries as True.
    prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        # If prime[p] is still True, then it is a prime
        if prime[p]:
            # Update all multiples of p as False
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    
    # Sum all prime numbers
    prime_sum = sum(p for p in range(2, limit) if prime[p])
    return prime_sum

# Take input from the user
limit = int(input("Enter a number to find the sum of all primes below it: "))

# Get the sum of primes below the limit
sum_of_primes = sieve_of_eratosthenes(limit)

# Print the result
print(f"The sum of all primes below {limit} is: {sum_of_primes}")
