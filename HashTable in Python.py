class HashTable:
    def __init__(self):
        self.max=10
        self.arry=[[] for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h += ord(i)
        return h%self.max
    
    def add(self, key, value):
        h=self.get_hash(key)  
        found = False 
        for index, element in enumerate(self.arry[h]):
            if len(element)==2 and element[0]==key:
                self.arry[h][index]=(key, value) 
                found=True
                break
        if found == False:
            self.arry[h].append((key, value))
            
    def delete(self,key):
        h=self.get_hash(key)
        for index, kv in enumerate(self.arry[h]):
            if len(kv)==2 and kv[0]==key:
                del self.arry[h][index]
                break
            
        
    def get_value(self,key):
        h=self.get_hash(key)
        for kv in self.arry[h]:
            if kv[0]==key:
                return kv[1] 
    
    
        
l=HashTable()
l.add("march 6",130)
l.add("march 17",150)
l.add("jan 6",1500)
l.add("feb 6",180)
l.add("oct 6",10)
print(l.arry)
print(l.get_value("march 6"))
l.delete("march 6")

print(l.arry)
print(l.get_hash("jan 6"))