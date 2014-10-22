def moving_average(dataset, points):
    ma = []
    data_len = len(dataset)

    for current in range(data_len - points + 1):
        average = sum(dataset[current:current+points]) / points
        ma.append(average)

    return ma
