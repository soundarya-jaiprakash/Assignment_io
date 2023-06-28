global a
a = [0, 0, 0]

def maxProfit(n):
    unit_time = [4, 5, 10]
    
    if n < 4:
        return 0
    else:
        profit = [0, (n - 4) * 1000, 0]
    
    if n >= 5:
        if n >= 10:
            profit[2] = (n - 10) * 3000
        else:
            profit[2] = 0

        profit[1] = max((n - 5) * 1500, profit[2])
    
    a[profit.index(max(profit))] += 1
    return profit[profit.index(max(profit))] + maxProfit(n - unit_time[profit.index(max(profit))])

if __name__ == '__main__':
    print("Earnings: $", maxProfit(int(input("Time unit: "))))
    print(f"Solution: T: {a[1]} P: {a[0]} C: {a[2]}")
