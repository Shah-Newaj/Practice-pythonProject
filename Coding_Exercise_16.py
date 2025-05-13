person = ("Rahul", 25, 5.9)

print("Age:", person[1])

# print(person)

try:
    person[0] = "Newaj"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")

# person = ("Rahul", 25, 5.9)
# # Print the second element of the tuple
# print(f"Age: {person[1]}")
#
# # Attempt to change the name in the tuple (this will raise an error)
# try:
#     person[0] = "John"  # This will not work
# except Exception as e:
#     print(f"Error: {e} - Tuples are immutable.")