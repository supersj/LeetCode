import os
import platform
import logging
import itertools

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),'test.log')

print('Logging to', logging_file)
print(os.getenv('HOMEDRIVE'))
print(os.getenv('HOMEPATH'))
print(os.path.join('asd','ccc', 'aaaa'))
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
l = itertools.count();
for i in l:
    print(i)
    if  i == 3:
        break;

print(next(l))
hh = itertools.combinations([1,2,3,4,5],3)
for i in hh:
    print(i)
s = 'asd'
s.encode()
logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')


city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
             ('Anchorage', 'AK'), ('Nome', 'AK'),
             ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
            ]
def get_state(city_state):
    return city_state[1]

ll = itertools.groupby(city_list, get_state)

print(ll)
for l in ll:
        for i in l[1]:
            print(i)