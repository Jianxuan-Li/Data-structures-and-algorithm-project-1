def contains(target, source):
    if not len(source):
        return False
    mid = len(source) // 2
    
    if ord(target) < ord(source[mid]):
        return contains(target, source[:mid])
    elif ord(target) > ord(source[mid]):
        return contains(target, source[mid + 1:])
    else:
        return True

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False