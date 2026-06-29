from database import (
    create_tables,
    add_trip,
    view_trips,
    search_customer
)

from analytics import (
    total_trips,
    total_revenue,
    total_fuel_cost,
    total_profit,
    highest_fare,
    average_fare,
    most_popular_route
)


def show_dashboard():

    print("\n========== AI BUSINESS DASHBOARD ==========")
    print(f"🚖 Total Trips      : {total_trips()}")
    print(f"💰 Revenue          : R{total_revenue():.2f}")
    print(f"⛽ Fuel Cost        : R{total_fuel_cost():.2f}")
    print(f"📈 Profit           : R{total_profit():.2f}")
    print(f"🏆 Highest Fare     : R{highest_fare():.2f}")
    print(f"💵 Average Fare     : R{average_fare():.2f}")
    print(f"🛣️ Popular Route    : {most_popular_route()}")
    print("===========================================")


def add_new_trip():

    print("\n----- Add New Trip -----")

    customer = input("Customer Name: ")
    phone = input("Phone Number: ")
    pickup = input("Pickup: ")
    destination = input("Destination: ")
    vehicle = input("Vehicle: ")
    driver = input("Driver: ")

    fare = float(input("Fare: R"))
    fuel = float(input("Fuel Cost: R"))

    payment = input("Payment Method: ")
    date = input("Trip Date (YYYY-MM-DD): ")

    add_trip(
        customer,
        phone,
        pickup,
        destination,
        vehicle,
        driver,
        fare,
        fuel,
        payment,
        date
    )


def show_all_trips():

    trips = view_trips()

    if not trips:
        print("\nNo trips found.")
        return

    print("\n========== ALL TRIPS ==========\n")

    for trip in trips:

        print("=" * 40)
        print(f"Trip ID      : {trip[0]}")
        print(f"Customer     : {trip[1]}")
        print(f"Phone        : {trip[2]}")
        print(f"Pickup       : {trip[3]}")
        print(f"Destination  : {trip[4]}")
        print(f"Vehicle      : {trip[5]}")
        print(f"Driver       : {trip[6]}")
        print(f"Fare         : R{trip[7]:.2f}")
        print(f"Fuel Cost    : R{trip[8]:.2f}")
        print(f"Payment      : {trip[9]}")
        print(f"Status       : {trip[10]}")
        print(f"Trip Date    : {trip[11]}")
        print("=" * 40)


def find_customer():

    name = input("\nEnter customer name: ")

    results = search_customer(name)

    if not results:
        print("\nCustomer not found.")
        return

    print("\n========== SEARCH RESULTS ==========\n")

    for trip in results:

        print("=" * 40)
        print(f"Trip ID      : {trip[0]}")
        print(f"Customer     : {trip[1]}")
        print(f"Phone        : {trip[2]}")
        print(f"Pickup       : {trip[3]}")
        print(f"Destination  : {trip[4]}")
        print(f"Vehicle      : {trip[5]}")
        print(f"Driver       : {trip[6]}")
        print(f"Fare         : R{trip[7]:.2f}")
        print(f"Fuel Cost    : R{trip[8]:.2f}")
        print(f"Payment      : {trip[9]}")
        print(f"Status       : {trip[10]}")
        print(f"Trip Date    : {trip[11]}")
        print("=" * 40)


def main():

    create_tables()

    while True:

        print("\n========== AI BUSINESS OS ==========")
        print("1. Add Trip")
        print("2. Business Dashboard")
        print("3. View All Trips")
        print("4. Search Customer")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_new_trip()

        elif choice == "2":
            show_dashboard()

        elif choice == "3":
            show_all_trips()

        elif choice == "4":
            find_customer()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
