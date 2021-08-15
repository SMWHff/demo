
# f = open("README.md")
# print(f.readable())
# # print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

with open("README.md") as f:
    line = True
    while line:
        line = f.readline()
        print(line)