def bracket_matcher(str):
    # print(f'++ {str} ++')
    matches = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    brackets = ['[', ']', '{', '}', '(', ')']

    # stack
    unmatched = []

    for char in str:
        # print(unmatched)
        if not char in brackets:
            continue

        if char in matches.keys():
            # if it is an opening bracket
            # add it to the stack and continue
            unmatched.append(char)
        else:
            # if it is a closing bracket
            # if the stack is empty, return False
            if len(unmatched) == 0:
                print(
                    f'{str}  =>  False :: closing bracket "{char}" has no matching opening bracket')
                return False
            # pop off the top of the stack and see if it matches
            top = unmatched.pop()
            if matches[top] != char:
                print(
                    f'{str}  =>  False  ::  closing "{char}" does not match opening "{top}"')
                return False

    if len(unmatched) > 0:
        print(f'{str}  =>  False  ::  unmatched opening brackets: {unmatched}')
    else:
        print(f'{str}  =>  True')

    return len(unmatched) == 0


bracket_matcher('abc(123)')
print('Should be True\n')
# returns true

bracket_matcher('a[b]c(123')
print('Should be False\n')
# returns false -- missing closing parens

bracket_matcher('a[bc(123)]')
print('Should be True\n')
# returns true

bracket_matcher('a[bc(12]3)')
print('Should be False\n')
# returns false -- improperly nested

bracket_matcher('a{b}{c(1[2]3)}')
print('Should be True\n')
# returns true

bracket_matcher('a{b}{c(1}[2]3)')
print('Should be False\n')
# returns false -- improperly nested

bracket_matcher('()')
print('Should be True\n')
# returns true

bracket_matcher('[]]')
print('Should be False\n')
# returns false - no opening bracket to correspond with last character

bracket_matcher('abc123yay')
print('Should be True\n')
# returns true -- no brackets = correctly matched
