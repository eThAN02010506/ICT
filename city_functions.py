# city_functions.py

from algorithm import calculate_affected_population
from city_data import city_population, city_spread_rates

def calculate_city_affected_population():
    simulation_time = 10  # 模拟时间（分钟）

    for city in city_population:
        total_population = city_population[city]
        spread_rate = city_spread_rates[city]
        affected_population = calculate_affected_population(total_population, spread_rate, simulation_time)
        print(f"在 {city} 中，预计在 {simulation_time} 分钟内影响人数为：{affected_population:.0f} 人")
