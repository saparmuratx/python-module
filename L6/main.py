my_dict = dict()
country_info = { "country_name": "Brazil", "region": "Rio"}

# print(my_dict)

my_dict["name"] = "Richard"
my_dict["birth_date"] = 1990.20

skills_list = ["Programming", "Microsoft Excel",]
characteristics = ("Blue Eyes", "Birthmark In Ears",)

print(my_dict["name"])
print(my_dict["birth_date"])

my_dict["height"] = "175cm"
my_dict["is_married"] = False
my_dict["country_info"] = country_info
my_dict['skills'] = skills_list
my_dict['characteristics'] = characteristics

my_dict["skills"].append("hacking")

my_dict["country_info"]["country_name"] = "Peru"
my_dict["country_info"]["region"] = "Unknown"

my_dict["country_info"]["citizenship"] = "Peru Republic"

print(my_dict)


marks = {'Physics':67, 'Maths':87}

my_dict_items = list(my_dict.items())

print(my_dict_items)


print(my_dict.values())

for key in my_dict.values():
    print(key)

marks = {'Physics':67, 'Maths':87}
internal_marks = {'Physics': 48}

marks.update(internal_marks)


print(marks)
