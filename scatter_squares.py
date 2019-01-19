import matplotlib.pyplot as plt


#plt.scatter(2, 4, s = 200)

#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]
#plt.scatter(x_values,y_values)

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c = y_values)

plt.title("title squares",fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("squares of value", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 7)

plt.show()
