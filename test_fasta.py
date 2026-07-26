with open("sample.fasta", "r") as file:
    content = file.read()

lines = content.splitlines()

header = lines[0][1:]
sequence = lines[1]

print(header)
print(sequence)