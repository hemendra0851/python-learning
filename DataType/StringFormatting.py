# Format string with fixed width

data = '{0:<15}'.format('abc') # Left justified
print(data)
data = '{0:>15}'.format('abc') # Right justified
print(data)
data = '{0:^15}'.format('abc') # Centered
print(data)