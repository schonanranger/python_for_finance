d = {
    'Name':'Angela Merkel',
    'Country':'Germany',
    'Profession':'Chancelor',
    'Age':60,
}

print(type(d))
print(d['Name'],d['Age'],"\n")
print(d.keys())
print(d.values())
print(d.items())
birthday = True
if birthday is True:
    d['Age'] += 1
print(d['Age'])