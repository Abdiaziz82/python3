# Python Dictionary Demonstration - Creating, accessing, and manipulating dictionaries

# Basic dictionary creation and type checking
my_dictionary = {
    "key1" : "value1",
     "key2": "value2"  
}
print(type(my_dictionary))        # Shows dictionary type
print(my_dictionary["key1"])      # Access value by key

# Contact management using dictionary
saved_contacts = {
    "abdullahi": "0722345678",
    "halima": "0722345678",
    "ahmed": "0722345678",
    "ahmedA": "0722345677"
}

print(saved_contacts)                                    # Print entire dictionary
print(saved_contacts["halima"])                          # Access specific contact
saved_contacts["ibrahim"] = "0722345678"                 # Add new contact
print(saved_contacts.get("abdoo" , "key not found"))    # Safe access with default value
print(saved_contacts.keys())                             # Get all keys (names)
print(saved_contacts.values())                           # Get all values (phone numbers)
print(saved_contacts.items())                            # Get key-value pairs

# Different ways to update dictionary
saved_contacts.update({"ismail" : "0722345678" , "iqra" : "097644" , "abdiaziz" : "0987544"})  # Add multiple items
saved_contacts.update({"halima": "0972225414516"})       # Update existing contact
saved_contacts.update([("john" ,"098665") , ("hh" , "9076618")])  # Update with list of tuples
saved_contacts.pop("abdullahi")                          # Remove contact by key

print(saved_contacts)

# Loop through dictionary items
for key , value in saved_contacts.items():
    print(key , value)

# Nested dictionary example 
Buses_in_Garissa = {
    "G-coach" : {
        "seats" : 90,
        "price" :1500,
        "route": "Garissa to Nairobi",
        "driver": {
            "name":"abdiaziz",
            "email" : "abbdhjdi@gamil.com"
        }  
    } ,
    "Alma": {
        "seats" : 70,
        "price" :1200,
        "route": "Garissa to Wajir",
        "driver": {
            "name":"aden",
            "email" : "abbd@gamil.com"
        }
    },
    "Rayan" : {
        "seats" : 60,
        "price" :1300,
        "route": "Garissa to Wajir",
        "driver": {
        "name":"ibrahim",
         "email" : "ibrahim@gamil.com"
        }
    }
}

# Access nested dictionary values
print(Buses_in_Garissa["G-coach"]["price"])              # Get bus price
print(Buses_in_Garissa["G-coach"]["driver"]["email"])    # Get driver's email

# Loop through nested dictionary
for key, value in Buses_in_Garissa.items():
    print(f"bus name : {key} ")
    driver = value["driver"]["name"]
    print(f"driver name is {driver}")