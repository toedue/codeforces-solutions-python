# Read input
i, ll, c, f, d = input().split()

# Convert to appropriate types
i = int(i)
ll = int(ll)
c = c          # char stays as string
f = float(f)
d = float(d)

# Print in required format
print(i)
print(ll)
print(c)
print(f"{f:.2f}")   # float: 2 decimal places
print(f"{d:.1f}")   # double: 1 decimal place
