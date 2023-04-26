
#Author: Laszlo Koosz

#Import pandas
import pandas as pd

# Create a DataFrame with balance.txt
df = pd.read_csv("balance.txt", sep=" ")

#Compare the average income based on ethnicity.

#select each ethnicity
african_americans = df[df["Ethnicity"] == "African American"]
caucasians = df[df["Ethnicity"] == "Caucasian"]
asians = df[df["Ethnicity"] == "Asian"]

#calculate average income for each ethnicity
average_income_aa = african_americans["Income"].mean()
average_income_caucasian = caucasians["Income"].mean()
average_income_asian = asians["Income"].mean()

#store the average income in a new data frame
average_incomes = pd.DataFrame({
    "African American": average_income_aa,
    "Caucasian": average_income_caucasian,
    "Asian": average_income_asian
}.items())

#print each ethnicity in descending order based on average income
print(average_incomes.sort_values([1], ascending=False))

# On average, do married or single people have a higher balance?
# Answer: On average, single people have a higher balance

# Program to calculate:
# select singles and marrieds
singles = df[df["Married"] == "No"]
marrieds = df[df["Married"] == "Yes"]

#calculate average balance of singles and marrieds
average_balance_singles = singles["Balance"].mean()
average_balance_marrieds = marrieds["Balance"].mean()

#compare balance
print(f"Average balance for marrieds: {average_balance_marrieds}")
print(f"Average balance for singles: {average_balance_singles}")
if average_balance_marrieds > average_balance_singles:
    print("On average, married people have a higher balance")
else:
    print("On average, single people have a higher balance")


# What is the highest income in our dataset?
# Answer: 186.634

# Program to calculate:
# pick highest income from dataframe
highest_income = df["Income"].nlargest(1)

#print income value
print(highest_income)

# What is the lowest income in our dataset?
# Answer: 10.354

# Program to calculate:
# pick lowest income from dataframe
lowest_income = df["Income"].nsmallest(1)

#print income value
print(lowest_income)

# How many cards do we have recorded in our dataset?
# Answer: 1183

#Program to calculate:
#caclulate sum of cards in dataset
cards = df["Cards"].sum()
print(cards)

# How many females do we have information for vs how many males?
# Answer: Females: 207, Males: 193 

#Program to calculate:
#select females and males
females = df[df["Gender"] == "Female"]
males = df[df["Gender"] == "Male"]

#print the number of males and females
print(f"Females: {len(females.count(axis='columns'))} Males: {len(males.count(axis='columns'))}")