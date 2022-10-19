# Importing tools
import streamlit as st
import pandas as pd
import plotly.express as px


# Config webpage.
## https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Dashboard: Project 4', page_icon=':leaves:', layout='wide')


# Function to load dataframe.
@st.cache
def get_data_from_excel():
    df = pd.read_excel(io='./Data/DataFrame_Customers_with_Cluster.xlsx',
                  engine='openpyxl', sheet_name='Data',
                  skiprows=3, usecols='B:R', nrows=1000)
    return df

# Call the function
df = get_data_from_excel()
print(df)

#st.dataframe(df)

# SIDEBAR SECTION.

# Filter for Cluster.
st.sidebar.header('Filter options:')
cluster = st.sidebar.multiselect('By Cluster:',
                                 options=df['Cluster'].unique(),
                                 default=df['Cluster'].unique())


# Filter for Income.
income_data = df['Income'].tolist()
income = st.sidebar.slider(label='By Income (US $K):', min_value=min(income_data),
                           max_value=max(income_data), value=(min(income_data), max(income_data)))

# Filter for Debt.
debt_data = df['Debt'].tolist()
debt = st.sidebar.slider(label='By Debt:', min_value=min(debt_data),
                        max_value=max(debt_data), value=(min(debt_data),max(debt_data)))

# Filter for DebtIncomeRatio.
debtratio_data = df['DebtIncomeRatio'].tolist()
debtratio = st.sidebar.slider(label='By Debt Income Ratio:', min_value=min(debtratio_data),
                        max_value=max(debtratio_data), value=(min(debtratio_data),max(debtratio_data)))

# Filter for Age.
age_data = df['Age'].tolist()
age = st.sidebar.slider(label='By Age:', min_value=min(age_data),
                        max_value=max(age_data), value=(min(age_data),max(age_data)))

# Filter for Education.
edu_data = df['Education'].tolist()
education = st.sidebar.slider(label='By Education Level:', min_value=min(edu_data),
                        max_value=max(edu_data), value=(min(edu_data),max(edu_data)))


# To make the filters interact with the table (data).
df_filtered = df.query('Cluster == @cluster \
                        and Education >= @education[0] and Education <= @education[-1] \
                        and Income >= @income[0] and Income <= @income[-1]\
                        and Debt >= @debt[0] and Debt <= @debt[-1]\
                        and DebtIncomeRatio >= @debtratio[0] and DebtIncomeRatio <= @debtratio[-1]\
                        and Age >= @age[0] and Age <= @age[-1]')


# MAINPAGE

st.title(':bar_chart: Customer Segmentation Dashboard')
st.markdown('##')

## TOP KPIs
avg_income = df_filtered['Income'].mean()
avg_debt = df_filtered['Debt'].mean()
avg_debt_income_ratio = df_filtered['DebtIncomeRatio'].mean()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Average Income')
    st.subheader(f'US $ {avg_income*1000:,.2f}')
with middle_column:
    st.subheader('Average Debt')
    st.subheader(round(avg_debt, 2))
with right_column:
    st.subheader('Average Debt Income Ratio')
    st.subheader(round(avg_debt_income_ratio, 2))

st.markdown('---')

## BAR PLOTS
### For Age
avg_age_per_cluster = df_filtered.groupby('Cluster')['Age'].mean()
fig_age_per_cluster = px.bar(avg_age_per_cluster, x='Age', y=avg_age_per_cluster.index, width=500, height=400,
                             orientation='h', title='<b> Avg. Age per Cluster</b>', color=avg_age_per_cluster.index,
                             color_discrete_sequence=['#0083B8', '#68b800', '#b80062'], template='plotly_white')
fig_age_per_cluster.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis=(dict(showgrid=False)))


### For Income
avg_income_per_cluster = df_filtered.groupby('Cluster')['Income'].mean()
fig_income_per_cluster = px.bar(avg_income_per_cluster, x='Income', y=avg_income_per_cluster.index, width=500, height=400,
                             orientation='h', title='<b> Avg. Income (US $K) per Cluster</b>', color=avg_income_per_cluster.index,
                             color_discrete_sequence=['#0083B8', '#68b800', '#b80062'], template='plotly_white')
fig_income_per_cluster.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis=(dict(showgrid=False)))


### For Debt
avg_debt_per_cluster = df_filtered.groupby('Cluster')['Debt'].mean()
fig_debt_per_cluster = px.bar(avg_debt_per_cluster, x='Debt', y=avg_debt_per_cluster.index, width=500, height=400,
                             orientation='h', title='<b> Avg. Debt per Cluster</b>', color=avg_debt_per_cluster.index,
                             color_discrete_sequence=['#0083B8', '#68b800', '#b80062'], template='plotly_white')
fig_debt_per_cluster.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis=(dict(showgrid=False)))

### For Debt Income Ratio
avg_debt_income_ratio_per_cluster = df_filtered.groupby('Cluster')['DebtIncomeRatio'].mean()
fig_debt_income_ratio_per_cluster = px.bar(avg_debt_income_ratio_per_cluster, x='DebtIncomeRatio',
                                           y=avg_debt_income_ratio_per_cluster.index, width=500, height=400, orientation='h',
                                           title='<b> Avg. Debt Income Ratio per Cluster</b>', color=avg_income_per_cluster.index,
                                           color_discrete_sequence=['#0083B8', '#68b800', '#b80062'],
                                           template='plotly_white')
fig_debt_income_ratio_per_cluster.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis=(dict(showgrid=False)))


### Setting the display layout
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_age_per_cluster, use_container_with=True)
left_column.plotly_chart(fig_income_per_cluster, use_container_with=True)
right_column.plotly_chart(fig_debt_per_cluster, use_container_with=True)
right_column.plotly_chart(fig_debt_income_ratio_per_cluster, use_container_with=True)


# HIDE STREAMLIT STYLE
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)






