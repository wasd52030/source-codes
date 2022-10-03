from sklearn import datasets
from matplotlib import pyplot
import pandas
import os

data = None


def hist_alcohol():
    global data
    pyplot.hist(data['alcohol'])
    pyplot.xlabel('alcohol')
    pyplot.savefig("./plots/hist_alcohol.png")
    pyplot.cla()


def bar_malic_acid():
    global data
    malic_acid = [len(data["malic_acid"][(data["Classes"] == "class_0")]),
                  len(data["malic_acid"][(data["Classes"] == "class_1")]),
                  len(data["malic_acid"][(data["Classes"] == "class_2")])]
    pyplot.bar(range(len(malic_acid)), malic_acid)
    pyplot.xticks(range(len(malic_acid)), ["class_0", "class_1", "class_2"])
    pyplot.xlabel('classes of malic_acid')
    pyplot.savefig("./plots/bar_malic_acid.png")
    pyplot.cla()


def pie_ash():
    global data
    malic_acid = [len(data["ash"][(data["Classes"] == "class_0")]),
                  len(data["ash"][(data["Classes"] == "class_1")]),
                  len(data["ash"][(data["Classes"] == "class_2")])]
    pyplot.pie(
        malic_acid,
        labels=["class_0", "class_1", "class_2"],
        autopct="%0.2f%%"
    )
    pyplot.xlabel('classes of ash')
    pyplot.savefig("./plots/pie_ash.png")
    pyplot.cla()


def boxplot_alcalinity_of_ash():
    global data
    pyplot.boxplot(
        [data['alcalinity_of_ash'][(data["Classes"] == "class_0")],
         data['alcalinity_of_ash'][(data["Classes"] == "class_1")],
         data['alcalinity_of_ash'][(data["Classes"] == "class_2")]],
        vert=False,
        labels=["class_0", "class_1", "class_2"],
    )

    pyplot.xlabel('classes of alcalinity_of_ash')
    pyplot.savefig("./plots/boxplot_alcalinity_of_ash.png")
    pyplot.cla()


def scatter__ash_and__alcalinity_of_ash():
    global data
    pyplot.scatter(data["ash"], data['alcalinity_of_ash'])
    pyplot.xlabel('ash')
    pyplot.ylabel('alcalinity_of_ash')
    pyplot.savefig("./plots/scatter__ash_and__alcalinity_of_ash.png")
    pyplot.cla()


def main():
    global data

    if not os.path.exists('./plots'):
        os.mkdir('./plots')

    if not os.path.exists('./reports'):
        os.mkdir('./reports')

    wine = datasets.load_wine()

    a = pandas.DataFrame(wine['data'], columns=wine['feature_names'])
    b = pandas.DataFrame(
        [wine['target_names'][i] for i in wine['target']],
        columns=['Classes']
    )
    data = pandas.concat([a, b], axis=1)
    data.to_csv('./reports/data.csv', index=False)
    data.describe().to_csv('./reports/basic_stat_describe.csv')

    hist_alcohol()
    bar_malic_acid()
    boxplot_alcalinity_of_ash()
    scatter__ash_and__alcalinity_of_ash()
    pie_ash()


main()
