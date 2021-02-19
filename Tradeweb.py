
def is_pal(var): 
    """check if palendrome"""
    var = str(var)
    word = var.reverse() 
    
    return word == var



# def main(): 
#     input = "text"
#     input2 = 1221
#     is_pal(input)

# main()


def palindrome(word): 
    if isinstance(word, int):
        word = str(word)
    print(type(word))
    reverse = word[::-1]
    print(reverse)
    half_word = len(word)//2 + 1
    half_reverse = len(reverse)//2 + 1
    print(half_word)
    return word[:half_word] == reverse[:half_reverse]

def main(): 
    #word = "string"
    #word = 1221
    word = [1,2,4,4,2,1]
    print(palindrome(word))

main()