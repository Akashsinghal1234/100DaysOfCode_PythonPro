alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
if direction != "encode" or direction != "decode":
    print("sale pagal banata hai")
else:
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : "))


def ceasar(plain_text, numbers_of_shift, direction_of_code):
    new_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        if direction_of_code == "encode":
            new_position = position + numbers_of_shift
            new_text += alphabets[new_position]
        elif direction_of_code == "decode":
            new_position = position - numbers_of_shift
            new_text += alphabets[new_position]
    if direction_of_code == "encode":
        print(f"The encoded message is {new_text}.")
    else:
        print(f"The decoded message is {new_text}.")


if direction == "encode" or direction == "decode":
    ceasar(text, shift, direction)