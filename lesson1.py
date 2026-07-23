dna = input("Enter DNA Sequence: ").upper()

valid_bases = {"A","T","G","C"}
is_valid = True

for base in dna:

    # check if base is not A,T,G,or C
    if base not in valid_bases:
        is_valid = False
        break

if is_valid and dna != "":
    print("Valid DNA Sequence")
else:
    print("Invalid DNA Sequence")