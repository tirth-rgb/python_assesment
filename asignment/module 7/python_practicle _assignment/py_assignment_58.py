from collections import Counter

# Sample data
data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

# Create a Counter
result = Counter()

# Combine amounts
for d in data:
    result[d['item']] += d['amount']

# Display output
print(result)
