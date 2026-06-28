from database import view_trips


def total_trips():
    trips = view_trips()
    return len(trips)


def total_revenue():
    trips = view_trips()

    revenue = 0

    for trip in trips:
        revenue += trip[7]

    return revenue


def total_fuel_cost():
    trips = view_trips()

    fuel = 0

    for trip in trips:
        fuel += trip[8]

    return fuel


def total_profit():
    return total_revenue() - total_fuel_cost()

def highest_fare():

    trips = view_trips()

    if not trips:
        return 0

    highest = trips[0][7]

    for trip in trips:
        if trip[7] > highest:
            highest = trip[7]

    return highest

def average_fare():

    trips = view_trips()

    if not trips:
        return 0

    return total_revenue() / len(trips)

def most_popular_route():

    trips = view_trips()

    if not trips:
        return "No trips"

    routes = {}

    for trip in trips:

        route = f"{trip[3]} → {trip[4]}"

        if route in routes:
            routes[route] += 1
        else:
            routes[route] = 1

    return max(routes, key=routes.get)
