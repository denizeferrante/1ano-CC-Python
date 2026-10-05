t = ('a', 'b', 'c')
print(t[0])

# ATRIBUIÇÃO DE TUPLAS
a = 5
b = 10
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")
print()

email = "fulano@gmail.com"
usuario, dominio = email.split("@")

print(usuario)
print(dominio)
