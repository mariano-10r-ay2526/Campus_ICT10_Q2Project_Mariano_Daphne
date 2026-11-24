from pyscript import display, document

creator = {
    'name': 'Daphne Annika Mariano',
    'interests': 'I love listening to music. I enjoy cooking my favorite food and spending time with family and friends.',
    'dreams': "My goal in life is to be successful. One day, I would like to dominate Computer Science based careers.",
    'quote': 'To love and lose and still be kind. -Warsan Shire'
}

sections = {
    'About Me': creator['name'],
    'Interests': ', '.join(interests),
    'Dreams': ', '.join(dreams),
    'Quote': ', '.join(quote),
}

display(creator['name'], target='output')
display(creator['interests'], target='output')

for title in sections:
    display(title, target='div1')
    display(sections[title], target='div1')

display(f'“{creator["quote"]}”', target='output')
