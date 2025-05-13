# with open('test.txt', 'a') as writer:
#     writer.write("writng from code")

# with open('test.txt') as reader:
#     content = reader.readlines()
#     with open('test.txt', 'w') as writer:
#         for line in reversed(content):
#             writer.write(line)
#
#         for line in reversed(content):
#             print(line)


with open('test.txt') as reader:
    print(reader.read())