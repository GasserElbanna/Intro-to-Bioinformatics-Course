import numpy as np

sequence = input('Enter your Sequence(Write default if you want to enter the assigned sequence)): ')

if sequence == 'default':
    sequence = 'ACAGTCGACTAGCTTGCACGTAC'

RNA_sequence = sequence.replace('T', 'U')
num_amino_acids = int(np.floor(len(RNA_sequence)/3))
num_bases = len(RNA_sequence) % 3
print('DNA Sequence:', sequence)
print('RNA Sequence:', RNA_sequence)
print('Number of Amino Acids =', num_amino_acids)
print('Number of Bases not forming Amino Acid =', num_bases)
