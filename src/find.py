

state = "Arizona"

print(state.find('zona'))

statement = "Hello, how are you"

edited = statement.replace("how", "who")
print(edited)


x = "   what the heck     "
print(x.lstrip())
print(x)
print(x.rstrip())
print(x.strip())

data = "my email address is andrewcengiz@gmail .com "

# What email service do I use?

start = data.find('@')
print(start)
end = data.find(' ', start)
print(end)
service = data[start+1: end]
print(service)

str = 'X-DSPAM-Confidence:0.8475'

start = str.find(':')
number = str[start+1:]
print(number)
value = float(number)
print(value)
