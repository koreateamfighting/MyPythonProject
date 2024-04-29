str = "abstract algebra"
result = []

for s in str:
    if s == "a" or "A":
        s = s.upper()
        result.append(s)
    elif s == r'[A-Z]':
        s = s.lower()
        result.append(s)
        
print(result)
        