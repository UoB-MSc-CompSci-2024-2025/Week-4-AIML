import logic

def implies(p,q):
    return (p or q)

# R = 'If it's your birthday or there will be cake, then there will be cake'

birthday = True
cake = True

R = implies(birthday, cake)

print(f"Evaluate proposition: birthday ∨ cake = {R}")