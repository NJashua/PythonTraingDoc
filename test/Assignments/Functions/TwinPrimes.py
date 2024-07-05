def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False 
        return True
    
def generate_twin_primes(start, end):
    for i in range(start, end):
        j = i + 2
        if (is_prime(i) and is_prime(j)):
            print(f"twin primes are {i} - {j}")

generate_twin_primes(2, 1000)
