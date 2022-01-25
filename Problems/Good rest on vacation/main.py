days = int(input())
food_cost_per_day = int(input())
flight_cost_one_way = int(input())
hotel_cost_one_night = int(input())

cost = food_cost_per_day * days
cost += flight_cost_one_way * 2
cost += hotel_cost_one_night * (days - 1)

print(cost)
