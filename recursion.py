lisBranches = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
def count_leaf_items(item_list):
    print(f"List: {item_list}")
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items(item)
        else:
            print(f"Counted leaf item \"{item}\"")
            count += 1
            print(f"Count: {count}")

    print(f"-> Returning count {count}")
    return count

count_leaf_items(lisBranches)