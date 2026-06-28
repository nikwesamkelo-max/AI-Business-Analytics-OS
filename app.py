from analytics import (
    total_trips,
    total_revenue,
    total_fuel_cost,
    total_profit,
    highest_fare,
    average_fare,
    most_popular_route
)

print("\n========== AI BUSINESS DASHBOARD ==========")
print(f"🚖 Total Trips      : {total_trips()}")
print(f"💰 Revenue          : R{total_revenue():.2f}")
print(f"⛽ Fuel Cost        : R{total_fuel_cost():.2f}")
print(f"📈 Profit           : R{total_profit():.2f}")
print(f"🏆 Highest Fare     : R{highest_fare():.2f}")
print(f"💵 Average Fare     : R{average_fare():.2f}")
print(f"🛣️ Popular Route    : {most_popular_route()}")
print("===========================================")
