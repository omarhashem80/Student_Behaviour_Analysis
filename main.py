import pandas as pd

# Read CSV file
df = pd.read_csv('assets/Student_Behaviour.csv')


Ism = (df[df['department'] == 'B.com ISM']
       .sort_values(by='college_mark', ascending=False).head(20).reset_index(drop=True))
Accounting = (df[df['department'] == 'B.com Accounting and Finance ']
              .sort_values(by='college_mark', ascending=False).head(20).reset_index(drop=True))
BCA = df[df['department'] == 'BCA'].sort_values(by='college_mark', ascending=False).head(20).reset_index(drop=True)
Commerce = (df[df['department'] == 'Commerce']
            .sort_values(by='college_mark', ascending=False).head(20).reset_index(drop=True))

cat_cols = ['certification_course', 'department', 'gender', 'hobbies',
            'daily_studying_time', 'prefer_to_study_in',
            'degree_satisfaction', 'degree_driven_career_aspirations',
            'social_media_and_video', 'travelling_time', 'stress_level',
            'financial_status', 'part_time_job', 'bmi']

num_cols = ['tenth_mark', 'twelfth_mark', 'college_mark', 'salary_expectation']
departments = '''
1. **BCA:** Bachelor of Computer Applications. This program typically focuses on computer science and application
development.
2. **Commerce:** A general term for educational programs related to business, finance, and trade, often covering
subjects like accounting, economics, and management.
3. **B.com Accounting and Finance:** Bachelor of Commerce with a specialization in Accounting and Finance.
This program delves deeper into financial accounting, auditing, and financial management.
4. **B.com ISM:** Bachelor of Commerce in Information Systems Management. This program combines commerce subjects with
a focus on information systems and technology management.
'''
multi_dict = {
    'Stress Levels vs college Mark by Preferred Study Time': ['Stress Level', 'College Mark',
                                                              'Prefer To Study In'],
    'Travelling Time vs college Mark by Preferred Study Time': ['Travelling Time', 'College Mark',
                                                                'Prefer To Study In'],
    'Stress Levels vs college Mark by partTime Job': ['Stress Level', 'College Mark', 'Part Time Job'],
    'Daily Studying Time vs college Mark by Social Media And Video': ['Daily Studying Time', 'College Mark',
                                                                      'Social Media And Video'],
    'Daily Studying Time vs College Marks by partTimeJob': ['Daily Studying Time', 'College Mark',
                                                            'Part Time Job'],
    'Daily Studying Time vs College Mark by Travelling Time': ['Daily Studying Time', 'College Mark',
                                                               'Travelling Time'],
    'Daily Studying Time vs college Marks by Degree Satisfaction': ['Daily Studying Time', 'College Mark',
                                                                    'Degree Satisfaction'],
    'Daily Studying Time vs collegeMark by degree Driven Career Aspirations': ['Daily Studying Time',
                                                                               'College Mark',
                                                                               'Degree Driven Career '
                                                                               'Aspirations'],
    'Financial Status vs College Marks by partTime Job': ['Financial Status', 'College Mark', 'Part Time Job'],
    'Degree Satisfaction vs College Mark by Degree Driven Career Aspirations': ['Degree Satisfaction',
                                                                                'College Mark',
                                                                                'Degree Driven Career '
                                                                                'Aspirations'],
    'Degree Satisfaction vs College Mark by social Media And Video': ['Degree Satisfaction', 'College Mark',
                                                                      'Social Media And Video']
}


