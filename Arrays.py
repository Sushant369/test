ExpensePerMonth= [2200,2350,2600,2130,2190]
month=["Jan","Feb","Mar","Apr","May"]


"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""
print("1. In Feb, how many dollars you spent extra compare to January?")
print(ExpensePerMonth[1]-ExpensePerMonth[0])


totalexpen=0
for i in range(3):
    totalexpen +=ExpensePerMonth[i]
print("2. Find out your total expense in first quarter (first three months) of the year.")
print("Total expense in first quarter",totalexpen)

print("3. Find out if you spent exactly 2000 dollars in any month")
for i in range(len(ExpensePerMonth)):
    if ExpensePerMonth[i]==2000:
        print(month[i])
    else:
        print("We didn't spend exact 2000 dollars in any month")


