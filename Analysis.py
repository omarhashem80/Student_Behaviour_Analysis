import streamlit as st
import main
import plotly.express as px
from Plots import DataAnalysis

da = DataAnalysis(main.df)
df = main.df
cats = [col.replace('_', ' ').title() for col in main.cat_cols]
nums = [col.replace('_', ' ').title() for col in main.num_cols]

cats_without_department = cats.copy()
cats_without_department.remove('Department')


def eda():

    uni_variate, bi_variate, multi_variate, bca, commerce, ism, accounting, questions = st.tabs(
        ['Univariate', 'Bivariate', 'Multivariate', 'BCA Department', 'Commerce Department',
         'B.com ISM Department', 'B.com Accounting and Finance Department', 'Questions'])

    with uni_variate:
        st.subheader('Descriptive statistics for Categorical Features')
        st.dataframe(df.describe(include='O'))

        st.subheader('Contribution')
        cat_feature = st.selectbox('Select a categorical feature', cats, key=1)
        st.plotly_chart(da.plot_uni_variate_categorical(cat_feature))

        st.subheader('Descriptive statistics for Numerical Features')
        st.dataframe(df.describe())

        st.subheader('Distribution')
        num_feature = st.selectbox('Select a numerical feature', nums, key=2)
        st.plotly_chart(da.plot_uni_variate_numerical(num_feature))

    with bi_variate:
        st.subheader('Categorical vs Numerical Analysis')
        cat = st.selectbox('Select a categorical feature', cats, key=3)
        num = st.selectbox('Select a numerical feature', nums, key=4)
        st.plotly_chart(da.plot_bi_variate_categorical_vs_numerical(num, cat))

        st.subheader('Numerical vs Numerical Analysis')
        st.plotly_chart(da.generate_correlation_heatmap(main.num_cols))
        bi_num = st.multiselect('Select two numerical features', nums, key=5, max_selections=2)
        if len(bi_num) == 2:
            st.plotly_chart(da.scatterplot_bi_variate_numerical_vs_numerical(bi_num[0], bi_num[1]))

    with multi_variate:
        st.subheader('Categorical vs Categorical vs Numerical Analysis')
        multi_features = st.multiselect('Select two categorical features', cats, key=6, max_selections=2)
        y = st.selectbox('Select a numerical feature', nums, key=7)
        if len(multi_features) == 2:
            st.plotly_chart(da.multivariate_analysis(multi_features[0], y, multi_features[1]))
        cat_features = cats.copy()
        cat_features.remove('Department')
        cat_features.remove('Bmi')
        st.subheader('Comparison of College Marks and Categorical Features Across Departments')
        st.markdown(main.departments)
        for cat_col in cat_features:
            st.plotly_chart(da.multivariate_analysis(cat_col, 'College Mark', 'Department'))
            st.write('Note:')
            lab = cat_col.replace(' ', '_').lower()
            st.markdown(main.formatted_data[lab])

    with bca:
        st.subheader('Top 20 Students in BCA Department Achieving High Marks by Doing These Things')
        bca_da = DataAnalysis(main.BCA)
        for col in cats_without_department:
            st.plotly_chart(bca_da.plot_uni_variate_categorical(col))

    with commerce:
        st.subheader('Top 20 Students in Commerce Department Achieving High Marks by Doing These Things')
        commerce_da = DataAnalysis(main.Commerce)
        for col in cats_without_department:
            st.plotly_chart(commerce_da.plot_uni_variate_categorical(col))

    with ism:
        st.subheader('Top 20 Students in B.com ISM Department Achieving High Marks by Doing These Things')
        ism_da = DataAnalysis(main.Ism)
        for col in cats_without_department:
            st.plotly_chart(ism_da.plot_uni_variate_categorical(col))

    with accounting:
        st.subheader('Top 20 Students in B.com Accounting and Finance Department Achieving High Marks by'
                     ' Doing These Things')
        accounting_da = DataAnalysis(main.Accounting)
        for col in cats_without_department:
            st.plotly_chart(accounting_da.plot_uni_variate_categorical(col))

    with questions:
        st.header('Analysis Questions')
        # Question 1
        st.subheader('What is the effect of hobby preferences among students on college marks?')
        dff_q1 = df.groupby('hobbies')[['college_mark']].mean().sort_values(by='college_mark').reset_index()
        st.plotly_chart(px.histogram(dff_q1, x='hobbies', y='college_mark', text_auto='.2f')
                        .update_layout(xaxis_title='Hobbies', yaxis_title='College Mark',
                                       title='Effect of Hobby Preferences on College Marks'))

        # Question 2
        st.subheader('How does gender impact the willingness to pursue a career based on their degree?')
        st.plotly_chart(
            px.histogram(df, x='degree_driven_career_aspirations', color='gender', text_auto='.2f', barmode='group')
            .update_layout(xaxis_title='Degree Driven Career Aspirations', yaxis_title='Count',
                           title='Impact of Gender on Career Aspirations'))

        # Question 3
        st.subheader(
            'What is the correlation between daily studying time and academic performance among BCA students?')
        dff_q3 = df[df['department'] == 'BCA']
        dff_q3 = dff_q3.groupby('daily_studying_time')[['college_mark']].mean().reset_index().sort_values(
            by='college_mark')
        st.plotly_chart(px.histogram(dff_q3, x='daily_studying_time', y='college_mark', text_auto='.2f')
                        .update_layout(xaxis_title='Daily Studying Time', yaxis_title='College Mark',
                                       title='Correlation: Daily Studying Time and College Marks for BCA Students'))

        # Question 4
        st.subheader('What are the most common hobbies among students who prefer studying in the morning, afternoon'
                     ', and night?')
        st.plotly_chart(px.histogram(df, x='hobbies', color='prefer_to_study_in', text_auto='.2f', barmode='group')
                        .update_layout(xaxis_title='Hobbies', yaxis_title='Count',
                                       title='Hobbies of Students by Preferred Study Time'))

        # Question 5
        st.subheader(
            'How does gender impact salary expectations among BCA students pursuing certification courses?')
        dff_q5 = df[(df['department'] == 'BCA') & (df['certification_course'] == 'Yes')][
            ['gender', 'salary_expectation']]
        dff_q5 = dff_q5.groupby('gender')[['salary_expectation']].mean().reset_index().sort_values(
            by='salary_expectation')
        st.plotly_chart(px.histogram(dff_q5, x='gender', y='salary_expectation', text_auto='.2f')
                        .update_layout(xaxis_title='Gender', yaxis_title='Average Salary Expectation',
                                       title='Impact of Gender on Salary Expectations for BCA Students with'
                                             ' Certification Courses'))

        # Question 6
        st.subheader('How does the preference for social media and video consumption differ based on the department'
                     ' or gender of students?')
        st.plotly_chart(
            px.histogram(df, x='social_media_and_video', color='department', text_auto='.2f', barmode='group')
            .update_layout(xaxis_title='Social Media and Video Preference', yaxis_title='Count',
                           title='Preference Distribution by Department'))
        st.plotly_chart(
            px.histogram(df, x='social_media_and_video', color='gender', text_auto='.2f', barmode='group')
            .update_layout(xaxis_title='Social Media and Video Preference', yaxis_title='Count',
                           title='Preference Distribution by Gender'))

        # Question 7
        st.subheader('Do students who engage in part-time jobs have different academic performance compared to '
                     'those who don\'t?')
        st.plotly_chart(
            px.histogram(df, x='part_time_job', y='college_mark', text_auto='.2f', barmode='group', histfunc='avg')
            .update_layout(xaxis_title='Part-Time Job', yaxis_title='Average College Mark',
                           title='Impact of Part-Time Jobs on Academic Performance'))

        # Question 8
        st.subheader('Are there any variations in stress levels based on financial status or traveling time?')
        st.plotly_chart(
            px.histogram(df, x='stress_level', color='financial_status', text_auto='.2f', barmode='group')
            .update_layout(xaxis_title='Stress Level', yaxis_title='Count',
                           title='Stress Levels Based on Financial Status'))
        st.plotly_chart(px.histogram(df, x='stress_level', color='travelling_time', text_auto='.2f', barmode='group')
                        .update_layout(xaxis_title='Stress Level', yaxis_title='Count',
                                       title='Stress Levels Based on Traveling Time'))

        # Question 9
        st.subheader('What is the overall satisfaction level with the chosen degree among students, and does it '
                     'differ based on gender or department?')
        st.plotly_chart(px.histogram(df, x='degree_satisfaction', color='gender', text_auto='.2f', barmode='group')
                        .update_layout(xaxis_title='Degree Satisfaction', yaxis_title='Count',
                                       title='Satisfaction Level with Degree by Gender'))
        st.plotly_chart(
            px.histogram(df, x='degree_satisfaction', color='department', text_auto='.2f', barmode='group')
            .update_layout(xaxis_title='Degree Satisfaction', yaxis_title='Count',
                           title='Satisfaction Level with Degree by Department'))

        # Question 10
        st.subheader('Are students who have higher academic performance more likely to pursue a career based on '
                     'their degree, and does this vary across departments or gender?')
        st.plotly_chart(px.histogram(df, x='degree_driven_career_aspirations', y='college_mark', color='gender',
                                     text_auto='.2f', barmode='group', histfunc='avg')
                        .update_layout(xaxis_title='Degree Driven Career Aspirations',
                                       yaxis_title='Average College Mark',
                                       title='Impact of Degree Driven Career Aspirations on Academic Performance by'
                                             ' Gender'))
        st.plotly_chart(px.histogram(df, x='degree_driven_career_aspirations', y='college_mark', color='department',
                                     text_auto='.2f', barmode='group', histfunc='avg')
                        .update_layout(xaxis_title='Degree Driven Career Aspirations',
                                       yaxis_title='Average College Mark',
                                       title='Impact of Degree Driven Career Aspirations on Academic Performance by'
                                             ' Department'))
        for header, features in main.multi_dict.items():
            st.subheader(header)
            st.plotly_chart(da.multivariate_analysis(*features))

