Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# 3a line of hyphens same length as belgium string

a = len(Belgium)
print('\n', '-' * a)

# 3b string with the comma separators replaced by colons ':'

b = Belgium.replace(',', ':')
print('\n', b)

# 3c population of belgium plus population of capital city (answer11183818)

c = int(Belgium[8:16]) + int(Belgium[26:32])
print('\n', c)
