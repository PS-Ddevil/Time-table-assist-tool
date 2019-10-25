def tlist(str):
    result = [x.strip(',') for x in str.split(' ')]
    return result[0]