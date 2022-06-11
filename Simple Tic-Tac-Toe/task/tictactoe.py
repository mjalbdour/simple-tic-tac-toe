# write your code here
def print_dashes():
    print("---------")


play = input()
print_dashes()

i = 0
for j in range(3):
    row = "| "
    for k in range(3):
        row = row + play[i] + " "
        i += 1
    row = row + "|"
    print(row)

print_dashes()
