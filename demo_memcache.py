from google.appengine.api import memcache

data=memcache.get("Emp_id")
Experience= str(input("Input Id to add:"))
name = str(input("Input name:"))
design = str(input("Input design:"))
if data is None:
    value = {"Name":name,"Designation":design,"Experience":Experience}
    memcache.add("1",value,namespace="Demo")
else:
    print(data)