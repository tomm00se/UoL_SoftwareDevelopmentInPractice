# Exercise: Given a list of data, return the type associated with that data.

def type_finder(data):
    """
    This function takes a list of data and returns the type associated with that data
    """
    for item in data:
        print("Type of ", item, " is ", type(item))
        
type_finder([1, 2, 3, "hello", "world", 4.5, 5.6, 7.8, 9.0, (0, -1), [5, 12], {"class": 'V', "section": 'A'}])