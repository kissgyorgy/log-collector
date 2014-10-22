def moving_average(dataset, points):
    ma = []
    data_len = len(dataset)

    average = sum(dataset[:points]) / points
    ma.append(round(average, 5))
    for first_of_set in range(data_len - points):
        next = first_of_set + points
        first_of_set_average = dataset[first_of_set] / points
        next_average = dataset[next] / points
        average = average - first_of_set_average + next_average
        ma.append(round(average, 5))

    return ma
