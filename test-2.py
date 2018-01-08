data = {'user': 1, 'name': 'Max', 'three': 4}
is_admin = data.get('admin', True)



'''
try:
    is_admin = data['admin']
except KeyError:
    is_admin = False
'''

