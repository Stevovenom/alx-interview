#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers rep the upper bounds for each round.

    Returns:
        str or None: Name of player with most wins
        ("Maria" or "Ben"), or None if it's a tie.
    """
    if x <= 0 or not nums:
        return None

    # Find the maximum number in nums for sieve precomputation
    max_num = max(nums)

    # Step 1: Precompute primes using the Sieve of Eratosthenes
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False

    # Step 2: Precompute the number of primes up to each number
    primes_up_to = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_up_to[i] = primes_up_to[i - 1] + (1 if is_prime[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If primes_up_to[n] is odd, Maria wins; if even, Ben wins
        if primes_up_to[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
