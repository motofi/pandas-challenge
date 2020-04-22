
import pandas as pd

school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

school_data_complete.head()

total_schools = school_data_complete["school_name"].value_counts()
total_students = school_data_complete["Student ID"].value_counts()
total_budget = school_data["budget"].sum()
avg_mathscore = student_data["math_score"].mean()
avg_readscore = student_data["reading_score"].mean()
overall_passing_rate = (avg_mathscore + avg_readscore) / 2

mathscores_df = student_data["math_score"]
passing_criteria1 = mathscores_df > 69
passing_mathscores_df = mathscores_df[passing_criteria1]
num_passing_math = passing_mathscores_df.shape[0]

readingscores_df = student_data["reading_score"]
passing_criteria2 = readingscores_df > 69
passing_readingscores_df = readingscores_df[passing_criteria2]
num_passing_reading = passing_readingscores_df.shape[0]

percent_passing_math = 100*(num_passing_math/len(total_students))
percent_passing_reading = 100*(num_passing_reading/len(total_students))

district_summary_df = pd.DataFrame({"Total Schools": [len(total_schools)],
                                  "Total Students": [len(total_students)],
                                  "Total Budget": [total_budget],
                                  "Average Math Score": [avg_mathscore],
                                  "Average Reading Score": [avg_readscore],
                                  "% Passing Math": [percent_passing_math],
                                  "% Passing Reading": [percent_passing_reading],
                                  "% Overall Passing Rate": [overall_passing_rate]})


school_summary_df = school_data_complete.set_index("school_name")
school_summary_df.head()


#Creating the DataFrame and grouping by "school_name"
school_summary = total_df.groupby(["school_name"])
#school_summary.head()
print(school_summary["Student ID"].count())
print(school_summary["budget"].sum())
print((school_summary["budget"].sum()) / (school_summary["Student ID"].count()))

school_mathscores_df = school_summary["math_score"]
passing_criteria1 = mathscores_df > 69
passing_mathscores_df = mathscores_df[passing_criteria1]
num_passing_math = passing_mathscores_df.shape[0]

readingscores_df = school_summary["reading_score"]
passing_criteria2 = readingscores_df > 69
passing_readingscores_df = readingscores_df[passing_criteria2]
num_passing_reading = passing_readingscores_df.shape[0]

percent_passing_math = 100*(num_passing_math/len(total_students))
percent_passing_reading = 100*(num_passing_reading/len(total_students))


school_summary_df = pd.DataFrame({"School Type": [school_type],
                                  "Total Students": [total_students_school],
                                  "Total Budget": [total_budget_school],
                                  "Per Student Budget": [student_budget_school],
                                  "Average Math Score": [avg_mathscore_school],
                                  "Average Reading Score": [avg_readscore_school],
                                  "% Passing Math": [percent_passing_math_school],
                                  "% Passing Reading": [percent_passing_reading_school],
                                  "% Overall Passing Rate": [overall_passing_rate_school]})


school_summary_df.groupby(school_name)


school_summary_df = school_summary_df.set_index("school_name")
school_summary_df = pd.DataFrame(school_data_complete)
school_summary_df.groupyby(["school_name"])
