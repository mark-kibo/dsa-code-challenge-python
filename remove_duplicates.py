def remove_duplicates(sequence):
    # handle if seq is a tuple or list
    new_sequence=list(sequence)
    my_unique=[]
    for i in set(new_sequence):
        my_unique.append(i)
    return my_unique

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  