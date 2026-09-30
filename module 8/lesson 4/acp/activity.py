import matplotlib.pyplot as plt

saved = [200,215,490,300,100]
weeks = ["1","2","3","4","5"]
plt.plot(weeks,saved,color = 'green',marker = "o",linestyle= 'dashed',linewidth = 2)
plt.xlabel('Weeks')
plt.ylabel('Money')
plt.title("Savings from week 1 to 5")
plt.ylim(0,1000)
plt.grid(True)
plt.show()


plt.bar(weeks,saved,color = "blue")
plt.xlabel("Weeks")
plt.ylabel("Money")
plt.title("Savings from week 1 to 5")
plt.ylim(0,1000)
plt.show()
