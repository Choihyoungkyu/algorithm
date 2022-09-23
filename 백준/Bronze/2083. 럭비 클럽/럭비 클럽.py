while True:
    name, age, weight = input().split()
    if int(age) > 17 or int(weight) >= 80:
        result = 'Senior'
    else:
        result = 'Junior'
    if name == '#':
        break
    print(f'{name} {result}')