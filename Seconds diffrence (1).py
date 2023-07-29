
def converting_in_seconds(time):
    add = 0
    for i in range(3):
        if i == 0:
            add += time[i] * 60 * 60
        elif i == 1:
            add += time[i] * 60
        elif i == 2:
            add += time[i]
    return add

def difference_finder(time1, time2):
    return converting_in_seconds(time2) - converting_in_seconds(time1)

timef = list(map(int, input("Enter the First Date (in hours, minutes, seconds separated by spaces): ").split()))
times = list(map(int, input("Enter the Second Date (in hours, minutes, seconds separated by spaces): ").split()))

print("Time difference in seconds:", difference_finder(timef, times))
