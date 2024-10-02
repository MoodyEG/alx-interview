#!/usr/bin/python3
""" Who would win the prime game """


def isWinner(x, nums):
    """ Let's find out """

    # Case of no game
    if x <= 0 or nums is None:
        return None

    # Set the scores
    maria_wins = 0
    ben_wins = 0

    # Create a list with size of the highest number given
    # and fill it with 1, where  if the number is 1
    # then it is still available to be picked
    # if 0, then it is taken or can't be taken
    prime_game = [1 for x in range(sorted(nums)[-1] + 1)]

    # Mark 0 and 1 as non-prime
    prime_game[0] = 0
    prime_game[1] = 0

    # Keep only prime numbers in the list
    for num in range(2, len(prime_game)):
        for i in range(2, len(prime_game)):
            try:
                prime_game[i * num] = 0
            except IndexError:
                break

    # Count the wins, since it is always determined who to start
    for n in nums:
        # If the list is even, ben wins
        if sum(prime_game[0:n + 1]) % 2 == 0:
            ben_wins += 1

        # If the list is odd, maria wins
        else:
            maria_wins += 1

    # Return the winner
    if ben_wins > maria_wins:
        return "Ben"
    if ben_wins < maria_wins:
        return "Maria"
    return None
