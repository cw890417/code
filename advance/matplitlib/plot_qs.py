import matplotlib.pyplot as plt

x_data = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
y_data = ['2000', '2000', '3500', '6000', '8000', '12000', '16000']
y_data1 = ['3000', '4000', '5000', '7000', '9000', '13000', '26000']
plt.plot(x_data, y_data1)
plt.plot(x_data, y_data)
plt.show()
