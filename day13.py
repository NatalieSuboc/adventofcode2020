def find_earliest_bus(file):
    with open(file) as txt:
        time = int(txt.readline())
        buses = [int(bus) for bus in txt.readline().split(',') if bus is not 'x']
        shortest = [0, float('inf')] # bus number, time waiting
        for bus in buses:
            time_to_wait = bus - (time % bus)
            if shortest[1] > time_to_wait:
                shortest[1] = time_to_wait
                shortest[0] = bus
    return shortest[0] * shortest[1]
