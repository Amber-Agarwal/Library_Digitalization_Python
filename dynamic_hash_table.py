from hash_table import HashSet, HashMap
from prime_generator import get_next_size

# class DynamicHashSet(HashSet):
#     def __init__(self, collision_type, params):
#         super().__init__(collision_type, params)
        
#     def rehash(self):
#         # IMPLEMENT THIS FUNCTION
#         pass
        
#     def insert(self, key):
#         # YOU DO NOT NEED TO MODIFY THIS
#         super().insert(key)
        
#         if self.get_load() >= 0.5:
#             self.rehash()
            
            
# class DynamicHashMap(HashMap):
#     def __init__(self, collision_type, params):
#         super().__init__(collision_type, params)
        
#     def rehash(self):
#         # IMPLEMENT THIS FUNCTION
#         pass
        
#     def insert(self, key):
#         # YOU DO NOT NEED TO MODIFY THIS
#         super().insert(key)
        
#         if self.get_load() >= 0.5:
#             self.rehash()


# class DynamicHashSet(HashSet):
#     def __init__(self, collision_type, params):
#         super().__init__(collision_type, params)
        
#     def rehash(self):
#         # Store old table and its properties
#         old_table = self.table
#         old_size = self.table_size
        
#         # Get next prime size (approximately double)
#         self.table_size = get_next_size()
        
#         # Reset table and count
#         if self.collision_type == "chaining":
#             self.table = [[] for _ in range(self.table_size)]
#         else:
#             self.table = [None] * self.table_size
#         self.count = 0
        
#         # Reinsert all elements from old table
#         if self.collision_type == "chaining":
#             for chain in old_table:
#                 for key in chain:
#                     self.insert(key)
#         else:  # linear or double hashing
#             for item in old_table:
#                 if item is not None:
#                     self.insert(item)
    
#     def insert(self, key):
#         # YOU DO NOT NEED TO MODIFY THIS
#         super().insert(key)
        
#         if self.get_load() >= 0.5:
#             self.rehash()
            
# class DynamicHashMap(HashMap):
#     def __init__(self, collision_type, params):
#         super().__init__(collision_type, params)
        
#     def rehash(self):
#         # Store old table and its properties
#         old_table = self.table
#         old_size = self.table_size
        
#         # Get next prime size (approximately double)
#         self.table_size = get_next_size(2 * self.table_size)
        
#         # Reset table and count
#         if self.collision_type == "chaining":
#             self.table = [[] for _ in range(self.table_size)]
#         else:
#             self.table = [None] * self.table_size
#         self.count = 0
        
#         # Reinsert all elements from old table
#         if self.collision_type == "chaining":
#             for chain in old_table:
#                 for key, value in chain:
#                     self.insert(key, value)
#         else:  # linear or double hashing
#             for item in old_table:
#                 if item is not None:
#                     key, value = item
#                     self.insert(key, value)
#     def insert(self, key):
#         # YOU DO NOT NEED TO MODIFY THIS
#         super().insert(key)
        
#         if self.get_load() >= 0.5:
#             self.rehash()


# class DynamicHashSet(HashSet):
#     def __init__(self, collision_type, params):
#         # Need to convert collision type to lowercase to match parent class
#         collision_type = collision_type.lower()
#         super().__init__(collision_type, params)
    
#     def rehash(self):
#         # Store old table
#         old_table = self.table
        
#         # Get next prime size
#         new_size = get_next_size(2 * self.table_size)
        
#         # Update params based on collision type
#         if self.collision_type == "chaining":
#             params = (self.z, new_size)
#         elif self.collision_type == "linear":
#             params = (self.z, new_size)
#         else:  # double hashing
#             params = (self.z1, self.z2, self.c2, new_size)
            
#         # Reinitialize with new size but keep old elements
#         super().__init__(self.collision_type, params)
        
#         # Reinsert all elements
#         if self.collision_type == "chaining":
#             for chain in old_table:
#                 for key in chain:
#                     super().insert(key)  # Use parent's insert
#         else:
#             for item in old_table:
#                 if item is not None:
#                     super().insert(item)  # Use parent's insert

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        
        old_table = self.table
        
        self.table_size = get_next_size()
        
        if self.collision_type == "Chain":
            self.table = [[] for _ in range(self.table_size)]
        else:
            self.table = [None] * self.table_size
        self.count = 0
        
        if self.collision_type == "Chain":
            for chain in old_table:
                for key in chain:
                    self.insert(key)
        else:  
            for item in old_table:
                if item is not None:
                    self.insert(item)
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
    def __str__(self):
        return super().__str__()


class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        # collision_type = collision_type.lower()
        super().__init__(collision_type, params)
    
    def rehash(self):
        old_table = self.table
        
        new_size = get_next_size()
        
        if self.collision_type == "Chain":
            params = (self.z, new_size)
        elif self.collision_type == "Linear":
            params = (self.z, new_size)
        else:  # double hashing
            params = (self.z1, self.z2, self.c2, new_size)
            
        super().__init__(self.collision_type, params)
        
        if self.collision_type == "Chain":
            for chain in old_table:
                for key, value in chain:
                    super().insert((key, value))
        else:
            for item in old_table:
                if item is not None:
                    key, value = item
                    super().insert((key, value))

    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
    def __str__(self):
        return super().__str__()