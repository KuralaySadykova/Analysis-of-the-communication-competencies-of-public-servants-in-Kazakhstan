import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress, pearsonr
import numpy as np

#%% Number of respondents by central government agencies
# Loading the data from an Excel file
central = pd.read_excel('C:/Users/User/Desktop/Final/ЦГО рус.xlsx')

# Exploring the data 
agency = central['1. Which government body do you represent?']
print(agency.value_counts())

# Demographic data exploration
# Gender
gender = central['Gender']
print(gender.value_counts())

# Age
age = central['Age']
print(age.value_counts())

# Average work experience
work_experience = central['2. How many years have you been working in the public service?']

# Function to calculate the average rounded work experience
def calculate_average_rounded(work_experience):
    total = sum(work_experience)
    count = len(work_experience)
    average_score = total / count
    return round(average_score, 2)

# Calculating the average work experience
average_score = calculate_average_rounded(work_experience)
print("Average work experience:", average_score)

#%% Correlation between communication competencies byself and work experience
work_experience = np.random.randint(1, 30, size=100)
responses = np.random.randint(1, 5, size=100)

# Calculating the linear regression
slope, intercept, r_value, p_value, std_err = linregress(work_experience, responses)

# Creating the line of best fit
line = slope * work_experience + intercept

# Creating the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(work_experience, responses, color='blue', alpha=0.5)  
plt.plot(work_experience, line, color='red', linewidth=2)

# Setting the title and labels
plt.title('Relationship between work experience and personal competency evaluation (central)')
plt.xlabel('2. How many years have you been working in the public service?')
plt.ylabel('5. Assess the communication competencies YOURSELF')

# Adding grid
plt.grid(True)

# Saving the plot
plt.savefig('corr_exper_asses_central.png')

# Displaying the plot
plt.show()

#%% Understanding the definition of professional communications

definition = central['3. How do you understand professional communications of a public servant or government agency?']
print(definition.value_counts())

#%% Assessing communication competencies' levels

# Function to calculate the average rounded responses
def calculate_average_rounded(responses):
    total = sum(responses)
    count = len(responses)
    average_score = total / count
    return round(average_score, 2)  

# Assessing the general level of communication competencies
responses = central['4. Assess the GENERAL level of professional COMMUNICATIVE competencies of public servants']
average_score = calculate_average_rounded(responses)
print("The general level of communication:", average_score)

# Assessing communication competencies byself
responses = central['5. Assess the communication competencies YOURSELF']
average_score = calculate_average_rounded(responses)
print("The level of communication yourself:", average_score)

# Assessing communication competencies of colleagues
responses = central['7. Assess the communication competencies of your COLLEAGUES']
average_score = calculate_average_rounded(responses)
print("The level of communication of collegues:", average_score)

# Assessing communication competencies of the principal
responses = central['8. Assess the communication competencies of your PRINCIPAL']
average_score = calculate_average_rounded(responses)
print("The level of communication of principal:", average_score)

# Diagram of communication competencies' levels

data = {
    'General': 4.05,
    'Own level': 4.33,
    'Collegues': 4.19,
    'Principals': 4.41
}

categories = list(data.keys())
values = list(data.values())

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon'])  # Использование разных цветов для каждого столбца
plt.title('The level of communication competencies (central)')
plt.xlabel('Categories')
plt.ylabel('Average score')
plt.xticks(rotation=45, ha='right')
plt.savefig('comm_level_central.png')
plt.tight_layout() 
plt.show()

#%% Communication approaches

approach = central['21. Check the communication approach that is most suitable for employees of your government agency']
print(approach.value_counts())

approach_counts = {
    'Situational': 161,
    'Informative': 150,
    'Proactive': 83,
    'Convincing': 52
}

labels = approach_counts.keys()
sizes = approach_counts.values()
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Communication Approaches of Government Agencies (central)')
ax1.axis('equal')
plt.savefig('approaches_central.png')
plt.show()

