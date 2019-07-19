from google.appengine.api import memcache

def add(ID,value,keys):
    data=memcache.get(ID)
    if data is None:
        memcache.add(ID,value)
    else:   
        raise ValueError("Id already exist")
    return memcache.get_multi(keys)

def delete1(ID,keys):
    stat=memcache.delete(str(ID))
    if stat == 1:
        raise ValueError("Deletion not possible check the Id")
    return memcache.get_multi(keys)

def update1(ID,Name1,Salary1,Design1,keys):
    data=memcache.get(str(ID))
    if data is None:
        raise ValueError("Id does not exist")
    else:
        data["Name"] = Name1
        data["Salary"] = Salary1
        data["Design"] = Design1
        memcache.set(ID,data)
    return memcache.get_multi(keys)

def clear_memcache():
    return memcache.flush_all()

def read(keys):
    return memcache.get_multi(keys)
    #rdata=[{k:memcache.get(str(k))} for k in set(keys)]
    #return rdata


