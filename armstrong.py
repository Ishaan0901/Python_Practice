og_number=153
temp=0

for i in str(og_number):
    sq=int(i)**3
    temp=temp+sq


if temp==og_number:
    print('Armstrong')
else:
    print('Non Armstrong')