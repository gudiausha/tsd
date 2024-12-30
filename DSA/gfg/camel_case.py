# https://www.geeksforgeeks.org/camel-case-given-sentence/
# Input: “i got intern at geeksforgeeks”
# Output: “IGotInternAtGeeksforgeeks”


# Input: “here comes the garden”
# Output: “HereComesTheGarden”

def camel_case(input_str):
    output = ''
    input_str_list = input_str.split()
    for word in input_str_list:
        first_letter = word.pop(0)
        word = first_letter.upper() + word
        output+=word
    print(output)

camel_case("i got intern at geeksforgeeks")