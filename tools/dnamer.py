import os
import re

season = 0


def place_quote(name):
    '''
    [01] => S<season>E<name>,
    only replace the first dir
    '''
    global season
    if not season:
        season = int(input('Input season: '))
    m = re.search('\[(?P<ep>[0-9][^\[\]]*)\]', name)
    if m:
        ep = m.group('ep')
        return name.replace(f'[{ep}]', f'S{season}E{ep} ')
    else:
        return name


def rid_quote(name):
    '''
    [xxx] => None
    Get rid of quotes
    '''
    return re.sub(r'\[[^\[\]]*\]', '', name)


def point_trip(name):
    t = [i.strip() for i in name.split('.')]
    return '.'.join(t)


def entry():
    dirs = os.listdir()
    rules = [place_quote, rid_quote, point_trip]
    perform = []

    for name in dirs:
        new_name = name
        for r in rules:
            new_name = r(new_name).strip()
        perform.append((name, new_name))

    print('---------------- Summaring -----------------')
    for res in perform:
        print(res[0], '=>', res[1])
    print('--------------------------------------------')

    c = input('Affect? [Y/n]: ')
    if c in ['', 'Y', 'y']:
        for res in perform:
            os.rename(res[0], res[1])
        print('Done.')
    else:
        print('Canceled.')


if __name__ == '__main__':
    entry()
