def replace(string, from_str, to_str):
    new_string = string
    while from_str in new_string:
        first_half = new_string[:new_string.find(from_str)]
        second_half = new_string[new_string.find(from_str) + len(from_str):]
        new_string =  first_half + to_str + second_half
    return new_string

print(replace("Are we out of the _____ yet?", "_____", "woods"))