principle = 5000
interest_rate = 0.035

# interest = principle * interest_rate
# principle = principle + interest #this is equivalent to below
for i in range(5):
    principle += principle * interest_rate
print(f'Principle: ${principle:0.2f}')
# principle *= 1 + interest_rate  #equivalent but less readable