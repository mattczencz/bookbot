def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = count_words(text)
  char_instances = count_character_instances(text)
  sorted_chars_list = chars_instances_to_sorted_list(char_instances)
  create_report(book_path, num_words, sorted_chars_list)


def count_words(text: str):
  return len(text.split())


def get_book_text(path):
  with open(path) as f:
    return f.read()


def count_character_instances(text: str):
  instances = {}
  for word in text:
    lowered = word.lower()
    # for each character in the lower cased word
    for char in lowered:
      # if the charector is not set in the instances dictionary
      if char not in instances:
        instances[char] = 1 # set it
      else:
        instances[char] += 1 # otherwise increment it
  return instances


def sort_on(dict):
  return dict["num"]


def chars_instances_to_sorted_list(char_instances):
    sorted_list = []
    # for each instance in char_instances
    for ch in char_instances:
        sorted_list.append({"char": ch, "num": char_instances[ch]}) # append the reformated dict
    sorted_list.sort(reverse=True, key=sort_on) # then sort the list
    return sorted_list


def create_report(path, word_count, instances):
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document")
  print("\n")

  for item in instances:
    if item["char"].isalpha():
      print(f"The '{item["char"]}' character was found {item["num"]} times")

  print("--- End report ---")


main()