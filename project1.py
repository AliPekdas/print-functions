# dir() takes functions of strings, lists, tuples, sets and dictionaries
string_functions = []
for i in dir(str):
    if i.startswith("__"):
        continue
    string_functions.append(i)

list_functions = []
for i in dir(list):
    if i.startswith("__"):
        continue
    list_functions.append(i)

tuple_functions = []
for i in dir(tuple):
    if i.startswith("__"):
        continue
    tuple_functions.append(i)

set_functions = []
for i in dir(set):
    if i.startswith("__"):
        continue
    set_functions.append(i)

dictionary_functions = []
for i in dir(dict):
    if i.startswith("__"):
        continue
    dictionary_functions.append(i)

header = ["String", "List", "Tuple", "Set", "Dictionary"]
functions = [string_functions, list_functions, tuple_functions, set_functions, dictionary_functions]

max_len = 0
for i in functions:
    if len(i) > max_len:
        max_len = len(i)

for h in header:
    print(h, end="")
    print(" " * (30 - len(header)), end="")
print()
print("-" * 129, end="")

for i in range(max_len):
    print()
    for j in functions:
        if i >= len(j):
            print("-----", end="")
            print(" " * 25, end="")
        else:
            print(j[i], end="")
            print(" " * (30 - len(j[i])), end="")

# writing to file
f = open("project1.txt", "w")
for h in header:
    f.write(h)
    f.write(" " * (30 - len(header)))
f.write("\n")
f.write("-" * 129)

for i in range(max_len):
    f.write("\n")
    for j in functions:
        if i >= len(j):
            f.write("-----")
            f.write(" " * 25)
        else:
            f.write(j[i])
            f.write(" " * (30 - len(j[i])))