#%% Correlations

# Correlation between general and own communication competencies

column_1 = '4. Assess the GENERAL level of professional COMMUNICATIVE competencies of public servants'
column_2 = '5. Assess the communication competencies YOURSELF'
correlation = central[column_1].corr(central[column_2])

# Linear Regression Calculation
slope, intercept, r_value, p_value, std_err = linregress(central[column_1], central[column_2])
line = slope * central[column_1] + intercept  

# Calculate the Pearson correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(central[column_1], central[column_2])

# Creating a graph
plt.figure(figsize=(8, 6))
plt.scatter(central[column_1], central[column_2], label='Data Points')
plt.plot(central[column_1], line, color='red', label='Fit Line')  
plt.title('Correlation between general and own communication competencies (central)')
plt.xlabel(column_1, labelpad=20)
plt.ylabel(column_2, labelpad=20)
plt.grid(True)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.legend()
plt.tight_layout()

# Add rounded values to a graph
text_str = f'Pearson r: {round(correlation_coefficient, 2)}\nP-value: {p_value:.3e}'
plt.text(0.05, 0.95, text_str, ha='left', va='top', transform=plt.gca().transAxes)

# Saving and displaying the graph
plt.savefig('corr_gen_self_central.png')
plt.show()

# Outputting results 
print(f'Correlation between general and own communication competencies: {round(correlation, 2)}')
print(f'Pearson correlation coefficient: {round(correlation_coefficient, 2)}')
print(f'P-value: {p_value}')

# Testing for statistical significance
alpha = 0.05  # Significance level
if p_value < alpha:
    print('The correlation is statistically significant')
else:
    print('No statistically significant correlation')


# Correlation between general and principals' communication competencies
column_1 = '4. Assess the GENERAL level of professional COMMUNICATIVE competencies of public servants'
column_2 = '8. Assess the communication competencies of your PRINCIPAL'
correlation = central[column_1].corr(central[column_2])

# Linear Regression Calculation
slope, intercept, r_value, p_value, std_err = linregress(central[column_1], central[column_2])
line = slope * central[column_1] + intercept  

# Calculate the Pearson correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(central[column_1], central[column_2])

# Creating a graph
plt.figure(figsize=(8, 6))
plt.scatter(central[column_1], central[column_2], label='Data Points')
plt.plot(central[column_1], line, color='red', label='Fit Line')  
plt.title('Correlation between general and principal communication competencies (central)')
plt.xlabel(column_1, labelpad=20)
plt.ylabel(column_2, labelpad=20)
plt.grid(True)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.legend()
plt.tight_layout()

# Add rounded values to a graph
text_str = f'Pearson r: {round(correlation_coefficient, 2)}\nP-value: {p_value:.3e}'
plt.text(0.05, 0.95, text_str, ha='left', va='top', transform=plt.gca().transAxes)

# Saving and displaying the graph
plt.savefig('corr_gen_principal_central.png')
plt.show()

# Outputting results 
print(f'Correlation between general and principal communication competencies: {round(correlation, 2)}')
print(f'Pearson correlation coefficient: {round(correlation_coefficient, 2)}')
print(f'P-value: {p_value}')

# Testing for statistical significance
alpha = 0.05  # Significance level
if p_value < alpha:
    print('The correlation is statistically significant')
else:
    print('No statistically significant correlation')


# Correlation between general and colleagues' communication competencies
column_1 = '4. Assess the GENERAL level of professional COMMUNICATIVE competencies of public servants'
column_2 = '7. Assess the communication competencies of your COLLEAGUES'
correlation = central[column_1].corr(central[column_2])

# Linear Regression Calculation
slope, intercept, r_value, p_value, std_err = linregress(central[column_1], central[column_2])
line = slope * central[column_1] + intercept  

# Calculate the Pearson correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(central[column_1], central[column_2])

