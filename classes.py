import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.questions_asked = 0

    def percentage(self):
        if self.score > 0 and self.questions_asked > 0:
            return round((self.score / self.questions_asked * 100), 1)
        else:
            return 0


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_question(self):
        print(self.question)

    def validate(self, input):
        correct_responses = [
            "🎉 Boom! You got it right! 🎉",
            "🌟 Spot on! You’re a star! 🌟",
            "🎯 Bullseye! Nailed it! 🎯",
            "🌍 Worldly wisdom! That’s correct! 🌍",
            "🎊 Yes! You’re on fire! 🎊",
        ]

        incorrect_responses = [
            "🙈 Oops! Close, but not quite.",
            "💥 Almost! Keep going, you’ve got this!",
            "😬 Swing and a miss! Try again!",
            "❌ Nope! But don’t give up yet!",
            "🌧️ A little off target! Let’s keep exploring!",
        ]

        if self.answer == input:
            print(f"{random.choice(correct_responses)}\n")
            return True
        else:
            print(f"{random.choice(incorrect_responses)}\n")
            print(f"💡 Did you know? The correct answer is: {self.answer}. 💡")
            return False
