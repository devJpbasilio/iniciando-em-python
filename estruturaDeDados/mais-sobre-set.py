

s1 = {1, 2, 3, 4, 5, 6}
s1.update([6, 7, 8, 9, 10])
s1.remove(7) # caso não encontre o item não existir no meu set
s1.discard(12) # não gera esse erro

print(type(s1))
print(s1)
print()
print()

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
print(set4)