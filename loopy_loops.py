if __name__ == "__main__":
    
    # Line breaks have been added for readability

    # Pokemon and tuples
    pokemon = ('picachu', 'charmander', 'bulbasaur')
    print(pokemon[1])
    starter1, starter2, starter3 = pokemon
    print('\n')

    # Creating tuple from name and checking for 'i'
    my_name = tuple('Kathy Lai')
    print(f'Is the letter i in my name? {"i" in my_name}')
    print('\n')

    # For loop that prints integers 2 through 10
    for i in range(2, 11):
        print(i)
    print('\n')

    # While loop that prints integers 2 through 10
    j = 2
    while j < 11:
        print(j)
        j += 1
    print('\n')

    # For loop that iterates over a string
    string = 'This is a simple string'
    for char in string:
        print(char)
    print('\n')

    # Nested loop that prints each word thrice
    simple_set = ('this', 'is', 'a', 'simple', 'set')
    for word in simple_set:
        for i in range(3):
            print(word)