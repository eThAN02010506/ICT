import math

def exponential_spread_rate(elapsed_time, total_population):
    base_population = 10000  # 在30分钟内受影响的基础人口数
    growth_rate = math.log(total_population / base_population) / 30  # 计算增长率

    # 使用对数函数来控制增长速率
    spread_rate = base_population * math.exp(growth_rate * elapsed_time)
    return min(spread_rate, total_population)  # 确保受影响人口不超过总人口

def calculate_affected_population(total_population, elapsed_time):
    spread_rate = exponential_spread_rate(elapsed_time, total_population)
    affected_population = spread_rate
    return affected_population

# 假设City3的人口为15000，计算30分钟内受影响的人口数量
city3_population = 15000
for time in range(31):
    affected = calculate_affected_population(city3_population, time)
    print(f"At {time} minutes, affected population in City3: {affected}")
