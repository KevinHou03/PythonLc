def min_refuel_stops(F, d, stations):
    """
    Compute the minimum number of refueling stops needed to reach the destination F.

    :param F: int - Final destination point on the number line.
    :param d: int - Maximum distance the vehicle can travel on a full tank.
    :param stations: List[int] - List of station positions on the number line, sorted in ascending order.
    :return: int, List[int] - The minimum number of refueling stops and the list of stations where stops occur.
    """
    current_pos = 0
    stops = 0
    stop_list = []
    i = 0
    n = len(stations)

    # Travel until reaching the final destination
    while current_pos + d < F:
        # Find the furthest station we can reach
        last_reachable_station = None
        while i < n and stations[i] <= current_pos + d:
            last_reachable_station = stations[i]
            i += 1

        # If no station is reachable and we haven't reached the destination, it's impossible to proceed
        if last_reachable_station is None:
            return -1, []

        # Refuel at the furthest reachable station
        stops += 1
        stop_list.append(last_reachable_station)
        current_pos = last_reachable_station

    return stops, stop_list

F = 25
d = 6
stations = [4, 7, 11, 13, 18, 20, 23]
min_stops, stop_stations = min_refuel_stops(F, d, stations)
print("Minimum stops needed:", min_stops)
print("Stop at stations:", stop_stations)
