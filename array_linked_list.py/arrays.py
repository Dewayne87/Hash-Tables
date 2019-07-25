

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self,capacity):
        # Your code here
        self.count = 0
        self.capacity = capacity
        self.elements = [None] * capacity
        


# Double the size of the given array
def resize_array(array):
    # Your code here
    newCapacity = array.capacity * 2
    newElements = [None] * newCapacity
    for i in range(array.capacity):
        newElements[i] = array.elements[i]
    array.elements = newElements
    array.capacity = newCapacity



# Return an element of a given array at a given index
def array_read(array,index):
    # Throw an error if array is out of the current count
    # Your code here
    if index >= array.count:
        print("You don' Goof'd")
        return None
    return array.elements[index]


# Insert an element in a given array at a given index
def array_insert(array,value,index):
    # Throw an error if array is out of the current count
    if index > array.count:
        print("You don' Goof'd")
        return None

    # Resize the array if the number of elements is over capacity
    if array.capacity <= array.count:
        resize_array(array)
    for i in range(array.count, index, - 1):
        array.elements[i] = array.elements[i-1]
    # Move the elements to create a space at 'index'
    # Think about where to start!

    # Add the new element to the array and update the count
    array.elements[index] = value
    array.count += 1


# Add an element to the end of the given array
def array_append(array,value):

    # Hint, this can be done with one line of code
    # (Without using a built in function)

    # Your code here
    array_insert(array, value, array.count)


# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove(array,element):
    # Your code here
    removed = False
    for i in range(array.count):
        if removed:
            array.elements[i-1] == array.elements[i]
        elif array.elements[i] == element:
            removed = True
        if removed:
            array.count -=1
            array.elements[array.count] = None
        else:
            print("Error, element" + str(element) + " not found")


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop(array,index):
    if index > array.count:
        print("Error, element " + str(index) +" is out of range")
        return None
    # Throw an error if array is out of the current count
    return_value = array.elements[index]
    for i in range(index + 1, array.count):
        array.elements[i-1] = array.elements[i]
    # Your code here
    array.count -=1
    array.elements[array.count] = None
    return return_value


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# # Testing
arr = array(1)

array_insert(arr, "STRING1", 0)
array_print(arr)
array_pop(arr, 0)
array_print(arr)
array_insert(arr, "STRING1", 0)
array_append(arr, "STRING4")
array_insert(arr, "STRING2", 1)
array_insert(arr, "STRING3", 2)
array_print(arr)
