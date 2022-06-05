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

#Exercice
dog = {}
print(dog)
dog=dict()
print(dog)

new_list = {'name': 'Fufi', 'color': 'Brown', 'breed': 'German shepherd', 'legs': 'four', 'age': 2}
dog.update(new_list)        #adding items to a list using .update()
print(dog)

student = {'first_name':'Brenda', 'last_name':'Murugi', 'gender':'Female', 'age':22, 'marital status':'Single', 'skills':['swimming','Organisational skills','UI/UX Design'], 'country':'Kenya', 'city':'Nairobi' ,'address':'P.O.BOX'}
print (student)
print(len(student))

print(type(student['skills']))          #type of the values

new_skills=['dancing','drawing']
student['skills'].extend(new_skills)        #adding more skills in the skills value list
print(student)

key= student.keys()
print(key)                  #getting keys in a list

value = student.values()
print(value)                #getting values in a list

print(student.items())      #changing dictionary to a list of  tuple

del student['address']      #deleting an item from a dict
print(student)

del dog         #deleting a dict
# print(dog)  