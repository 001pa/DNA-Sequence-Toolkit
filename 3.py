dna = input("Enter DNA Sequence: ").upper()

print("-" * 20)  

valid_bases = {"A", "T", "G", "C"}
is_valid = True


for base in dna:

    # check if base is not A,T,G,or C
    if base not in valid_bases:
        is_valid = False
        break

if is_valid and dna != "":
    print("Valid DNA Sequence")

    print("-" * 20)    
    print("\nDNA Analysis")
    print("-" * 20)

    length = len(dna)
    print(f"Length: {length}")
    print("-" * 20)
    G = 0
    C = 0

    for base in dna:
        if base == "G":
            G += 1
        elif base == "C":
            C += 1

    print(f"G Count: {G}")
    print(f"C Count: {C}")
    gc_content = ((G + C) / length) * 100
    print("GC Content:", round(gc_content,2))
else:
    print("Invalid DNA Sequence")

