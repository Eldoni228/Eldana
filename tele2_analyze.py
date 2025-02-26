import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    'Age': np.random.randint(20, 60, 100),
    'Salary': np.random.randint(40000, 150000, 100),
    'Experience': np.random.randint(1, 40, 100),
    'Department': np.random.choice(['IT', 'HR', 'Sales', 'Marketing', 'Support'], 100),
    'Region': np.random.choice(['Almaty', 'Astana', 'Shymkent', 'Karaganda'], 100)
})

print(df.head())
print(df.describe())
print(df.info())

plt.figure(figsize=(10, 5))
sns.histplot(df['Salary'], bins=20, kde=True)
plt.title('Salary Distribution in Tele2')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

df_encoded = df.copy()
df_encoded['Department'] = df_encoded['Department'].astype('category').cat.codes
df_encoded['Region'] = df_encoded['Region'].astype('category').cat.codes

correlation_matrix = df_encoded.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Tele2 Employees')
plt.show()

avg_salary_by_department = df.groupby('Department')['Salary'].mean()
print(avg_salary_by_department)

plt.figure(figsize=(8, 4))
avg_salary_by_department.plot(kind='bar', color=['blue', 'green', 'red', 'orange', 'purple'])
plt.title('Average Salary by Department in Tele2')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.show()

avg_salary_by_region = df.groupby('Region')['Salary'].mean()
print(avg_salary_by_region)

plt.figure(figsize=(8, 4))
avg_salary_by_region.plot(kind='bar', color=['cyan', 'magenta', 'yellow', 'black'])
plt.title('Average Salary by Region in Tele2')
plt.xlabel('Region')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.show()
