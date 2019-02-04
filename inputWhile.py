
#函数input()
message = ''#input("Tell me something, and I will repeat it back to you: ")
print(message)



#input输入数字
age = 10#input("How old are you? ")
age = int(age)
print(age)

if age > 18:
    print('age > 18')


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)