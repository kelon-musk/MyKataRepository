'''
Challenge name:-


Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'


Given Tests:-

test.describe('to_weird_case')

test.it('should return the correct value for a single word')
test.assert_equals(to_weird_case('This'), 'ThIs')
test.assert_equals(to_weird_case('is'), 'Is')

test.it('should return the correct value for multiple words')
test.assert_equals(to_weird_case('This is a test'), 'ThIs Is A TeSt')


'''

def to_weird_case(string):
    Bean=""
    F=True
    for char in string:
        if F :    
            Bean += char.upper()
            F=False
        else :
            Bean += char.lower()
            F=True
        if char == ' ' :
            F=True
        
    return Bean
    
def main():
    bean=to_weird_case("BEANS ARE GOOD")   
    print(bean)

if __name__ == "__main__":
    main()
   
    
