# excercise one
num = 1

while True:
    cube = num ** 3
    if cube > 1000:
        break
    print(cube)
    num += 1

#exercise two
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2

while len(primes) < 100:
    if is_prime(num):
        primes.append(num)
    num += 1

print(primes)

# excerise three

age = int(input("Enter your age: "))

if age < 18:
    print("Kids")
elif age >= 18 and age <= 65:
    print("Adults")
else:
    print("Seniors")
