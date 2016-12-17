D = {'arrow': 4, '1' : 1, 'bi' : 2, '007': 7, 'abc':4}

key_list = D.keys()

key_list = sorted(key_list)

for key in key_list :
    print ('%s\t%d' % (key, D[key]))