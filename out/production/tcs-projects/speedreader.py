"""
Attempts to use RSVP but on the python console line

https://www.youtube.com/watch?v=5yddeRrd0hA
"""

def split_str(string):
    return string.split()

def read(string):
    for word in string.split(): print(word)

if __name__ == '__main__':
    read("I like drinking sour cream")