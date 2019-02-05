import os
import csv

# Path to CSV
csv_path = os.path.join("..","Resources","budget_data.csv")

# Create lists
months=[]
profits=[]

# Open CSV
with open(csv_path, newline="", encoding = "utf-8") as csvfile:
    budget = csv.reader(csvfile, delimiter=",")

    # Skip Headers
    csv_header = next(budget)

    for i in budget:
        # Collect months in list
        months.append(i[0])

        # Collect profits in list
        profits.append(int(i[1]))

    # Set Total Values
    total_months = len(months)

    total_ammount = sum(profits)

    # Find Average
    average_change = total_ammount / len(profits)

    # Find Greatist Increase ammount and date
    greatist_ammount = max(profits)
    max_index = profits.index(greatist_ammount)
    increase_date = months[max_index]

    # Find Greatist Decrease ammount and date
    lowest_ammount = min(profits)
    min_index = profits.index(lowest_ammount)
    decrease_date = months[min_index]

    # Print values
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_ammount}")
    print(f"Average Change: ${average_change}")
    print(f"Greatist Increase in Profits: {increase_date} (${greatist_ammount})")
    print(f"Greatist Decrease in Profits: {decrease_date} (${lowest_ammount})")

    # Export text file
    output_path = os.path.join("..", "PyBank", "BudgetResults.txt")

    text_file = open(output_path, "w")

    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total_ammount}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatist Increase in Profits: {increase_date} (${greatist_ammount})\n")
    text_file.write(f"Greatist Decrease in Profits: {decrease_date} (${lowest_ammount})")

    text_file.close()





