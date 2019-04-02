

string = "These are words that I split, so deal, yo"
list = string.split(',')
print(list)
print(len(list))
for word in list:
    print(word)

line = 'from andrewcengiz@gmail.com'
words = line.split()
email = words[1]
segments = email.split('@')
service = segments[1]
site = service.split('.')
gmail = site[0]
print(gmail)
