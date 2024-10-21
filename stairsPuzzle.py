def countWays(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return countWays(n - 1) + countWays(n - 2)


steps = 35
ways = countWays(steps)
print("There are " + str(ways) + " distinct ways to climb a staircase of " + str(steps) + " steps when climbing up "
                                                                                          "one or two steps at a time.")
