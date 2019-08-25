def is_integer_palindrome(num: int) -> bool:
    if num < 0:
        return False

    num_str = str(num)
    while num_str:
        if num_str[0] != num_str[-1]:
            return False
        num_str = num_str[1:len(num_str)-1]
    return True

test_cases = [
    (0, True),
    (11, True),
    (121, True),
    (-1, False),
    (12, False),
    (100, False),
    (2147483647, False)
]

if __name__ == '__main__':
    for inp, out in test_cases:
        print("Testing:", inp, out)
        print("The result is {}".format(is_integer_palindrome(inp)))
        print()