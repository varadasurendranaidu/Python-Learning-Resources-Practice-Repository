"""
Python Learning Resources & Practice Repository

Topics:
1. Variables and data types
2. Lists and dictionaries
3. Functions
4. Input validation
5. Practice questions
"""

def variables_demo():
    print("\n--- Variables and Data Types ---")

    name = "Surendra"
    age = 20
    marks = 85.5
    is_student = True

    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)
    print("Student:", is_student)


def lists_demo():
    print("\n--- Lists ---")

    numbers = [10, 20, 30, 40, 50]

    print("Numbers:", numbers)
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])
    print("Sum:", sum(numbers))
    print("Maximum:", max(numbers))


def dictionaries_demo():
    print("\n--- Dictionaries ---")

    student = {
        "name": "Rahul",
        "age": 20,
        "marks": 88
    }

    for key, value in student.items():
        print(f"{key}: {value}")


def functions_demo():
    print("\n--- Functions ---")

    def calculate_average(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    scores = [80, 90, 75, 85]

    print("Scores:", scores)
    print("Average:", calculate_average(scores))


def input_validation_demo():
    print("\n--- Input Validation ---")

    while True:
        user_input = input("Enter an integer between 1 and 100: ")

        try:
            number = int(user_input)

            if 1 <= number <= 100:
                print("Valid number:", number)
                break

            print("Number must be between 1 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def practice_questions():
    print("\n--- Practice Questions ---")

    questions = [
        "1. Find the largest number in a list.",
        "2. Count vowels in a string.",
        "3. Remove duplicates from a list.",
        "4. Write a function to check whether a number is prime.",
        "5. Count the frequency of each word in a sentence."
    ]

    for question in questions:
        print(question)


def main():
    while True:
        print("\n===== PYTHON LEARNING RESOURCES =====")
        print("1. Variables and Data Types")
        print("2. Lists")
        print("3. Dictionaries")
        print("4. Functions")
        print("5. Input Validation")
        print("6. Practice Questions")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            variables_demo()
        elif choice == "2":
            lists_demo()
        elif choice == "3":
            dictionaries_demo()
        elif choice == "4":
            functions_demo()
        elif choice == "5":
            input_validation_demo()
        elif choice == "6":
            practice_questions()
        elif choice == "0":
            print("Thank you for learning Python!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
