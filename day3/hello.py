#__all__ = ['addnum','divnum'] # restricts functions/classes to be imported when 'from module import *' directive is used
def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b    

if __name__ == '__main__':
    # __name__ - will return the current namespace
    print("calling from module:",__name__)
    print("calling from module:",addnum(24,8))
    print("calling from module:",divnum(24,8))