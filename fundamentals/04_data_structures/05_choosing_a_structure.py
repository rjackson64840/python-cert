# CHOOSING THE RIGHT DATA STRUCTURE — quick reference
# ---------------------------------------------------
#
#              ORDERED?   MUTABLE?   DUPLICATES?   SYNTAX        LOOKUP BY
# list           yes        yes         yes        [1, 2, 3]     index
# tuple          yes        NO          yes        (1, 2, 3)     index
# dict           yes*       yes         keys: NO   {"a": 1}      key
# set            NO         yes         NO         {1, 2, 3}     (membership only)
# frozenset      NO         NO          NO         frozenset()   (membership only)
#
# * dict preserves insertion order since Python 3.7
#
# QUICK DECISION GUIDE:
#   Need order + ability to change?          -> list
#   Need a fixed sequence that won't change?  -> tuple
#   Need to look things up by a name/key?     -> dict
#   Need uniqueness or fast membership tests?  -> set
#   Need an immutable set (e.g. dict key)?     -> frozenset


# Same data, four structures — see how each behaves
data_list  = [1, 2, 2, 3]
data_tuple = (1, 2, 2, 3)
data_set   = {1, 2, 2, 3}            # -> {1, 2, 3}, duplicate dropped
data_dict  = {"a": 1, "b": 2}

print(data_list)    # [1, 2, 2, 3]
print(data_tuple)   # (1, 2, 2, 3)
print(data_set)     # {1, 2, 3}
print(data_dict)    # {'a': 1, 'b': 2}


# MUTABILITY SUMMARY — which can be changed after creation?
#   MUTABLE:   list, dict, set                  (can grow/shrink/change)
#   IMMUTABLE: tuple, frozenset, str, int,      (fixed once created)
#              float, bool, bytes
#
# Only IMMUTABLE types can be dict keys or set members (they must be hashable).
print({(1, 2): "tuple key works"})       # OK
# print({[1, 2]: "list key fails"})      # TypeError: unhashable type: 'list'


# CONVERTING between structures
nums = [3, 1, 2, 2, 3]
print(tuple(nums))      # (3, 1, 2, 2, 3)
print(set(nums))        # {1, 2, 3}
print(list(set(nums)))  # dedupe a list: [1, 2, 3]
print(sorted(set(nums)))# dedupe AND sort: [1, 2, 3]
