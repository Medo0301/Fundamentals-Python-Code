def get_substrings(substrings: list, full_words: list):
    result = []
    for substr in substrings:
        substrings_word = [substr for word in full_words if substr in word]
        if len(substrings_word) > 0:
            result.append(substr)
    return result


first_list = input().split(", ")
second_list = input().split(", ")

final_result = get_substrings(first_list, second_list)
print(final_result)