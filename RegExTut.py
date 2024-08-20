import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("search successful.")

else:
    print("Search unsuccessful.")


#^ used for 'starts with'

#$ used for 'ends with'