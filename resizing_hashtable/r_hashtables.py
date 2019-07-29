

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5) + hash) + ord(x)  
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashed = hash(key,hash_table.capacity)
    newpair = LinkedPair(key,value)
    
    currentPair = hash_table.storage[hashed]
    while currentPair is not None and currentPair.key != key:
        currentPair = currentPair.next
    if currentPair == None:
        newpair.next = hash_table.storage[hashed]
        hash_table.storage[hashed] = newpair
    else:
        currentPair.value = value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed = hash(key,hash_table.capacity)

    if hash_table.storage[hashed] != None and hash_table.storage[hashed].next == None and hash_table.storage[hashed].key == key:
        hash_table.storage[hashed] = None
        return
    elif hash_table.storage[hashed] != None and hash_table.storage[hashed].next != None and hash_table.storage[hashed].key == key:
        hash_table.storage[hashed] = hash_table.storage[hashed].next
        return
    
    currentPair  = hash_table.storage[hashed]
    while currentPair is not None and currentPair.key != key:
        lastpair = currentPair
        currentPair = currentPair.next
    if currentPair.key == key and currentPair != None:
        lastpair.next = currentPair.next
        hash_table.storage[hashed] = lastpair
    else:
        print("value isnt there")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed = hash(key,hash_table.capacity)
    currentPair = hash_table.storage[hashed]

    if hash_table.storage[hashed] != None and hash_table.storage[hashed].key == key:
        return hash_table.storage[hashed].value
    while currentPair is not None and currentPair.key != key:
        currentPair = currentPair.next
    if currentPair == None:
        return None
    elif currentPair != None and currentPair.key == key:
        return currentPair.value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    newHashTablestorage = hash_table.storage
    hash_table.capacity = hash_table.capacity * 2
    hash_table.storage = [None] * hash_table.capacity
    for i in range(len(newHashTablestorage) ):
        if newHashTablestorage[i] != None and newHashTablestorage[i].next == None :
            hash_table_insert(hash_table,newHashTablestorage[i].key,newHashTablestorage[i].value)
        elif newHashTablestorage[i] != None and newHashTablestorage[i].next != None :
                currentPair = newHashTablestorage[i]
                hash_table_insert(hash_table,currentPair.key,currentPair.value)               
                while currentPair.next:
                    currentPair = currentPair.next
                    hash_table_insert(hash_table,currentPair.key,currentPair.value)               
    
    return hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)


    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
