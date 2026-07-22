dna = input("Enter DNA Sequence: ").upper()

A = 0
T = 0
G = 0
C = 0

for base in dna:
    if base == "A":
        A += 1
    elif base == "T":
        T += 1
    elif base == "G":
        G += 1
    elif base == "C":
        C += 1

print("\nDNA Analysis")
print("-" * 20)
print("A =", A)
print("T =", T)
print("G =", G)
print("C =", C)
