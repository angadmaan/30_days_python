# What is the length of the set given below?

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))

# Because set doesn't allow duplicate values. So it will only store one value.

# As (20) and (20.0) are same. So it will only store one value.