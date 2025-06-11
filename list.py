# Initialize a shopping bag list with various items
shopping_bag = ["laptop" ,"clothes" ,"shoes","laptop",
                "books" ,"Tv", "phone","shirts"
                ]

# Get the length of the list
print(len(shopping_bag))
# Result: 8

# Reverse the list using slicing (creates a new reversed list)
print(shopping_bag[::-1])
# Result: ['shirts', 'phone', 'Tv', 'books', 'laptop', 'shoes', 'clothes', 'laptop']

# append() modifies the list in-place and returns None
print(shopping_bag.append("charger"))
# Result: None but added the value at the end

# Replace the last item with "gggg"
shopping_bag[len(shopping_bag) -1] = "gggg"

# Print current state of shopping_bag
print(shopping_bag)

# Insert items at specific positions
shopping_bag.insert(0 ,"watch")        # Insert at beginning
shopping_bag.insert(8 ,"wa")           # Insert at index 8
shopping_bag.insert(18 ,"chair")       # Insert at end (index 18 > list length)

# Sort the list in-place (alphabetically)
shopping_bag.sort()

# Create a new sorted list in reverse order (doesn't modify original)
sorted_shopping = sorted(shopping_bag , reverse=True)
print(sorted_shopping)
# Count occurrences of "laptop" in the list
print(shopping_bag.count("laptop"))
# Result: 2

# Add multiple items to the end of the list
shopping_bag.extend(["trouser" ,"flash"])

# Create a shallow copy of the list
coppied = shopping_bag.copy()
# Modify the copy (original remains unchanged)
coppied[1] ="new_clothes"
print(coppied)
# Original list is unchanged
print(shopping_bag)

# Remove first item and "shoes" from the list
shopping_bag.pop(0)            # Remove first item
shopping_bag.remove("shoes")   # Remove first occurrence of "shoes"
print(shopping_bag)


# LIST COMPREHENSION EXAMPLES

# Traditional loop approach to convert USD to KSH
amount_in_usd = [12,34,56,76]
amount_in_ksh = []

for amount in amount_in_usd:
    converted_amount = amount * 120  # Convert USD to KSH 
    amount_in_ksh.append(converted_amount)
    
print(amount_in_ksh)
# Result: [1440, 4080, 6720, 9120]

# List comprehension - creates a list in memory
amount_in_ksh = [amount * 120 for amount in amount_in_usd ]

# Generator expression - creates a generator object (lazy evaluation)
amount_in_ksh_gen = (amount * 120 for amount in amount_in_usd)

print(amount_in_ksh)
# Result: [1440, 4080, 6720, 9120]

print(amount_in_ksh_gen)
# Result: <generator object <genexpr> at 0x...>

# Iterate through generator (values generated on-demand)
for gen in amount_in_ksh_gen:
    print(gen)
# Result: 
# 1440
# 4080
# 6720
# 9120

# Compare memory usage: list vs generator
print(sys.getsizeof(amount_in_ksh))    # List stores all values in memory
# Result: 104 (bytes)

print(sys.getsizeof(amount_in_ksh_gen)) # Generator stores only the logic
# Result: 112 (bytes, but this is just the generator object overhead)