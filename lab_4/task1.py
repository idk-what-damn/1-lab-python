import numpy as np

expenses = np.array([120, 130, 110, 100, 90, 80, 85, 95, 105, 115, 125, 135])

winter = expenses[[11, 0, 1]]
summer = expenses[[5, 6, 7]]

print("Зимние расходы:", winter.sum())
print("Летние расходы:", summer.sum())

if winter.sum() > summer.sum():
    print("Зимой тратится больше.")
else:
    print("Летом тратится больше.")

max_expense = expenses.max()
max_months = np.where(expenses == max_expense)[0] + 1
print("Месяцы с наибольшими расходами:", max_months)
