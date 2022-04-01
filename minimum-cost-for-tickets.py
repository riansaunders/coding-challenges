def mini(days, costs):

    def f(day):
        # If you're at the end there's nowhere to go, you already paid for this day.
        if day == len(days):
            return 0 
        minimum = float('inf')
        day_progression = [1,7, 30]
        for i, cost in enumerate(costs):
            j = day
            # Go right into the array until I see a day that's bigger than the duration of my ticket + my current day.
            # For example I am on day 1, duration 7 which means the day in the array must be at least 8.
            while j < len(days) and days[j] < days[day] + day_progression[i]:
                j += 1 
            # The stack will pass up the cost.
            minimum = min(minimum, cost+ f(j))
        return minimum 
    return f(0)

print(mini([1,4,6,7,8,20], [2,7,15]))
