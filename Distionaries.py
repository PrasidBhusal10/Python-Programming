std ={"Name":"Prasid", "age": 20, "city": "Butwal", "Course":["Math", "Science", "English"]}
print(std)
print(std["Name"])
print(std["Course"])
#using get method
print(std.get("Name")) #it will return none because of case sensitivity
#To update the date in the dictionary
std.update({"Name": "Prasid Bhusal"})
print(std)
#To delete the data in the dictionary
del std["city"]
x = std.pop("age")
print(x)
print(len(std))
print(std.keys())   
#To print the keys of the dictionary
for key in std:
    print(key)