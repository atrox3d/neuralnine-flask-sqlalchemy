import ss1
import ss2

from singleton_store import SingletonStore as ss

print(ss.get('name'))
print(ss.get('age'))

try:
    ss.add_values(name='john')
except:
    ss.add_values(x='bob')
