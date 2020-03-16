sequence = input('Enter your Sequence(Write default if you want to enter the assigned sequence)): ')

if sequence == 'default':
    sequence = 'ACAGTCGACTAGCTTGCACGTAC'

C_Percentage = (sequence.count('C')/len(sequence))*100
G_Percentage = (sequence.count('G')/len(sequence))*100
CG_Percentage = ((sequence.count('C')+sequence.count('G'))/len(sequence))*100

print('DNA Sequence:', sequence)
print('CG Percentage =', CG_Percentage)
print('C Percentage =', C_Percentage)
print('G Percentage =', G_Percentage)
