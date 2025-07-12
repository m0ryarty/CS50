input_item = input('Item: ').lower()

nutrition = [
    {
        "item":"Apple",
        "cal": 130
    },
    {
        "item": "Banana",
        "cal": 110
    },
    {
        "item": "Avocado",
        "cal": 50
    },
    {
        "item": "Cantaloupe",
        "cal": 50
    },
    {
        "item": "Grapefruit",
        "cal": 60
    },
    {
        "item": "Grapes",
        "cal": 90
    },
    {
        "item": "Honeydew Melon",
        "cal": 50
    },
    {
        "item": "Kiwifruit",
        "cal": 90
    },
    {
        "item": "Lemon",
        "cal": 15
    },
    {
        "item": "Nectarine",
        "cal": 60
    },
    {
        "item": "Orange",
        "cal": 80
    },
    {
        "item": "Peach",
        "cal": 60
    },
    {
        "item": "Pineapple",
        "cal": 50
    },
    {
        "item": "Strawberries",
        "cal": 50
    },
    {
        "item": "Sweet Cherries",
        "cal": 100
    },
    {
        "item": "Tangerine",
        "cal": 50
    },
    {
        "item": "Watermelon",
        "cal": 80
    },
    {
        "item": "Lime",
        "cal": 20
    },
    {
        "item": "Pear",
        "cal": 100
    },
    {
        "item": "Plums",
        "cal": 70
    },
]

for item in nutrition:
    if item['item'].lower() == input_item:
        print('Calories:', item['cal'])
