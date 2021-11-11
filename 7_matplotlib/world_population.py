import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1975, 1980, 1985, 1990, 1995,
         2000, 2005, 2010, 2015]

pops = [2.525, 2.758, 3.018, 3.322, 3.682, 4.061, 4.440, 4.853,
        5.310, 6.127, 6.520, 6.930, 7.349]

deaths = [.8, 1.2, 1.7, 2.2, 2.5, 2.7, 1.8, 1.6, 3.1, 2.4, 2.7, 3.9, 4.2]


def main():
    plt.plot(years, pops, '--', color=(1, .5, .5))
    plt.plot(years, deaths, color=(.6, .6, 1))
    plt.ylabel("Population in billions")
    plt.xlabel("Population growth by year")
    plt.title("Population growth")

    plt.show()


if __name__ == "__main__":
    main()
