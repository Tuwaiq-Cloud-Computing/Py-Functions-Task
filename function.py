# Create list of three elements
color_list = ["red", "yellow", "green"]
print(color_list)
print("----------")
# add an element to the end of list
color_list.append("white")
print(color_list)
print("----------")
# remove an element from the list
color_list.remove("white")
print(color_list)
print("----------")
# reverse the list
color_list.reverse()
print(color_list)
print("----------")
# sort the list
color_list.sort()
print(color_list)
print("----------")
# add an element at the start of the list
color_list.insert(0, "white")
print(color_list)

print("----------")
# print the index of the last element
index = len(color_list)-1
print(index)

people = ["Ahmed", "Nasser", "Mohammed"]
print("----------")

# Join the list elements using a comma and a space
print(", ".join(people))
print("----------")

#Make a list of 3 dictionaries, each dictionary should contain information such as: name, phone_number
people = [
    {"Ahmed", "123-456-7890"},
    {"Nasser", "987-654-3210"},
    {"Mohammed", "555-444-3333"}
]
for person in people:
    print(person)

 
# now add 1 more dictionary to the list
people.append({"Omar", "444-333-2222"})
print("----------")
for person in people:
    print(person)

# now delete the name from the first dictionary
del people[0]
print("\nList after deleting first name `:")
print(people)

#update the phone number of the last person

#last_person = people[-1]
#last_person["44-333-2222"] = "777-666-5555"
#print(people)

if "name" in people[0]:
    print("The first dictionary has a key called 'name'")
else:
    print("The first dictionary does not have a key called 'name'")