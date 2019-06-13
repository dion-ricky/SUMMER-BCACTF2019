#!/usr/bin/python3

def read_file(f):
    retr = []
    with open(f, 'r') as _f:
        retr = _f.read().split('\n')

    return retr

def is_viable(s):
    if len(s) % 3 == 0:
        if '&' not in list(s):
            return True
    return False

def get_nth_char(c, n):
    return list(c)[int(n)-1]

def get_flag(f):
    file = read_file(f)
    num = file[0].split(' ')
    flag = []
    for i in file[1:]:
        if len(num) > 0:
            if is_viable(i):
                flag.append(get_nth_char(i, num[0]))
                num = num[1:]

    print(''.join(flag))

if __name__ == '__main__':
    get_flag('flag.txt')
