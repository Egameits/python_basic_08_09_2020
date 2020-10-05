file = open('test.txt', 'w', encoding='UTF-8')

# print(file.read(2))
# print(file.read(2))
#
# for line in file:
#     print(line)

file.write('New Hello')
file.close()