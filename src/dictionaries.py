

player = dict()
player['name'] = 'Andrew'
player['weapon'] = 'broadsword'
player['hearts'] = '40%'
player['shrines'] = 110

print(player)
print(player["weapon"])
player['shrines'] = player['shrines'] + 10
print(player)
player["horse"] = "Charlie"
print(player)


count = dict()
names = ["Andrew", "Gina", "Andrew", "Belle",
         "Gina", "Roxcy", "Jonah", "Gina", "Gina"]
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)


for name in names:
    count[name] = count.get(name, 0) + 1

print(count)

counts = dict()
print("Enter a line of text:")
line = input('')

words = line.split()

print("Words:", words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

birthday = {"Andrew": "March", "Gina": "October", "Belle": "January"}
for person in birthday:
    print(person, birthday[person])

print(list(birthday))
print(birthday.keys())
print(birthday.values())
print(birthday.items())

for aaa, bbb in birthday.items():
    print(aaa, bbb)
