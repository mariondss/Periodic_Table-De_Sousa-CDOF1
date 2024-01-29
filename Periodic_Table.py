class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer.lower()

    def display(self):
        result = self.prompt + "\n"
        for option in self.options:
            result += "- " + option + "\n"
        return result

    def check_answer(self, user_answer):
        return self.answer == user_answer.lower()


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.restart = True

    def run(self):
        while self.restart:
            self.score = 0
            for question in self.questions:
                print("\n")
                print(question.display() + "\nEnter your answer :")
                answer = input()
                if question.check_answer(answer):
                    self.score += 1
                print("\n")
            self.display_score()
            self.ask_restart()

    def display_score(self):
        if self.score == 0:
            print("Loser ! Your score is ", self.score)
        elif self.score in [1, 2, 3]:
            print("You are really not the best... Your score is ", self.score)
        elif self.score == 4:
            print("Almost perfect ! Your score is ", self.score)
        elif self.score == 5:
            print("Perfect ! Your score is ", self.score)

    def ask_restart(self):
        answer = ""
        while answer.lower() not in ["yes", "no"]:
            print("\nWould you like to try again ? (Yes or No) :")
            answer = input()
        if answer.lower() == "no":
            self.restart = False


question1 = Question("What does the letter H represent in the periodic table?", ["Helium", "Hydrogen", "Hafnium", "Holmium"], "Hydrogen")
question2 = Question("What does the letter C represent in the periodic table?", ["Calcium", "Cobalt", "Carbon", "Curium"], "Carbon")
question3 = Question("What does the letter N represent in the periodic table?", ["Neon", "Nickel", "Nitrogen", "Nihonium"], "Nitrogen")
question4 = Question("What does the letter O represent in the periodic table?", ["Oxygen", "Osmium", "Oganesson", "Ruthenium"], "Oxygen")
question5 = Question("What does the letter K represent in the periodic table?", ["Krypton", "Kryptonite", "Potassium", "Kurium"], "Potassium")

quiz = Quiz([question1, question2, question3, question4, question5])
quiz.run()