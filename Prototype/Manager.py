from Property import Property

initial_property = Property('Stefan cel Mare 59', 3, 250000)


new_property = initial_property.clone()

new_property.address = 'Alexandru cel Bun 59'
new_property.rooms = 2
new_property.price = 89000


print('Initial property:')
print(f'Address: {initial_property.address}')
print(f'Rooms: {initial_property.rooms}')
print(f'Price: {initial_property.price}\n')


print('New property:')
print(f'Address: {new_property.address}')
print(f'Rooms: {new_property.rooms}')
print(f'Price: {new_property.price}')
