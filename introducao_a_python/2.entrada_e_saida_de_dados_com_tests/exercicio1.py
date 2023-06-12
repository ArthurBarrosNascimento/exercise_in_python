def write_the_opposite_name(name):
    for removed_letters in range(len(name)):
        for index in range(len(name) - removed_letters):
            print(name[index], end='')
        print()


if __name__ == '__main__':
    name = str(input('Digite seu nome: '))
    write_the_opposite_name(name)
