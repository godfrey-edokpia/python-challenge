import csv
total_months = 0
month = []
mylist_total = []
total_amount = 0
average = []
avr = 0,0
total = 0,0
print('Financial Analysis')
print('-----------------------')
with open("budget_data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimeter =',')
    csv_header = next(csvfile)
    for row in reader:
        #new_month = row[0]
        month.append(row[0])
        #To get the total for row 1
        mylist_total.append(int(row[1]))
    for row in range(1, len(mylist_total)):
        average.append(int(mylist_total[row] - int(mylist_total[row - 1])))
    # find the total month
    print("Total Month : ", len(month))
    for i in mylist_total:
        total_amount += 1
    print("total $:", total_amount)
    averagerevenue = sum(average) / len(average)    
    print('Average_Change: ', averagerevenue)
    # Max Revenue
    max_revenue = max(average)
    print('Greatest Increase in Profit: ',(month [average.index(max(average))]), (max_revenue))
 
    # MainRevenue
    print('Greatest decrease in Profit: ',(month [average.index(min(average))]), (min_revenue))
       # Average.append(int(row[1]))
       # print (i)
       
       # total_amount += x

