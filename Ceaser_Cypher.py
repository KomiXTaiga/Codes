def encode():
    r = input("Please enter a word to encode: \n")
    n = int(input("How many letters over would you like to shift the word \n"))
    n = n % 26
    lst = list(r)
    alphabnet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a', "A", "B", "C", "D", "E", "F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    word = []
    tmp = 0
    for i in range(len(lst)):
        letter = lst[tmp]
        if letter in alphabnet:
            alphabnet_letter = alphabnet.index(letter)
            tmp_2=alphabnet[alphabnet_letter+n]
            word.append(tmp_2)
            tmp += 1
        else:
            word.append(letter)
            tmp+=1
    return word
def decode():
    r = input("Please enter a word to decode \n")
    n = int(input("How manmy letter did yous shift the word over\n"))
    n = n % 26
    lst = list(r)
    alphabnet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "A", "B", "C", "D", "E", "F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    word = []
    tmp = 0
    for i in range(len(lst)):
        letter = lst[tmp]
        if letter in alphabnet:
            alphabnet_letter = alphabnet.index(letter)
            tmp_2 = alphabnet[alphabnet_letter - n]
            word.append(tmp_2)
            tmp += 1
        else:
            word.append(letter)
            tmp += 1
    return word
def list_to_string(lst):
    str = ""
    for ele in lst:
        str += ele
    print(str)
if __name__ == "__main__":
    y = True
    while y == True:
        x = input("Would you like to encode or decode a word? (E/D)?\n").upper()
        if x == 'E':
            list_to_string(encode())
        elif x == 'D':
            list_to_string(decode())
        else:
            print("TF are u talking about?")
        keep_open = input("Would you like to run this shit again? Y/N?\n").upper()
        if keep_open == 'Y':
            continue
        elif keep_open == 'N':
            break
        else:
            print("What? Im going to restart now k")

