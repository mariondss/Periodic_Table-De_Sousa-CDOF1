from enum import Enum

class Score(Enum):
    LOSER = 0
    NOT_BEST = range(1, 4)
    ALMOST_PERFECT = 4
    PERFECT = 5

class Question:
    """This class represents a question in the quiz."""
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def display(self):
        """This method displays the question and its options."""
        result = self.prompt + "\n"
        for i, option in enumerate(self.options, start=1):
            result += f"{i}. {option}\n"
        return result

    def check_answer(self, user_answer):
        """This method checks if the user's answer is correct."""
        return self.answer == self.options[int(user_answer) - 1]

class Quiz:
    """This class represents the quiz."""
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.restart = True

    def run(self, interface):
        """This method runs the quiz."""
        while self.restart:
            self.score = 0
            for question in self.questions:
                interface.display_question(question)
                answer = interface.get_answer(question)
                if question.check_answer(answer):
                    self.score += 1
                print(f"Your current score is: {self.score}")
            interface.display_score(self.score)
            self.restart = interface.ask_restart()

class QuizInterface:
    """This class handles user interactions."""
    @staticmethod
    def display_question(question):
        """This method displays a question."""
        print(question.display())

    @staticmethod
    def get_answer(question):
        """This method gets the user's answer."""
        while True:
            answer = input("Enter the number of your answer: ")
            if answer.isdigit() and 1 <= int(answer) <= len(question.options):
                return answer
            else:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def display_score(score):
        """This method displays the user's score."""
        if score == Score.LOSER.value:
            print("Loser! Your score is ", score)
        elif score in Score.NOT_BEST.value:
            print("You are really not the best... Your score is ", score)
        elif score == Score.ALMOST_PERFECT.value:
            print("Almost perfect! Your score is ", score)
        elif score == Score.PERFECT.value:
            print("Perfect! Your score is ", score)

    @staticmethod
    def ask_restart():
        """This method asks the user if they want to restart the quiz."""
        answer = ""
        while answer.lower() not in ["yes", "no"]:
            print("\nWould you like to try again? (Yes or No):")
            answer = input()
        return answer.lower() == "yes"


question1 = Question("What does the letter H represent in the periodic table?", ["Helium", "Hydrogen", "Hafnium", "Holmium"], "Hydrogen")
question2 = Question("What does the letter C represent in the periodic table?", ["Calcium", "Cobalt", "Carbon", "Curium"], "Carbon")
question3 = Question("What does the letter N represent in the periodic table?", ["Neon", "Nickel", "Nitrogen", "Nihonium"], "Nitrogen")
question4 = Question("What does the letter O represent in the periodic table?", ["Oxygen", "Osmium", "Oganesson", "Ruthenium"], "Oxygen")
question5 = Question("What does the letter K represent in the periodic table?", ["Krypton", "Kryptonite", "Potassium", "Kurium"], "Potassium")

quiz = Quiz([question1, question2, question3, question4, question5])
interface = QuizInterface()
quiz.run(interface)