# for loop

float_list = []

for i in range(100):
    float_list.append(i * 100)

# list comprehension

float_list = [i * 100 for i in range(100)]

data_list = [1, 2, 3, 4, 5]


def process_incoming_data(data_list):
    temp = []
    for datum in data_list:
        temp.append(datum // 2 * 67 - 5)
    print(temp)
    return temp


def comprehension_process_incoming_data(data_list):
    print([(datum // 2 * 67 - 5) for datum in data_list])
    return [(datum // 2 * 67 - 5) for datum in data_list]


if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]
    process_incoming_data(data_list)
    comprehension_process_incoming_data(data_list)
