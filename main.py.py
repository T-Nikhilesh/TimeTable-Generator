def generate_timetable():
    num_theory_subjects = int(input("Enter the number of theory subjects: "))
    num_analytic_subjects = int(input("Enter the number of analytic subjects: "))
    num_lab_slots = int(input("Enter the number of lab slots per week: "))
    num_theory_periods_per_day = int(input("Enter the number of theory periods per day: "))

    days_of_week = 6
    periods_per_day = 7
    morning_periods = 2
    afternoon_periods = 3

    # Validate input constraints
    if num_theory_subjects < 0 or num_analytic_subjects < 0 or num_lab_slots < 0 or num_theory_periods_per_day < 0:
        print("Invalid input")
        return

    if num_lab_slots > afternoon_periods:
        print("Invalid input: Number of lab slots exceeds available afternoon periods")
        return

    total_subjects = num_theory_subjects + num_analytic_subjects

    # Calculate the number of periods each subject should have
    num_periods_per_subject = []
    for i in range(total_subjects):
        if i < num_theory_subjects:
            num_periods_per_subject.append(num_theory_periods_per_day)
        else:
            num_periods_per_subject.append(2)

    # Generate timetable
    timetable = [['' for _ in range(periods_per_day)] for _ in range(days_of_week)]
    lab_count = 0

    # Assign subjects to morning periods
    for day in range(days_of_week):
        for period in range(morning_periods):
            subject_index = (day + period) % total_subjects
            subject_type = "Theory" if subject_index < num_theory_subjects else "Analytic"
            timetable[day][period] = f"{subject_type} {subject_index + 1}"
            num_periods_per_subject[subject_index] -= 1

    # Assign lab slots
    for subject_index in range(total_subjects):
        if subject_index >= num_theory_subjects:
            if lab_count < num_lab_slots:
                for day in range(days_of_week):
                    if timetable[day][afternoon_periods] == '':
                        timetable[day][afternoon_periods] = f"Lab {lab_count + 1}"
                        timetable[day][afternoon_periods + 1] = f"Lab {lab_count + 1}"
                        timetable[day][afternoon_periods + 2] = f"Lab {lab_count + 1}"
                        lab_count += 1
                        break

    # Assign analytic subjects to remaining periods
    for subject_index in range(total_subjects):
        if subject_index >= num_theory_subjects:
            subject_type = "Analytic"
            num_periods = num_periods_per_subject[subject_index]
            for day in range(days_of_week):
                for period in range(morning_periods, periods_per_day):
                    if num_periods == 0:
                        break
                    if timetable[day][period] == '':
                        timetable[day][period] = f"{subject_type} {subject_index + 1}"
                        num_periods -= 1

    # Add club activity and library period
    for day in range(days_of_week):
        if timetable[day][morning_periods] == '':
            timetable[day][morning_periods] = "Club Activity"
        if timetable[day][periods_per_day - 1] == '':
            timetable[day][periods_per_day - 1] = "Library Period"

    # Print the timetable
    print("Timetable:")
    for day in range(days_of_week):
        print(f"Day {day + 1}:")
        for period in range(periods_per_day):
            print(f"Period {period + 1}: {timetable[day][period]}")
        print()

# Generate the timetable based on user inputs
generate_timetable()

