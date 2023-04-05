from Property import Property

initial_property = Property('X Street, No. 10', 3, 250000)


new_property = initial_property.clone()


new_property.address = 'Y Street, No. 20'
new_property.rooms = 2
new_property.price = 200000


print('Initial property:')
print(f'Address: {initial_property.address}')
print(f'Number of rooms: {initial_property.rooms}')
print(f'Price: {initial_property.price}\n')


print('New property:')
print(f'Address: {new_property.address}')
print(f'Number of rooms: {new_property.rooms}')
print(f'Price: {new_property.price}')
