import pandas as pd

def gps(path):
    if path == '001':
        print('Navigating to location 1...')
        return False
    elif path == '002':
        print('Navigating to location 2...')
        return False
    elif path == '003':
        print('Navigating to location 3...')
        return False
    elif path == '004':
        print('Navigating to location 4...')
        return False
    else:
        print('Invalid location')
    return True

if __name__ == '__main__':
    gps(decoded_text)