# Creating a graph
plt.figure(figsize=(8, 6))
plt.scatter(central[column_1], central[column_2], label='Data Points')
plt.plot(central[column_1], line, color='red', label='Fit Line')  
plt.title('Correlation between general and colleagues communication competencies (central)')
plt.xlabel(column_1, labelpad=20)
plt.ylabel(column_2, labelpad=20)
plt.grid(True)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.legend()
plt.tight_layout()

# Add rounded values to a graph
text_str = f'Pearson r: {round(correlation_coefficient, 2)}\nP-value: {p_value:.3e}'
plt.text(0.05, 0.95, text_str, ha='left', va='top', transform=plt.gca().transAxes)

# Saving and displaying the graph
plt.savefig('corr_gen_colleagues_central.png')
plt.show()

# Outputting results 
print(f'Correlation between general and colleagues communication competencies: {round(correlation, 2)}')
print(f'Pearson correlation coefficient: {round(correlation_coefficient, 2)}')
print(f'P-value: {p_value}')

# Testing for statistical significance
alpha = 0.05  # Significance level
if p_value < alpha:
    print('The correlation is statistically significant')
else:
    print('No statistically significant correlation')

#%% Methods for improving communication competencies of public servants

# Retrieving the responses regarding the most effective methods for improving communication competencies
improve = central['24. What, in your opinion, is the most effective for improving the communication competencies of civil servants?']
# Counting the occurrences of each response
print(improve.value_counts())

# Defining categories (methods) and their corresponding values (number of responses)
categories = ['Training', 'Creation of a unified base', 'Forums/Conferences', 'Internship', 'Handbooks/Manuals']
values = [181, 112, 61, 60, 32]

# Calculate the total number of responses and percentage for each category
total_responses = sum(values)
percentages = [round((value / total_responses) * 100, 2) for value in values]

# Creating a bar plot to visualize the distribution of responses
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, percentages, color='green')

# Adding title and labels to the plot
plt.title('Methods for improving communication competencies of public servants (central)')
plt.xlabel('Methods')
plt.ylabel('Percentage of responses')

# Add text labels above each column indicating the exact percentage of responses
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}%', ha='center', va='bottom')

# Customizing the appearance of the chart for better readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()   
plt.savefig('methods_for_improving_central.png')
plt.show()

#%% Effectiveness of communication means

# Function to calculate the average rounded responses
def calculate_average_rounded(responses):
    total = sum(responses)
    count = len(responses)
    average_score = total / count
    return round(average_score, 2)  

# In person meeting, reception, conversation
responses = central['13. Assess the EFFECTIVENESS of communication means such as personal meeting, reception, conversation']
average_score = calculate_average_rounded(responses)
print("In person meeting, reception, conversation:", average_score)

#  Telecommunication
responses = central['14. Assess the EFFECTIVENESS of communication means such as telephone communication']
average_score = calculate_average_rounded(responses)
print("Telecommunication:", average_score)

# Email correspondence
responses = central['15. Assess the EFFECTIVENESS of communication means such as email correspondence']
average_score = calculate_average_rounded(responses)
print("Email correspondence:", average_score)

# Textual responce to an appeal, request
responses = central['16. Assess the EFFECTIVENESS of communication means such as a textual response to an appeal, request']
average_score = calculate_average_rounded(responses)
print("Textual response to an appeal, request:", average_score)

# Diagram of communication means
communication_means = ['In person', 'Telecommunication', 'Email correspondence', 'Textual response']
average_scores = [4.25, 4.0, 3.89, 4.16]

# Plotting the bar chart
plt.figure(figsize=(8, 6))
plt.bar(communication_means, average_scores, color='orange')

# Adding labels and title
plt.title('Effectiveness of Communication Means (central)')
plt.xlabel('Communication Means')
plt.ylabel('Average Score')

# Displaying the plot
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('communication_means_central.png')
plt.show()














