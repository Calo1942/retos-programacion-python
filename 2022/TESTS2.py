def isPalindrome(x: int) -> bool:
    x_str = str(x)
    number_reverse = ""
    while x_str != "":
        number_reverse += x_str[-1]
        x_str = x_str[:-1]
    if number_reverse == x_str:
        return True
    else:
        False

isPalindrome(127)