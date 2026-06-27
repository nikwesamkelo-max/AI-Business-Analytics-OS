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
