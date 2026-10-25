"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost
    


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day_cost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return day_cost
    


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = annual_cost / (SEMESTERS_PER_YEAR * credits)
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = (CS1430_CREDITS / credits ) * (cost_per_semester(annual_cost) /(CS1430_MEETINGS_PER_SEMESTER))
    return class_cost

def cost_per_minute(annual_cost, credits):
    """Give back what one minute of being late to C 1430 costs."""
    minute_cost = cost_per_class(annual_cost, credits) / 50
    return minute_cost


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the annual cost of college: "))
    credits = int(input("Enter the number of credits you are taking this semester: "))
    while True:
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost if you are one minute late to CS1430")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        elif choice == "1":
            semester = cost_per_semester(annual_cost)
            print(f"One semester costs: ${semester:.2f}")

        elif choice == "2":
            month = cost_per_month(annual_cost)
            print(f"One month costs: ${month:.2f}")  
        
        elif choice == "3":
            day = cost_per_day(annual_cost)
            print(f"One class day costs: ${day:.2f}")

        elif choice == "4":
            credit = cost_per_credit(annual_cost, credits)
            print(f"One credit costs: ${credit:.2f}")

        elif choice == "5":
            class_cost = cost_per_class(annual_cost, credits)
            print(f"One CS 1430 class meeting costs: ${class_cost:.2f}")

        elif choice == "6":
            minute = cost_per_minute(annual_cost, credits)
            print(f"One minute costs: ${minute:.2f}")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
