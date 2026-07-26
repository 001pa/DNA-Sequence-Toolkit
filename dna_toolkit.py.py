def validate_dna(dna):

    valid_bases = {"A", "T", "G", "C"}

    if dna == "":
        return False

    for base in dna:

        if base not in valid_bases:
            return False

    return True


def reverse_complement(dna):

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    complement_list = [complement[base] for base in dna]
    complement_str = "".join(complement_list)

    reverse = complement_str[::-1]

    return reverse


def gc_content(dna):

    if not dna:
        return 0

    G = 0
    C = 0

    for base in dna:

        if base == "G":
            G += 1

        elif base == "C":
            C += 1

    gc_count = G + C
    length = len(dna)

    gc_percentage = (gc_count / length) * 100

    return round(gc_percentage, 2)


def transcribe_rna(dna):

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

    return rna


def read_fasta(filename):

    with open(filename, "r") as file:

        lines = file.read().splitlines()

    header = lines[0][1:]

    sequence = ""

    for line in lines[1:]:
        sequence += line

    return header, sequence

codon_table = {
    # Phenylalanine
    "TTT": "F", "TTC": "F",

    # Leucine
    "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L",
    "CTA": "L", "CTG": "L",

    # Isoleucine
    "ATT": "I", "ATC": "I", "ATA": "I",

    # Methionine (Start)
    "ATG": "M",

    # Valine
    "GTT": "V", "GTC": "V",
    "GTA": "V", "GTG": "V",

    # Serine
    "TCT": "S", "TCC": "S",
    "TCA": "S", "TCG": "S",
    "AGT": "S", "AGC": "S",

    # Proline
    "CCT": "P", "CCC": "P",
    "CCA": "P", "CCG": "P",

    # Threonine
    "ACT": "T", "ACC": "T",
    "ACA": "T", "ACG": "T",

    # Alanine
    "GCT": "A", "GCC": "A",
    "GCA": "A", "GCG": "A",

    # Tyrosine
    "TAT": "Y", "TAC": "Y",

    # Histidine
    "CAT": "H", "CAC": "H",

    # Glutamine
    "CAA": "Q", "CAG": "Q",

    # Asparagine
    "AAT": "N", "AAC": "N",

    # Lysine
    "AAA": "K", "AAG": "K",

    # Aspartic Acid
    "GAT": "D", "GAC": "D",

    # Glutamic Acid
    "GAA": "E", "GAG": "E",

    # Cysteine
    "TGT": "C", "TGC": "C",

    # Tryptophan
    "TGG": "W",

    # Arginine
    "CGT": "R", "CGC": "R",
    "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",

    # Glycine
    "GGT": "G", "GGC": "G",
    "GGA": "G", "GGG": "G",

    # Stop Codons
    "TAA": "STOP",
    "TAG": "STOP",
    "TGA": "STOP"
} 

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


def show_menu():

    print("=" * 30)
    print("     DNA Sequence Toolkit")
    print("=" * 30)
    print("1. Validate DNA")
    print("2. Reverse Complement")
    print("3. GC Content")
    print("4. RNA Transcription")
    print("5. DNA Translation")
    print("6. Load DNA from FASTA File")
    print("7. Exit")


while True:

    show_menu()

    choice = input("Choose an option: ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Invalid Choice")
        continue

    # ---------- FASTA ----------
    if choice == "6":

        filename = input("Enter FASTA filename: ")

        try:
            header, dna = read_fasta(filename)
            dna = dna.upper()

            if not validate_dna(dna):
                print("Invalid DNA sequence found in FASTA file.")
                continue

            print("\nFASTA Loaded Successfully")
            print(f"Header   : {header}")
            print(f"Sequence : {dna}")

        except FileNotFoundError:
            print("File not found.")

        continue

    # ---------- Manual DNA ----------
    dna = input("Enter DNA Sequence: ").upper()

    if not validate_dna(dna):
        print("Invalid DNA Sequence")
        continue

    if choice == "1":
        print("Valid DNA Sequence")

    elif choice == "2":
        print(f"Reverse Complement: {reverse_complement(dna)}")

    elif choice == "3":
        print(f"GC Content: {gc_content(dna)}%")

    elif choice == "4":
        print(f"RNA Sequence: {transcribe_rna(dna)}")

    elif choice == "5":
        print("Protein:", translate_dna(dna))


print("Program Ended")