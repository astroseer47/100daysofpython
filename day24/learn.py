file = open("my_text.txt")
contents = file.read()
print(contents)
file.close()

with open('my_text.txt', mode='r') as f:
    contents = f.read()
    print(contents)


with open('my_text.txt', mode='w') as f:
    f.write("New text updated")