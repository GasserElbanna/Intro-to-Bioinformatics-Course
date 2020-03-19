sequence = input('Enter your Sequence(Write default if you want to enter the assigned sequence)): ')

if sequence == 'default':
    sequence = 'ACAGTCGACTAGCTTGCACGTAC'

RNA_sequence = sequence.replace('T', 'U')

print('DNA Sequence:', sequence)
print('RNA Sequence:', RNA_sequence)
