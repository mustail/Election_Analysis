# mustafa practice

print("Hello World!")

print(5+2*3)
print(8//5)
print(8%5)
print(2**3)

# lists are mutable

counties = ["Arapahoe", "Denver", "Jefferson"]

print(counties[1])

print(counties[0])

# counties

print(counties[-2]) # second from the last!

# slicing
# list[start:end] returns a list containing a copy of the items in the list
# from  the starting index value up to, but NOT including, the ending index value.

# move item within a list
# move Denver to third place:
print(counties)
counties.insert(2,counties.pop(1))

print(counties)

# TUPLE
# tuple is like a list, but immutable.

counties_tuple = ("Arapahoe", "Denver", "El Paso")

print(counties_tuple,"the data type is",type(counties_tuple))

print(counties,"the data type is ",type(counties))

print(counties_tuple[1])

print(counties_tuple[:2])

# dictionaries are mutable.
# counties_dict = {key1:value1, key2:value2}
# values in a dictionary can be objects of any time: integers, floating-point decimals,
# strings, Boolean values, datetime values, and lists. (even dictionaries?)
# keys must be immutable objects, like integers, floating-point decimals, or strings.
# Keys cannot be lists or any other type of mutable object.


# if statement
if counties_tuple[1] == "Denver":
    print("Dogru")

if counties_tuple[2] != "Jefferson":
    print(counties_tuple[2] + " Olmadi")

# if else statement, dual alternative decision statement temperature ac
temperature = int(input("What is the current temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


# what is the score?

score = int(input("What is your test score?"))

if score >= 90:
    print("Your grade is an A.")
else:
    if score >= 80:
        print("Your grade is a B.")
    else:
        if score >= 70:
            print("Your grade is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print ("Your grade is an F.")

# in conditional

sehirler = ["Turgutlu", "Alasehir", "Selendi", "Salihli"]

if "Turgutlu" in sehirler:
    print("Turgutlu sehirler arasinda var.")
else:
    print("Turgutlu sehirler arasinda degil.")

if "Turgutlu" in sehirler and "Selendi" in sehirler:
    print("Hem Turgutlu hem de Selendi sehirler arasinda var.")
else:
    print("Problem var.")

# the while loop

x = 0
while x <= 5:
    print(x)
    x = x+1


# the for loop in lists and tuples

for sayi in range(10):
    print(sayi)

for sehir in sehirler:
    print(sehir)

for i in range(len(sehirler)):
    print("Bu da baska " + sehirler[i])

sehirler_dict = {"Turgutlu" : 90000, "Alasehir" : 80000, "Salihli" : 85000}

for sehir in sehirler_dict:
    print("Dictionary'den key'ler: " + sehir)

for zamazingo in sehirler_dict:
    print("Zamazingo ile deneme: " + zamazingo)

for county in sehirler_dict.keys():
    print("Keys() method ile deneme: " +county)

for hoppala in sehirler_dict.values():
    print("Bu da values() methodu ile values alimi " + str(hoppala))

for sehir in sehirler_dict:
    print(sehirler_dict[sehir])

for sehir in sehirler_dict:
    print("Bu da get() method ile " + str(sehirler_dict.get(sehir)))


for anahtar, deger in sehirler_dict.items():
    print("Bu anahtar: "+ anahtar + " Bu da deger: " + str(deger))


voting_data = [{"county": "Arapahoe", "registered_voters" : 422829},
                {"county": "Denver", "registered_voters" : 463353},
                {"county": "Jefferson", "registered_voters" : 432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]["county"])

print("Get the values from a list of dictionaries:")

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("retrieve the number of registered voters from each dictionary:")

for i in range(len(voting_data)):
    print(voting_data[i]["registered_voters"])

print("retrieve the same without using range method ")
for county_dict in voting_data:
    print(county_dict["registered_voters"])
