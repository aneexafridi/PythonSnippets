from matplotlib import pyplot as pt


Days = [1,2,3,4,5,6,7]
Temperature = [47, 36, 20, 30, 29, 49, 37]

pt.plot(Days,Temperature,marker='o',label='Temperature')
pt.legend(loc='lower right')
pt.xlabel('Days')
pt.ylabel('Temperature')
pt.title('Kohat Weather')

pt.grid()
pt.show()

