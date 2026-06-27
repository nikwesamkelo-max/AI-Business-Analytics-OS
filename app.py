from database import create_tables, add_trip, view_trips


def main():

    create_tables()

    add_trip(
        customer_name="John",
        phone="0812345678",
        pickup="Pinetown",
        destination="King Shaka Airport",
        vehicle="7 Seater",
        driver="Ngwane",
        fare=550,
        fuel_cost=120,
        payment_method="Cash",
        trip_date="2026-06-27"
    )

    print("\n------ ALL TRIPS ------")

    trips = view_trips()

    for trip in trips:
        print(trip)


if __name__ == "__main__":
    main()
