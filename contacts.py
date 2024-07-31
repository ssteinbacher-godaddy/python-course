contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Soundwave', 'email': 'soundwave@example.com'},
        {'name': 'Megatron', 'email': 'megatron@example.com'},
        {'name': 'Starscream', 'email': 'starscream@example.com'}, 
        {'name': 'Unicron', 'email': 'unicron@example.com'},
    ]    
}
print('Student emails;')
for student in contacts['students']:
    print(student['email'])