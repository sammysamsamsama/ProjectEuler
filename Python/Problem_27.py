from Problem_26 import is_prime

max_primes_generated = 0
max_a = 0
max_b = 0
for a in range(-999, 999, 2):
    for b in range(-1000, 1000):
        if not is_prime(abs(b)):
            continue
        primes_generated = 0
        n = 0
        while is_prime(n ** 2 + a * n + b):
            primes_generated += 1
            n += 1
        if primes_generated > max_primes_generated:
            max_primes_generated = primes_generated
            max_a = a
            max_b = b
        if primes_generated > 10:
            print("n**2 + " + str(a) + "n + " + str(b))
            print(primes_generated)
print(max_primes_generated, max_a, max_b, max_a*max_b)
