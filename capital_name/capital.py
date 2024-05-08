def capitalize_name(full_name):
    words = full_name.split("  ")
    capitalized_words = [word.capitalize() for word in words]
    capitalized_name = ' '.join(capitalized_words)

    return capitalized_name

full_name = input()
capitalized_name = capitalize_name(full_name)
print(capitalized_name)