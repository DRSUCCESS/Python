# ...READ FILE
# ipsum_file = open('files/ipsum.txt')


# # for line in ipsum_file:
#     # print(line.rstrip())

# # ipsum_file.seek(0) # start from beginning
# # lines = ipsum_file.readlines()
# # print(lines)

# ipsum_file.seek(50) #find 50chars
# file_text = ipsum_file.read(100)
# print(file_text)

# ipsum_file.close() #must be closed


def sequence_filter(line):
    return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))