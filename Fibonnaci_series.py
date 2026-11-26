first=0
second=1

print(first)
print(second)

for i in range(11):
    new=first+second

    first=second
    second=new
    print(new)