dictionary = {"1":{"Name":"ROhith","design":"SD"},
            "2":{"Name":"ROhith","design":"SD"},
            "3":{"Name":"ROhith","design":"SD"}}


print("read data",dictionary)
#Add
Id= str(input("Input Id to add:"))
name = str(input("Input name:"))
design = str(input("Input design:"))
dictionary.update({Id :{"Name":name,"design":design}})
print(dictionary)
#delete
print("delete data")
ke = str(input("Enter the key to delete:"))
print("checking return statement",dictionary.pop(ke))
print("printing after deleting",dictionary)
#update
iud=str(input("Input Id to update the details:"))
Field = str(input("filed to change:"))
value= str(input("value to change:"))
dat=dictionary.get(iud)
print(dat)
dat[Field] = value
print(dictionary[iud])
print(dictionary)
