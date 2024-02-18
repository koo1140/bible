import search
import os

def query(l, n, c, v, e):
    file_path = os.path.join("json", f"{l}_{n}.json")
    verses = search.load_verses_from_json(file_path)
    result = search.search_verses_in_json(verses, c, v, e)
    return result

print(query("en", "kjv", "1", "1", "1"))