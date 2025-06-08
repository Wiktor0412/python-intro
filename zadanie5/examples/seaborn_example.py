import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")
plt.title("Wykres rozrzutu - Seaborn")
plt.show()
