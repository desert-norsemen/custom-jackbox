smile = ':)'
nameston = ['Matthew Michael Morris', 'Jordan Daniel Cooper', 'Taylor f@#*&$&% Earl', 'Benjamin Bud Beveridge', 'yikes']

for name in nameston:
    for character in name:
        if character != ' ':
            print(smile, end='')
        else:
            print('    ', end='')

    print ('')