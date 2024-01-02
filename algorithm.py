def calculate_affected_population(total_population, initial_spread_rate, elapsed_time, upgrade_point):
    # Assuming initial_spread_rate is the initial rate before reduction
    # Define the time after which the rate will decrease (in minutes)
    time_to_reduce_rate = 10  # Adjust this time as needed (e.g., 10 minutes)

    # Define the reduction amount
    reduction_amount = 0.1  # Adjust this reduction amount as needed

    # If the elapsed time exceeds the time_to_reduce_rate, reduce the spread rate
    if elapsed_time >= time_to_reduce_rate:
        # Calculate how many times the reduction has occurred
        reduction_times = elapsed_time // time_to_reduce_rate

        # Calculate the updated spread rate after reductions
        updated_spread_rate = initial_spread_rate - (reduction_times * reduction_amount)

        # Use the updated spread rate for calculation
        affected_population = total_population * updated_spread_rate * elapsed_time
    else:
        # Use the initial spread rate before reduction for calculation
        affected_population = total_population * initial_spread_rate * elapsed_time

    # Calculate the proportion of affected population
    proportion_affected = affected_population / total_population

    # Check if the proportion satisfies the condition for earning upgrade points
    if proportion_affected >= 0.1:  # Example: 1/10 of the total population
        upgrade_point += 1  # Increase upgrade points by 1

    return affected_population, upgrade_point


