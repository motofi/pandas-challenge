# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


school_data_complete.head()

school_data_complete["math_score"].describe()

total_schools = school_data_complete["school_name"].value_counts()
#len(total_schools)
total_students = school_data_complete["Student ID"].value_counts()
#to output *only* the value ---  len(total_students)
total_budget = school_data["budget"].sum()
#see if you can format the output into currency for budget
avg_mathscore = student_data["math_score"].mean()
avg_readscore = student_data["reading_score"].mean()
overall_passing_rate = (avg_mathscore + avg_readscore) / 2

# Converting the membership days into weeks and then adding a column to the DataFrame
#weeks = training_df["Membership (Days)"]/7
#training_df["Membership (Weeks)"] = weeks

#training_df.head()


#create variable for number of values above 69
#divide that number by total number values for student grades


#passing_mathscores = student_data["math_score"] > 69
#len(passing_mathscores)
#passing_mathscores_df = student_data["math_score"]
#passing_mathscores_df.loc[[int("math_score")] > 69].sum

#values above 69 quantity
#---of those values/total_students
#percent_passing_read =
#avg_passing_rate =
#average of the previous two

# Place all of the data found into a summary DataFrame
district_summary_df = pd.DataFrame({"Total Schools": [len(total_schools)],
                                  "Total Students": [len(total_students)],
                                  "Total Budget": [total_budget],
                                  "Average Math Score": [avg_mathscore],
                                  "Average Reading Score": [avg_readscore],
                                  "% Passing Math": [len(total_students)],
                                  "% Passing Reading": [len(total_students)],
                                  "% Overall Passing Rate": [overall_passing_rate]})

#format total budget as currency
#still need figures for %passing math / % passing reading
#optional - table formatting
school_summary_df = school_data_complete.set_index("school_name")
school_summary_df.head()

school_summary_df
school_summary_df = pd.DataFrame({"School Type": [len(total_schools)],
                                  "Total Students": [len(total_students)],
                                  "Total School Budget": [len(total_students)],
                                  "Total Student Budget": [total_budget],
                                  "Average Math Score": [avg_mathscore],
                                  "Average Reading Score": [avg_readscore],
                                  "% Passing Math": [len(total_students)],
                                  "% Passing Reading": [len(total_students)],
                                  "% Overall Passing Rate": [overall_passing_rate]})


school_summary_df





### Top Performing Schools (By Passing Rate)

* Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Bottom Performing Schools (By Passing Rate)

* Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.

### Math Scores by Grade\*\*

* Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

### Reading Scores by Grade

* Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

### Scores by School Spending

* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Scores by School Size

* Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).

### Scores by School Type

* Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).

# As final considerations:
#
# * Use the pandas library and Jupyter Notebook.
# * You must submit a link to your Jupyter Notebook with the viewable Data Frames.
# * You must include a written description of at least two observable trends based on the data.
# * See [Example Solution](PyCitySchools/PyCitySchools_starter.ipynb) for a reference on the expected format.

## Hints and Considerations
#
# * These are challenging activities for a number of reasons.
# For one, these activities will require you to analyze thousands of records.
# Hacking through the data to look for obvious trends in Excel is just not a feasible option.
# The size of the data may seem daunting, but pandas will allow you to efficiently parse through it.
#
# * Second, these activities will also challenge you by requiring you to learn on your feet.
# Don't fool yourself into thinking: "I need to study pandas more closely before diving in."
# Get the basic gist of the library and then _immediately_ get to work.
# When facing a daunting task, it's easy to think: "I'm just not ready to tackle it yet."
# But that's the surest way to never succeed.
# Learning to program requires one to constantly tinker, experiment, and learn on the fly.
# You are doing exactly the _right_ thing, if you find yourself constantly practicing Google-Fu and diving into documentation.
# There is just no way (or reason) to try and memorize it all.
# Online references are available for you to use when you need them. So use them!
#
# * Take each of these tasks one at a time.
# Begin your work, answering the basic questions:
# "How do I import the data?" "How do I convert the data into a DataFrame?" "How do I build the first table?"
# Don't get intimidated by the number of asks. Many of them are repetitive in nature with just a few tweaks.
# Be persistent and creative!
