import json
import os

# Function to load verses from JSON file
def load_verses_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    return data

# Function to search verse in JSON data
def search_verses_in_json(verses, chapter_num, start_verse, end_verse):
    try:
        for verse in verses:
            if verse['abbrev'] == 'gn':
                chapter = verse['chapters'][int(chapter_num) - 1]
                if start_verse.lower() == 'all':
                    start_verse = 1
                    end_verse = len(chapter)
                else:
                    start_verse = int(start_verse)
                    if end_verse.lower() == 'all':
                        end_verse = len(chapter)
                    else:
                        end_verse = int(end_verse)
                if start_verse < 1 or end_verse > len(chapter) or start_verse > end_verse:
                    return "Invalid verse range."
                return "\n".join(chapter[start_verse - 1:end_verse])
    except (IndexError, ValueError):
        return "Verse not found."

#def main():
#    search_input = input("Enter search query (lang abrev chap start-verse end-verse/all): ")
#    search_parts = search_input.split()
#
#    if len(search_parts) == 5:
#        lang_abrev, book_abrev, chapter_num, start_verse, end_verse = search_parts
#
#        file_path = os.path.join("json", f"{lang_abrev}_{book_abrev}.json")
#        if os.path.exists(file_path):
#            verses = load_verses_from_json(file_path)
#            result = search_verses_in_json(verses, chapter_num, start_verse, end_verse)
#            print(f"Verses {lang_abrev} {book_abrev} {chapter_num}:{start_verse}-{end_verse}:")
#            print(result)
#        else:
#            print("JSON file not found.")
#    else:
#        print("Invalid input format. Please provide lang abrev chap start-verse end-verse/all.")
#
#if __name__ == "__main__":
#    main()
