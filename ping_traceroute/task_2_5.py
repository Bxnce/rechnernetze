import matplotlib.pyplot as plt


def extract_data(file_name):
    with open(file_name, 'r', encoding='UTF-16') as file:
        data = []
        for line in file.readlines():
            if 'Zeit' in line:
                for part in line.split(' '):
                    if 'Zeit' in part and not 'Zeitangaben' in part:
                        data.append(part.split('=')[1].replace('ms', ''))
        return data


def plot_data(data, title):
    # plot the data of the array without pyplot
    plt.plot(data)
    plt.title(title)
    plt.savefig(title + '.png')
    plt.show()


if __name__ == "__main__":
    data_set = ['htwg_au.txt', 'htwg_tur.txt', 'ping_uw.txt']
    for data in data_set:
        plot_data(extract_data(data), data)
