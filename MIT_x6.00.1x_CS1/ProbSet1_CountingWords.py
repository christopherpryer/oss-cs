# Counting Words -- bob

bob = 0
s = 'azcbobobegghakl'
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        bob += 1
print 'Number of times bob occurs is: %d' % bob
