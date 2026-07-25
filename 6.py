def translate_dna(dna):
    protein = ""
    for i in range (0, len(dna), 3):
        codon = dna[i:i+3]

        if len(codon) < 3:
            print(f"Warning: Incomplete codon '{codon}' ignored.")
            break
        amino_acid = codon_table.get(codon)
        if amino_acid is None:
            print("Unkown codon:", codon)
            break

        if amino_acid == "STOP":
            break

        protein += amino_acid
    return protein