import streamlit as st
import main
from Analysis import eda
from Conclusion import conclusion


st.header('Student Behaviour Analysis')

page = st.sidebar.radio('Pages', ['Home', 'EDA', 'Conclusion'])


def home():
    st.subheader('This app is created to analyze the data of Student Behaviour')
    st.image('./assets/cover.jpg', caption='Massachusetts Institute of Technology')
    st.text('''
    This dataset contains information collected from university students
    through a Google form. It includes details such as certification courses,
    gender, department, height (in cm), weight (in kg), marks in 10th and 12th grade,
    college marks, hobbies, daily studying time, preferred study environment,
    salary expectations, satisfaction with their degree, willingness to pursue a career
    related to their degree, social media and video usage, traveling time,
    stress levels, and financial status.
    The dataset aims to provide insights into student behavior and can be used for 
    analysis and research purposes.
    ''')

    # Display column descriptions
    st.markdown("""
        <div style='text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 10px;'>
            Column Descriptions:
        </div>
        <ul style='list-style-type: square;'>
            <li><strong>Certification Course:</strong> Indicates whether the student has completed any certification course or not.</li>
            <li><strong>Gender:</strong> The gender of the student.</li>
            <li><strong>Department:</strong> The department or field of study the student is enrolled in.</li>
            <li><strong>Height (CM):</strong> The height of the student in centimeters.</li>
            <li><strong>Weight (KG):</strong> The weight of the student in kilograms.</li>
            <li><strong>tenth Mark:</strong> The student's marks obtained in the 10th grade.</li>
            <li><strong>twelfth Mark:</strong> The student's marks obtained in the 12th grade.</li>
            <li><strong>College Mark:</strong> The student's marks obtained in their college or university.</li>
            <li><strong>Hobbies:</strong> The hobbies or interests of the student.</li>
            <li><strong>Daily Studying Time:</strong> The amount of time the student spends studying on a daily basis.</li>
            <li><strong>Prefer to Study in:</strong> The preferred study environment or location of the student.</li>
            <li><strong>Salary Expectation:</strong> The student's expectation for their future salary.</li>
            <li><strong>Degree Satisfaction:</strong> The student's opinion on whether they like their degree or not.</li>
            <li><strong>Degree Driven Career Aspirations:</strong> The student's willingness to pursue a career related to their degree.</li>
            <li><strong>Social Media & Video:</strong> The student's engagement with social media and video platforms.</li>
            <li><strong>Traveling Time:</strong> The time it takes for the student to commute or travel to their educational institution.</li>
            <li><strong>Stress Level:</strong> The perceived stress level of the student.</li>
            <li><strong>Financial Status:</strong> The financial status or economic background of the student.</li>
            <li><strong>Part-time Job:</strong> Whether the student is engaged in a part-time job or not.</li>
        </ul>""", unsafe_allow_html=True)

    # Load data
    df = main.df

    # Show data
    st.write(df.head())

    st.markdown(
        '<a href="https://www.kaggle.com/datasets/gunapro/student-behavior"> <center> Link to Dataset</center> </a>',
        unsafe_allow_html=True
    )


# Use tabs for different pages
tabs = {
    'Home': home,
    'EDA': eda,
    'Conclusion': conclusion,
}

# Display the selected page
tabs[page]()
