
from prime_generator import get_next_size

# class HashTable:
#     def __init__(self, collision_type, params):
#         '''
#         Possible collision_type:
#             "Chain"     : Use hashing with chaining
#             "Linear"    : Use hashing with linear probing
#             "Double"    : Use double hashing
#         '''
#         pass
    
#     def insert(self, x):
#         pass
    
#     def find(self, key):
#         pass
    
#     def get_slot(self, key):
#         pass
    
#     def get_load(self):
#         pass
    
#     def __str__(self):
#         pass
    
#     # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
#     def rehash(self):
#         pass
    
# # IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# # IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# # YOU WOULD NOT NEED TO WRITE IT TWICE
    
# class HashSet(HashTable):
#     def __init__(self, collision_type, params):
#         pass
    
#     def insert(self, key):
#         pass
    
#     def find(self, key):
#         pass
    
#     def get_slot(self, key):
#         pass
    
#     def get_load(self):
#         pass
    
#     def __str__(self):
#         pass
    
# class HashMap(HashTable):
#     def __init__(self, collision_type, params):
#         pass
    
#     def insert(self, x):
#         # x = (key, value)
#         pass
    
#     def find(self, key):
#         pass
    
#     def get_slot(self, key):
#         pass
    
#     def get_load(self):
#         pass
    
#     def __str__(self):
#         pass




