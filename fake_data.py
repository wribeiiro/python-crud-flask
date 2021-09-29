import requests

fake_list = [
    {
        'name': 'Well1',
        'image': 'https://fakeimg.pl/250x100/',
        'description': 'Commodo sunt nisi in consequat. Et et ut laboris ex velit proident ex. Enim ex fugiat minim reprehenderit magna cupidatat non sint ullamco.',
        'link': 'https://wribeiiro.com'
    },
    {
        'name': 'Well1',
        'image': 'https://fakeimg.pl/250x100/',
        'description': 'Commodo sunt nisi in consequat. Et et ut laboris ex velit proident ex. Enim ex fugiat minim reprehenderit magna cupidatat non sint ullamco.',
        'link': 'https://wribeiiro.com'
    },
]

for fake in fake_list:
    response = requests.post('http://localhost:5000/catalog/add', data=fake)
    print(response.text)