formatted_data = {
    'certification_course': '''Observing the data, it is evident that, 
across most departments, students who enrolled and 
successfully completed courses tend to have a higher 
average grade compared to their counterparts. However, 
an exception is observed in the B.com ISM department, 
where the opposite trend is noticed. Notably, 
the disparity is expected to be pronounced among B.com Accounting students,
while in the Commerce department, the difference is relatively modest.
The BCA department also shows a noticeable difference in average grades between the two groups of students.''',

    'gender': '''In this context, it is evident that the academic performance of females
in the Commerce and BCA departments surpasses that of males. Conversely,
the opposite pattern is observed in the departments of B.com ISM and B.com Accounting,
where male academic performance exceeds that of females.''',

    'hobbies': '''From this analysis, it becomes evident that Commerce students with high average scores tend to engage in
activities such as reading books and going to the movies. Similarly, Accounting students with high average
scores share these preferences for reading books and enjoying cinema. Conversely,
BCA students concentrate their hobbies on going to the cinema and reading books,
while B.com ISM students center their leisure activities around video games and playing sports.''',

    'daily_studying_time': '''Accounting and BCA students typically require three to four hours,
while Commerce students and B.com ISM students typically need one to two hours.''',

    'prefer_to_study_in': '''Commerce students exhibit higher average marks regardless of their study time,
and accounting students also achieve higher grades regardless of study time. However,
BCA students studying at night tend to have higher grades,
while ISM students performing well at any study time.
Conversely, looking from the lower end, accounting students and ICM students who study at night,
as well as commerce students in general, tend to have lower grades. In contrast, BCA students studying 
in the morning have comparatively lower grades.''',

    'degree_satisfaction': '''There is a notable disparity in the scores achieved by accounting students who
express satisfaction with their department compared to those who do not. 
The difference is somewhat less evident in ISM and Commerce, while in the case of BCA, 
the distinction is not as substantial.''',

    'degree_driven_career_aspirations': '''In the Commerce department, students who decided to work in the same field as their academic specialization,
constituting 100%,are those who achieve the highest average grades. Following them are those who made this decision
at a rate of 25%, then 75%, 50%, and finally 0%.For BCA students, those who decided at a rate of 100% are the ones who
cover a wide range of grades. Next are those who made this decision at 75%, followed by those at 25%, and the least at 0%.
In the case of ICM students, those who decided at a rate of 25% are the top achievers, followed by those at 50%, 75%,
and finally 100%.As for Accounting students, those who decided at a rate of 100% are the ones with the highest average grades
, followed by those at 25%, 75%, and 50%.''',

    'social_media_and_video': '''In the Accounting Department, we note that students who refrain from spending time on social media consistently
achieve high average grades. Interestingly, these scores remain equal across the two periods: one hour, one and a half 
hours, and more than two hours. Conversely, at the Ministry of Commerce, there is a clear difference between those who 
spend 30 to 60 minutes and those who spend an hour and a half. The decrease was noticeable from one minute to 30, and even 
more noticeable from one to one and a half hours, especially as social media use exceeded two hours. In the ISM section, 
peak performance occurs within a 1.5-hour time frame, while lowest scores are associated with more than 2 hours of social 
media use. The differences in the remaining periods are almost negligible. Moving to the BCA section, the highest average 
scores are observed among students who spend more than two hours on social media. We can say that viewing social media sites 
does not have a significant impact on students’ grades''',

    'travelling_time': '''In this context, we are discussing the correlation between average marks and the time students spend commuting to 
college. It is evident that among Commerce students, those who spend more than three hours commuting tend to have higher 
average grades, followed by those with durations of less than 30 minutes. Subsequently, students who commute between two 
and a half to three hours follow, and then those with durations ranging from one to one and a half hours. In the BCA department,
there is not a significant difference; however, students who spend between two and a half to three hours have slightly higher 
average grades.Shifting our focus to the ISM department, we observe that students who spend 30 to 60 minutes commuting have 
higher average grades, followed by those who spend less than 30 minutes. After them are students who spend between one to one 
and a half hours, and then those who spend almost equal amounts more than three hours and between two and a half to three hours.
For Accounting students, the highest average grades are among those who spend from two to two and a half hours, closely followed
by those who spend almost equal amounts less than half an hour and between one and a half to three hours. The lowest average 
grades are observed among students who take less than one and a half hours.''',

    'stress_level': '''In the realm of BCA students, those experiencing a good level of pressure achieve the highest average grades,
followed by those facing an awful level of pressure, then students dealing with a bad level of pressure, and finally,
those with a fabulous level of pressure. Interestingly, students experiencing a fabulous level of pressure emerge with
the highest average grades.Turning to ISM students, those encountering a good level of pressure secure the highest average
grades, followed by those facing a bad level of pressure, then students with a fabulous level of pressure, and lastly, 
students with an awful level of pressure. Meanwhile, for accounting students, those under an awful level of pressure garner 
the highest grades, followed by those with a bad level of pressure, and then students with a fabulous level of pressure. 
Surprisingly, there is an equal standing between those with a fabulous and awful level of pressure, with the least performance 
observed among those facing a good level of pressure.''',

    'financial_status': '''Commerce students with a good financial standing attain a higher average score compared to their peers.
Following them are students with a fabulous financial level, succeeded by those with an awful financial standing.
Next in line are students with a bad financial level.For BCA students, irrespective of whether their financial level 
is good, bad, or awful, they achieve the same average grades. Notably, those with a fabulous financial level exhibit 
the lowest average grades.In the case of accounting students, those with an awful financial level achieve the highest 
average grades.Among ICM students, those with a bad financial standing secure the highest average grades, followed by 
those with a good financial level, and then those with an awful financial level.''',

    'part_time_job':'''The average marks of Accounting students who work part-time are higher than those who do not, 
showing a noticeable difference. In contrast, Commerce and BCA students exhibit an almost insignificant 
difference in their averages. Additionally, the average marks of ISM students who work are lower than their counterparts.'''
}

