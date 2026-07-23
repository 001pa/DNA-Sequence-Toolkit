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

    complement = ""

    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    reverse_complement = complement[::-1]

    print("\nDNA Analysis")
    print("-" * 20)
    print(f"Complement         : {complement}")
    print(f"Reverse Complement : {reverse_complement}")

else:
    print("Invalid DNA Sequence")

    if dna == "":
        print("Error: Input sequence cannot be empty.")
    else:
        print(f"Invalid character: {invalid_base}")