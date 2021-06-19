"""
Реализуйте необходимые методы для того, чтобы следующий код выполнился

Должна быть возможность инициализировать LinkedList с помощью списка, 
или пустым.
"""


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, lst=None):
        if lst is None:
            self.head = None
        else:
            self.head = Element(0)
            current = self.head
            for e in lst:
                current.next = Element(e) 
                current = current.next

    def __str__(self):
        r = '|'
        e = self.head
        if e is not None:
            while e is not None:
                r += str(e.value)
                r += ' -> '
                e = e.next  
            r = r[:-4]  
        else:
            pass       
        r += '|'   
        return r

    def __getitem__(self, key):
        self.key = key 
        return key

    def __setitem__(self, key, value):
        self.key = key
        self.value = value
        return key, value
        
    def append(self, value):
        if self.head is None:
            self.head = Element(value)
            return

        e = self.head
        while e.next is not None:
            e = e.next
        e.next = Element(value)


ll = LinkedList()
ll2 = LinkedList([1, 2, 3])

print(ll)
# empty list should be represented as two pipes (vertical lines)
# || 

print(ll2)
# |1 -> 2 -> 3|

ll2.append('new')
print(ll2)
# |1 -> 2 -> 3 -> 'new'|

# print(len(ll2))
# 4

print(ll2[2])
# 3

# ll2[2] = 'changed'
# print(ll2)
# # |1 -> 2 -> 'changed' -> 'new'|

# del ll2[1]
# print(ll2)
# # |1 -> 'changed' -> 'new'|

# print('truthy' if ll else 'falsy')
# # falsy

# print('truthy' if ll2 else 'falsy')
# # truthy

# ll3 = LinkedList([5, 6])
# print(ll2 + ll3)
# # |1 -> 'changed' -> 'new' -> 5 -> 6|

# ll4 = LinkedList([1, 'changed', 'new'])
# print('equal' if ll2 == ll4 else 'not equal')
# # equal

# print('not equal' if ll2 != ll3 else 'equal')
# not equal

# Если предыдущего покажется маловато, то вот со звездочкой на десерт:
# for i in ll2:
#     print(i)