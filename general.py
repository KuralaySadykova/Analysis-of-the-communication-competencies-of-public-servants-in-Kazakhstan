import pandas as pd
import matplotlib.pyplot as plt

# Read data from the first Excel file
df1 = pd.read_excel('C:/Users/User/Desktop/Final/ЦГО рус.xlsx')

# Read data from the second Excel file
df2 = pd.read_excel('C:/Users/User/Desktop/Final/МИО рус.xlsx')

# Merge data across columns with the same names
merged_df = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)

# Saving merged data to a new Excel file
merged_df.to_excel('merged_file.xlsx', index=False)

# Read data from merged Excel file
df = pd.read_excel('merged_file.xlsx')

# Counting the number of respondents
respondent_count = df.shape[0]
print("Number of respondents:", respondent_count)

#%% General Demographics

# Gender
gender = merged_df['Gender']
print(gender.value_counts())

# Age
age = merged_df['Age']
print(age.value_counts())

#%% How much time do government employees spend on communications?

# Loading the data from an Excel file
time = merged_df['11. What percentage of your working time do you spend on communications?']

# Exploring the data 
print(time.value_counts())

# Data to plot the chart
labels = ['0.5', '0.8', '0.7', '1', '0.3', '0.4', '0.9', '0.6', '0.2', '0.1', 'Less than 10%']
values = [376, 260, 232, 187, 179, 136, 134, 131, 78, 36, 27]

# Calculate the total number of responses
total_responses = sum(values)

# Convert values to percentages
percentages = [(value / total_responses) * 100 for value in values]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, percentages, color='skyblue')

# Customize axis title and labels
plt.title('Percentage of Working Time Spent on Communications')
plt.xlabel('Percentage of Time')
plt.ylabel('Percentage of Responses')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adding percentage values above columns
for i, percentage in enumerate(percentages):
    plt.text(i, percentage + 0.5, f'{percentage:.1f}%', ha='center')

# Display chart
plt.tight_layout()
# Saving the chart
plt.savefig('time_to_communication.png')
plt.show()


#%% Feedback check

# Loading the data from an Excel file
feedback = merged_df['22. After transmitting a response to an appeal, request, information to the addressee, do you check how much the addressee understood and whether he interpreted your answer correctly?']

# Exploring the data 
print(feedback.value_counts())

# Data for charting
labels = ['Yes, I always check', 'Sometimes when I have time', 'I never check, I have no time']
sizes = [1212, 471, 95]
colors = ['blue', 'red', 'khaki']

# Create a Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title customization
plt.title('Feedback check')

# Chart display
plt.axis('equal')  # чтобы диаграмма была кругом
# Saving the chart
plt.savefig('feedback.png')
plt.show()






