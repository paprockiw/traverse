# traverse
Python-based recursive generator for walking JSON objects dumpped to Python.

How to use this:

1. Import the find_element function.
2. Take some JSON, and use the json.dumps function to dump it into a Python object.
3. Identify the information that you need to pull out of the JSON-like Python object, and the path to that data.
4. Define a list of elements that you need to traverse to get to the data you are operation on (use "*" to get all elements on a given level).
5. Pass the JSON-like Python object and the list of elements to find_element function, assigning a variable to the function to capture its output.
6. Iterate over the results that the function returns, which will be in the form of a generator object. Grab the results and process them in a for loop.

This function works by following the specified traversal path recursively. It uses Python generators under the covers, and will return a generator object. If you're looking for only one item, you'll need to iterate over the results and get just that item. Otherwise, you'll want to iterate and process each one. There is some flexibility in how you can pull items like arrays and dictionaries. You may want to pull the entire item and process one or a few elements, or just pull the elements you need to process. 
