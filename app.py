# Importing tools
import pandas as pd
import plotly.express as px
import streamlit as st

# Config webpage.
## https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Dashboard: Customer Segmentation', page_icon=':bar_chart:', layout='wide')


# Function to load dataframe.
def get_data_from_excel():
    df = pd.read_excel(io='./Data/DataFrame_Customers_with_Cluster.xlsx',
                  engine='openpyxl', sheet_name='Data',
                  skiprows=3, usecols='B:R', nrows=1000)
    return df

# Call the function
df = get_data_from_excel()
print(df)



# Sidebar section.
## Filter for Cluster.
st.sidebar.header('Please filter here:')
cluster = st.sidebar.multiselect('Select the Cluster:',
                                 options=df['Cluster'].unique(),
                                 default=df['Cluster'].unique())

## Filter for Education.
education1 = st.sidebar.multiselect('Select Education Level:',
                                 options=df['Education'].unique(),
                                 default=df['Education'].unique())

## Filter for Income.
income_data = df['Income'].tolist()
income = st.sidebar.slider(label='Select the Income ($K):', min_value=min(income_data),
                           max_value=max(income_data), value=(min(income_data), max(income_data)))

## Filter for Debt.
debt_data = df['Debt'].tolist()
debt = st.sidebar.slider(label='Select the Debt:', min_value=min(debt_data),
                        max_value=max(debt_data), value=(min(debt_data),max(debt_data)))

## Filter for DebtIncomeRatio.
debtratio_data = df['DebtIncomeRatio'].tolist()
debtratio = st.sidebar.slider(label='Select the Debt Income Ratio:', min_value=min(debtratio_data),
                        max_value=max(debtratio_data), value=(min(debtratio_data),max(debtratio_data)))

## Filter for Age.
age_data = df['Age'].tolist()
age = st.sidebar.slider(label='Select the Age:', min_value=min(age_data),
                        max_value=max(age_data), value=(min(age_data),max(age_data)))

## Filter for Education.
edu_data = df['Education'].tolist()
education = st.sidebar.slider(label='Select the Education Level:', min_value=min(edu_data),
                        max_value=max(edu_data), value=(min(edu_data),max(edu_data)))

# To make the filters interact with the table (data).
df_filtered = df.query('Cluster == @cluster and Education == @education1 and Age == @age')

#print(df.query("'Cluster' == @cluster and 'Education' == @education1 and 'Income' == @income"))
#print(df.query("Cluster == @cluster and Education == @education1")# and `Income` == @income"))
#print(df.query("`Courses Fee` >= 23000 and `Courses Fee` <= 24000"))

# & Income == @income & Debt == @debt & DebtIncomeRatio == @debtratio & Age == @age & Education == @education')

st.dataframe(df_filtered)
















