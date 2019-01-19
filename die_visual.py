from die import Die

import pygal

die = Die()

results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
	frequeny = results.count(value)
	frequencies.append(frequeny)

hist = pygal.Bar()
hist.title = "rolling one  D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "result"
hist.y_title = "frequeny result"

hist.add('D6',frequencies)
hist.render_to_file('/Users/chenwei/code/data/aaa.svg')
