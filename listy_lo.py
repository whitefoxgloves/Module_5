if __name__ == "__main__":
    
    # Line breaks have been added for readability

    # List of food
    food = ['rice', 'beans']
    food.append('broccoli')
    food.extend(['bread', 'pizza'])
    print(food[:2])
    print(food[-1])
    print('\n')

    # Breakfast list
    bfast_string = "eggs,fruit,orange juice"
    bfast_list = bfast_string.split(",")
    print(f'Number of elements in breakfast: {len(bfast_list)}')
    print('\n')

    # Get float(s) and print avg, min, and max
    num_list = []
    while True:
        value = input('Enter a value or type "stop": ')
        if value == 'stop':
            break
        floats = float(value)
        num_list.append(floats)

    print(f'Average: {sum(num_list) / len(num_list)}')
    print(f'Min value: {min(num_list)}')
    print(f'Max value: {max(num_list)}')