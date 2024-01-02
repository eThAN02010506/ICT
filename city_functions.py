from city_data import city_population, city_spread_rates
from algorithm import calculate_affected_population

def calculate_city_affected_population(elapsed_time, upgrade_point):
    simulation_time = elapsed_time  # 模拟的时间（分钟）
    total_population = sum(city_population.values())  # 计算所有城市人口的总和

    for city in city_population:
        spread_rate = city_spread_rates[city]
        affected_population, upgrade_point = calculate_affected_population(city_population[city], spread_rate, simulation_time, upgrade_point)
        # Print or use affected_population for each city
        print(f"In {city}, the estimated affected population in {simulation_time} minutes is: {affected_population:.0f} people")

    return upgrade_point, total_population  # 返回升级点数和总人口数
