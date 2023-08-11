
def calcular_tn(n):
    return 2 + (n - 1) * 3

def calcular_un(n):
    return n**2 + 1

def calcular_vn(n):
    return n**2 * 10

print("Sucesión (tn):")
for n in range(1, 6):
    tn = calcular_tn(n)
    print(f"t{n} = {tn}")

print("\nSucesión (un):")
for n in range(1, 6):
    un = calcular_un(n)
    print(f"u{n} = {un}")

print("\nSucesión (vn):")
for n in range(1, 6):
    vn = calcular_vn(n)
    print(f"v{n} = {vn}")