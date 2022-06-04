#Dictionery - a collection of an unordered,mutable,paired(key:value) data type
empty_dict = {}
print(empty_dict)
empty_dict2=dict()
print(empty_dict2)

print(len(empty_dict2))     #checking length

dict3 = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5'}
print(dict3.get('key1'))        #check if the key exists-if it doesn't it output 
print(dict3['key1'])        #accessing keys

dict3['key6']=['value6','skills','python']
print(dict3)        #adding items to a dict

dict3['key6'].append('HTML')
print(dict3)        #appending a list in values of a dict

dict3['key1']='one'
print(dict3)        #modifying items in a dict

print('key1' in dict3)      #checking keys in dict

dict3.pop('key1')       #removing items by a specific key
print(dict3)

dict3.popitem()     #removes the last item
print(dict3)

del dict3['key2']       #removes item with specific key
print(dict3)

print(dict3.items())        #items() changes the dict to a list of tuples

print(dict3.clear())        #clears all items in the dict

del dict3       #deleting a dict

dict3 = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5'}
dict_copy=dict3.copy()
print(dict_copy)        #copies a dictionary

keys = dict3.keys()     #getting keys in a list
print(keys)

values = dict3.values()      #getting values in list
print(values)