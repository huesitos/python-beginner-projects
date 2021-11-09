import matplotlib.pyplot as plt


def main():
    labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
    print(type(labels))
    sizes = [33, 52, 12, 17, 62, 48]
    separated = (0, 0, 0, 0, .2, 0)

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
    plt.show()
    plt.axis('equal')


if __name__ == "__main__":
    main()
