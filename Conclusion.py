import streamlit as st

conclusion_text = '''**Conclusion:**

Analyzing the multifaceted relationship between various factors and academic performance across different departments 
yields valuable insights. Here are key takeaways from the observations:

1. **Departmental Variances:**
   Academic performance varies significantly among departments, with notable exceptions in certain specializations. 
While most departments exhibit higher grades for students who complete courses, the B.com ISM department stands out 
with a contrary trend. The disparities are more pronounced in B.com Accounting and relatively modest in Commerce, 
with the BCA department showing noticeable differences.

3. **Hobbies and Academic Performance:**
   Student hobbies align with their academic success. Commerce and Accounting students with high grades share 
preferences for reading and movies. BCA students focus on cinema and books, while B.com ISM students lean towards 
video games and sports.

3. **Study Time Patterns:**
   Varied study time patterns emerge, with Commerce and Accounting students exhibiting higher grades regardless of 
study time. BCA students studying at night tend to perform well, and B.com ISM students show consistent performance 
across study times.

4. **Satisfaction with Department:**
   Disparities in average scores are evident among accounting students expressing satisfaction with their department,
while differences are less pronounced in ISM and Commerce, and negligible in BCA.

5. **Career Aspirations and Academic Performance:**
   The decision to work in the same field as academic specialization correlates with higher average grades,
with nuances varying across departments.

6. **Social Media Impact:**
   Social media use shows varied impacts on academic performance across departments, with Accounting students achieving
high grades by refraining from social media. Conversely, Commerce students' performance varies based on usage
duration.

7. **Commute Time and Academic Performance:**
   Commute time correlates with academic performance, with notable variations among departments. Commerce students 
with longer commutes achieve higher grades, while ISM students with shorter commutes perform better.

8. **Stress Levels and Academic Performance:**
   Stress levels are linked to academic success, with nuances across departments. BCA and ISM students facing higher
pressure achieve higher grades, while Accounting students under awful pressure perform best.

9. **Financial Status Impact:**
    Financial standing correlates with academic performance, with nuances. Commerce students with good financial
standing outperform others, while BCA students exhibit consistent grades across financial levels. Accounting
students with awful financial standing achieve the highest grades.

10. **Part-time Jobs and Academic Performance:**
    The impact of part-time jobs on academic performance varies, with Accounting students benefiting the most.
Commerce and BCA students show minimal differences, while ISM students who work tend to have lower averages.

In summary, academic performance is influenced by a complex interplay of factors, emphasizing the need for tailored
interventions based on department-specific dynamics and individual student characteristics. Understanding these nuances
can inform targeted strategies to enhance student success and well-being.'''


def conclusion():
    st.markdown(conclusion_text)

