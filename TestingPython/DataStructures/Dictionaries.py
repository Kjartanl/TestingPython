# NOTE / keep in mind:
# - Keys are hashed, and stored in order of these hashes,
#   so the order of items in dictionaries may vary (and therefore 
#   also be PRINTED in a seemingly random order), even though
#   the key-value relations will remain stable. 
#
# - Using a hash map for lookup means dictionaries a little 
#   slower than regular lists for small sizes; for very long 
#   lists on the other hand, ref-lookups using hash tables 
#   may be faster. 
# - A key can be ALMOST anything (any object etc), but not 
#   un-hashable types such as a list. 

my_dict = {1: "a", 2: "b", 3: "c"}
print(my_dict)

print("Keys: %s" %my_dict.keys())

print("Values: %s" %my_dict.values())