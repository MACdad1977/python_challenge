import os
import csv

# set path
budget_data = os.path.join("Resources", "budget_data.csv")

# Create lists to store data
profit = []
monthly_changes = []
date = []

# create variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#loop through columns
for files in budget_data:
    budget_dataCSV = os.path.join("Resources", bud)