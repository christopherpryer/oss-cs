# Counting Vowels

s = ''
count = 0
for char in s:
    if char.lower() in "aeiou":
        count += 1

print "Number of vowels: %d" % count
