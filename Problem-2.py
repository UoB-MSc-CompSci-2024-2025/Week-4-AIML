import logic

def implies(p,q):
    return not (p and not q)

"""
1. Neighbourhood watch is active
2. Street lighting is adequate
3. Neighbourhood is safe
4. If the neighbourhood watch is active and street lighting is adequate, then the neighbourhood is considered safe
"""

def KB(C,O,P):
    return implies(C and O, P)
# If both C and O are True, then it implies that P is True

def Y(C,O,P):
    return implies(not P, not C or not O)
# If O is False, then P is also False

models, modelKBi, modelYi, entails = logic.model_check(KB,Y)
print(f'Model-check entailment: (KB ⊨ Y) is {entails}')

print(models)
# As seen in 'logic.py', models is the set of permutations of True and False values:
# [[False, False, False], [False, False, True], [False, True, False], [False, True, True], 
# [True, False, False], [True, False, True], [True, True, False], [True, True, True]]

print(modelKBi)
print(modelYi)
# model KBi and modelYi return the index if the value is True, and nothing if False:
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Because these are aligned, it means that the logical inference of our KB and Y functions are correct;
# the variable 'entails' as seen in the model_check() function therefore returns True
# If there was any variation, it would mean that our logical inference of these statements was incorrect and it would return False