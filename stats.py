def count_words(contents: str):
    words = contents.split()
    print(f"Found {len(words)} total words")
    
def count_unique_characters(contents: str):
    count = {}
    for content in contents:
        if (content.lower() in count):
            count[content.lower()] += 1
        else:
            count[content.lower()] = 1
    return count

def sort_on(items):
    return items["num"]

def sort_unique_characters(counts: object):
    count_list = []
    for count in counts:
        if(count.isalpha()):
            count_list.append({"char": count, "num": counts[count]})
    count_list.sort(reverse=True, key=sort_on)
    return count_list