def magic_string():
    iterations = 10
    return ''.join(['BestSchool' + str(i) for i in range(1, iterations + 1)])


print(magic_string())

