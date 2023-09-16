# dsa-code-challenge-python
# Python Functions

This repository contains Python functions for various tasks.

## Stacks

### is_balanced

This function checks if an expression containing parentheses, curly braces, and square brackets is balanced.

Sample Usage:
```python
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
```


### remove_duplicates

This function removes duplicates in a sequence and return a new sequence in the original order as the passed sequence 


Sample Usage:
```python
sample input = 

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
```


### Word frequency

This function takes 
a sentence and returns a dictionary containing the frequency of each 
word in the sentence. 


Sample Usage:
```python
sample input = 

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result) # output{'This': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}
```

