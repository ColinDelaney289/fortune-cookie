# TechPrep Python Project One
# Question One – Random Number Generator
# "Fortune Cookie"

import random

fortunes = [
    'All the effort you are making will ultimately pay off.',
    'An acquaintance of the past will affect you in the near future.',
    'Determination is what you need now.',
    'Do not let ambitions overshadow small success.',
    'Do not let the past and useless detail choke your existence.',
    'Emulate what you respect in your friends.',
    'Good news will come to you by mail.',
    'It is time to get moving. Your spirits will lift accordingly.',
    'Now is the time to try something new.',
    'Say hello to others. You will have a happier day.',
    'You have the power to write your own fortune.',
    'Your ideals are well within your reach.',
    'The early bird gets the worm, but the second mouse gets the cheese.',
    'The fortune you seek is in another cookie.',
    'Be on the alert to recognize your prime at whatever time of your life it may occur.',
    'Tension is who you think you should be. Relaxation is who you are.',
    'Everyone seems normal until you get to know them.',
    'A closed mouth gathers no feet.',
    'Inside every old person is a young person wondering what the hell happened.',
    'You are cleverly disguised as a responsible adult.',
    'You think it is a secret, but they know.',
    'You will die alone and poorly dressed.',
    'Courage is not the absence of fear; it is the conquest of it.',
    'All things are difficult before they are easy.',
    'A ship in harbor is safe, but that\'s not why ships are built.',
    'He who laughs at himself never runs out of things to laugh at.',
    'If you want the rainbow, you have to tolerate the rain.',
    'Fear is interest paid on a debt you may not owe.',
    'To avoid criticism, do nothing, say nothing, be nothing.',
    'We don\'t know the future, but here\'s a cookie.',
    'A journey of a thousand miles begins with a single step.',
    'Of all our human resources, the most precious is the desire to improve.',
    'Do the thing you fear, and the death of fear is certain.',
    'Success is going from failure to failure without loss of enthusiasm.',
    'Do not let yesterday take up too much of today.',
    'All we have to decide is what to do with the time that is given to us.',
    'It is never too late to be what you might have been.',
    'Not all those who wander are lost.',
    'In every ending, there is a new beginning.',
    'Life shrinks or expands in proportion to one\'s courage.',
    'Ask yourself if what you are doing today is getting you closer to where you want to be tomorrow.',
    'Wise sayings often fall on barren ground, but a kind word is never thrown away.',
    'It\'s dangerous to go alone! Take this fortune.'
]

# Pull a random fortune from the list
random_number = random.randrange(0,len(fortunes),1) 
your_fortune = fortunes[random_number]

# Put together a list of 4 random unique lucky numbers
lucky_num_set = set()
lucky_min = 1
lucky_max = 99
while len(lucky_num_set) < 4:
    lucky_num = random.randint(lucky_min,lucky_max)
    lucky_num_set.add(lucky_num)

print(your_fortune)
print('Lucky numbers:', end=" ") 
for lucky_num_set_item in sorted(lucky_num_set):
    print(lucky_num_set_item, end=" ") 