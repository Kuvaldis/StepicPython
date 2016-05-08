import itertools


def primes():
    current = 1
    prevs = []
    while True:
        current += 1
        isPrime = True
        for prev in prevs:
            if current % prev == 0:
                isPrime = False
                break
        if isPrime:
            prevs.append(current)
            yield current


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
