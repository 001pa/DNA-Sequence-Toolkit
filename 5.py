dna = input("Enter DNA Sequence: ").upper()

valid_bases = {"A", "T", "G", "C"}
is_valid = True
invalid_base = ""

# Validation
for base in dna:
    if base not in valid_bases:
        is_valid = False
        invalid_base = base
        break

if is_valid and dna != "":

    rna = ""
    

    for base in dna:
        if base == "A":
            rna += "U"
        elif base == "T":
            rna += "A"
        elif base == "G":
            rna += "C"
        elif base == "C":
            rna += "G"

    

    print("\nDNA Analysis")
    print("-" * 20)
    print(f"Original DNA : {dna}")
    print(f"RNA Sequence : {rna}")
    print(f"RNA Length   : {len(rna)}")
    print("-" * 20)
    

else:
    print("Invalid DNA Sequence")

    if dna == "":
        print("Error: Input sequence cannot be empty.")
    else:
        print(f"Invalid character: {invalid_base}")