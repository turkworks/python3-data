

state = "Montana"
index = 0
while index < len(state):
    letter = state[index]
    print(index, letter)
    index = index + 1


for letter in state:
    print(letter)

word = "banana"
acount = 0

for letter in word:
    if letter == 'a':
        acount = acount + 1
print(acount)
