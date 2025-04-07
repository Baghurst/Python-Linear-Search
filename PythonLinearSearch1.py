key = 3
L = [1,2,3,4,]
index = 0
while index < len(L):
    if L[index] == key:
        print(f"Number {key} found at index {index}.")
        break
    index += 1
if index == len(L):
    print(f"Number {key} not found in the list.")