class HashTable:
    def __init__(self, collision_type, params):

        self.collision_type = collision_type
        if collision_type == "Chain":
            self.z, self.table_size = params
            self.table = [[] for _ in range(self.table_size)]
        elif collision_type == "Linear":
            self.z, self.table_size = params
            self.table = [None] * self.table_size
        elif collision_type == "Double":
            self.z1, self.z2, self.c2, self.table_size = params
            self.table = [None] * self.table_size
        self.count = 0
    
    def char_to_number(self, char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 26
        else:
            return ord(char)%52
        
    def polynomial_hash(self, key, z):
        h = 0
        i=0
        for i  in range(len(key)):
            h = h * z + self.char_to_number(key[len(key)-i-1])
        return h
    

    
    def get_slot(self, key):
        if self.collision_type == "Chain" or self.collision_type == "Linear":
            return self.polynomial_hash(key, self.z) % self.table_size
        elif self.collision_type == "Double":
            h1 = self.polynomial_hash(key, self.z1) % self.table_size
            
            return h1
    
    def get_load(self):
        return self.count / self.table_size
    
    def rehash(self):
        pass


class HashSet(HashTable):
    def __init__(self, collision_type, params):
#         pass
        super().__init__(collision_type, params)
        self.dist = 0
        # self.collision_type = collision_type
        # if collision_type == "chaining":
        #     self.z, self.table_size = params
        #     self.table = [[] for _ in range(self.table_size)]
        # elif collision_type == "linear":
        #     self.z, self.table_size = params
        #     self.table = [None] * self.table_size
        # elif collision_type == "double":
        #     self.z1, self.z2, self.c2, self.table_size = params
        #     self.table = [None] * self.table_size
        # self.count = 0

    def insert(self, key):
        # if self.count == self.table_size:
            # raise Exception("Table is full")
        
        slot = self.get_slot(key)
        if self.collision_type == "Chain":
            if key not in self.table[slot]:
                self.table[slot].append(key)
                self.count += 1
        elif self.collision_type == "Linear":
            i=0
            while self.table[slot] is not None:

                if self.table[slot] == key:
                    return
                slot = (slot + 1) % self.table_size
                i+=1
            if i==self.table_size:
                raise Exception("Table is full")
            self.table[slot] = key
            self.count += 1
        elif self.collision_type == "Double":
            h1= slot
            h2 = self.c2 - (self.polynomial_hash(key, self.z2) % self.c2)
            i = 0
            while self.table[(h1 + i * h2) % self.table_size] is not None:
                if self.table[(h1 + i * h2) % self.table_size] == key:
                    return
                i += 1
            if i==self.table_size:
                raise Exception("Table is full")
            self.table[(h1 + i * h2) % self.table_size] = key
            self.count += 1
    
    def find(self, key):
        slot = self.get_slot(key)
        if self.collision_type == "Chain":
            return key in self.table[slot]
        elif self.collision_type == "Linear":
            while self.table[slot] is not None:
                if self.table[slot] == key:
                    return True
                slot = (slot + 1) % self.table_size
            return False
        elif self.collision_type == "Double":
            h1 = slot
            h2 = self.c2 - (self.polynomial_hash(key, self.z2) % self.c2)
            i = 0
            while self.table[(h1 + i * h2) % self.table_size] is not None:
                if self.table[(h1 + i * h2) % self.table_size] == key:
                    return True
                i += 1
            return False
    
    def __str__(self):
        res = []
        for slot in self.table:
            if self.collision_type == "Chain":
                if len(slot)==0:
                    res.append("<EMPTY>")
                else :
                    res.append(" ; ".join(slot))
            else:
                if slot is None:
                    res.append("<EMPTY>")
                else:
                    res.append(str(slot))
        return " | ".join(res)


class HashMap(HashTable):

    def insert(self, x): # x = (key,value)
        # if self.count == self.table_size:
            # raise Exception("Table is full")

        slot = self.get_slot(x[0])
        if self.collision_type == "Chain":
            for entry in self.table[slot]:
                if entry[0] == x[0]:
                    return
            self.table[slot].append(x)
            self.count += 1
        elif self.collision_type == "Linear":
            j=0
            while self.table[slot] is not None:
                if self.table[slot][0] == x[0]:
                    return
                slot = (slot + 1) % self.table_size
                j+=1
            if j==self.table_size:
                raise Exception("Table is full")
            self.table[slot] = x
            self.count += 1
        elif self.collision_type == "Double":
            h1 = slot
            h2 = self.c2 - (self.polynomial_hash(x[0], self.z2) % self.c2)
            i = 0
            while self.table[(h1 + i * h2) % self.table_size] is not None:
                if self.table[(h1 + i * h2) % self.table_size][0] == x[0]:
                    return
                i += 1
            if i==self.table_size:
                raise Exception("Table is full")
            self.table[(h1 + i * h2) % self.table_size] = x
            self.count += 1
    
    def find(self, key):
        slot = self.get_slot(key)
        if self.collision_type == "Chain":
            for entry in self.table[slot]:
                if entry[0] == key:
                    return entry[1]
            return None
        elif self.collision_type == "Linear":
            while self.table[slot] is not None:
                if self.table[slot][0] == key:
                    return self.table[slot][1]
                slot = (slot + 1) % self.table_size
            return None
        elif self.collision_type == "Double":
            h1 = slot
            h2 = self.c2 - (self.polynomial_hash(key, self.z2) % self.c2)
            i = 0
            while self.table[(h1 + i * h2) % self.table_size] is not None:
                if self.table[(h1 + i * h2) % self.table_size][0] == key:
                    return self.table[(h1 + i * h2) % self.table_size][1]
                i += 1
            return None
    
    def __str__(self):
        ans = []
        for slot in self.table:
            if self.collision_type == "Chain":
                if len(slot) == 0:
                    ans.append("<EMPTY>")
                else:
                    ans.append(" ; ".join(f"({k}, {v})" for k, v in slot))
            else:
                if slot is None:
                    ans.append("<EMPTY>")
                else:
                    ans.append(f"({slot[0]}, {slot[1]})")
        return " | ".join(ans)


# def main():
#     # Parameters for hash table
#     jobs_params = (31, 10)               # For Chain: (z, table_size)
#     gates_params = (31, 10)              # For Linear: (z, table_size)
#     bezos_params = (31, 37, 7, 10)       # For Double: (z1, z2, c2, table_size)

#     # Create all combinations
#     print("===== Testing String Representation =====")
    
#     # HashSet with all collision types
#     hash_set_jobs = HashSet("Chain", jobs_params)
#     hash_set_gates = HashSet("Linear", gates_params)
#     hash_set_bezos = HashSet("Double", bezos_params)

#     # HashMap with all collision types
#     hash_map_jobs = HashMap("Chain", jobs_params)
#     hash_map_gates = HashMap("Linear", gates_params)
#     hash_map_bezos = HashMap("Double", bezos_params)

#     # Test data
#     test_data = ["Apple", "Banana", "Cherry"]
#     map_data = [("Apple", "Red"), ("Banana", "Yellow"), ("Cherry", "Purple")]

#     print("\nHashSet with Chain Collision (Jobs):")
#     for word in test_data:
#         hash_set_jobs.insert(word)
#     print(hash_set_jobs)

#     print("\nHashSet with Linear Probing (Gates):")
#     for word in test_data:
#         hash_set_gates.insert(word)
#     print(hash_set_gates)

#     print("\nHashSet with Double Hashing (Bezos):")
#     for word in test_data:
#         hash_set_bezos.insert(word)
#     print(hash_set_bezos)

#     print("\nHashMap with Chain Collision (Jobs):")
#     for key, value in map_data:
#         hash_map_jobs.insert((key, value))
#     print(hash_map_jobs)

#     print("\nHashMap with Linear Probing (Gates):")
#     for key, value in map_data:
#         hash_map_gates.insert((key, value))
#     print(hash_map_gates)

#     print("\nHashMap with Double Hashing (Bezos):")
#     for key, value in map_data:
#         hash_map_bezos.insert((key, value))
#     print(hash_map_bezos)

# if __name__ == "__main__":
#     main()