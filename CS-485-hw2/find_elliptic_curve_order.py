
import sympy  # For prime checking
def find_order(a,b,p):
    answer = []
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        for y in range(p):
            if y**2 % p == rhs:
                answer.append((x, y))
    answer.append(0)
    print(f"the order of x^3 + {a}x + {b} mod {p} is :", len(answer))
    return answer



print(find_order(3,2,7))


def find_all_order():
    for a in range(103):
        for b in range(103):
            find_order(a,b,103)


find_all_order()


def find_order(a, b, p):
    points = []
    for x in range(p):
        rhs = (x ** 3 + a * x + b) % p
        for y in range(p):
            if (y ** 2) % p == rhs:
                points.append((x, y))
                if y != 0:  # Avoid adding the same point twice if y == 0
                    points.append((x, p - y))
    points.append('O')  # Point at infinity
    return len(set(points))  # Use a set to avoid duplicates

def find_all_order():
    p = 103
    prime_orders = []
    for a in range(p):
        for b in range(p):
            order = find_order(a, b, p)
            if sympy.isprime(order):
                prime_orders.append((order, (a, b)))
            print(f"Checking a={a}, b={b}, Order={order}")  # Debug print

    # Sort to get the largest primes and corresponding (a, b)
    prime_orders.sort(reverse=True, key=lambda x: x[0])
    return prime_orders[:10]

# Example usage
prime_curves = find_all_order()
for order, (a, b) in prime_curves:
    print(f"Order: {order}, Curve: y^2 = x^3 + {a}x + {b} mod 103")


'''
Checking a=0, b=0, Order=104
Checking a=0, b=1, Order=84
Checking a=0, b=2, Order=117
Checking a=0, b=3, Order=124
Checking a=0, b=4, Order=111
Checking a=0, b=5, Order=97
Checking a=0, b=6, Order=91
Checking a=0, b=7, Order=111
Checking a=0, b=8, Order=84
Checking a=0, b=9, Order=84
Checking a=0, b=10, Order=124
Checking a=0, b=11, Order=97
Checking a=0, b=12, Order=97
Checking a=0, b=13, Order=84
Checking a=0, b=14, Order=84
Checking a=0, b=15, Order=111
Checking a=0, b=16, Order=117
Checking a=0, b=17, Order=111
Checking a=0, b=18, Order=117
Checking a=0, b=19, Order=117
Checking a=0, b=20, Order=91
Checking a=0, b=21, Order=97
Checking a=0, b=22, Order=124
Checking a=0, b=23, Order=84
Checking a=0, b=24, Order=124
Checking a=0, b=25, Order=117
Checking a=0, b=26, Order=117
Checking a=0, b=27, Order=124
Checking a=0, b=28, Order=1
'''




def find_order(a, b, p):
    points = []
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        for y in range(p):
            if y**2 % p == rhs:
                points.append((x, y))
    order = len(points) + 1
    return order
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def find_all_order(p):
    results = []
    for a in range(p):
        for b in range(p):
            order = find_order(a, b, p)
            if is_prime(order):
                results.append((order, a, b))
    results.sort(reverse=True, key=lambda x: x[0])
    return results[:10]

p = 103
top_curves = find_all_order(p)
for curve in top_curves:
    print(f"Order: {curve[0]}, a: {curve[1]}, b: {curve[2]}")
