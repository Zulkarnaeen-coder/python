import matplotlib.pyplot as plt

days = ["SAT","SUN","MON","TUES","WED","THURS","FRI"]
score = [68,97,45,78,86,85,100]

plt.plot(days,score)
plt.show()

plt.plot(days,score,color="red",marker="o",linestyle = "dashed",linewidth = 2)
plt.title("My Quiz traker")
plt.ylabel("Scores")
plt.xlabel("Days")
plt.ylim(0,100)
plt.grid(True)
plt.show()

plt.bar(days,score,color = "orange")
plt.ylabel("Score")
plt.xlabel("Days")
plt.ylim(0,100)
plt.show()