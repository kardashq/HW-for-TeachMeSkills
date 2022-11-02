"""Task:
https://colab.research.google.com/drive/1kd5YBvmE3gU5lv-btCPBh-cbAwqbjpwR?usp=sharing
"""


from random import shuffle


class Mystery:
    complexity = None

    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.answer = answer
        self.choices = choices
        self.choices.append(answer)
        shuffle(choices)

    def quiz(self):
        print(self.question)
        for i, v in enumerate(self.choices):
            print(f'\t{i}: {v}')
        user_input = input('Select option, "skip" for skip question: ')
        if user_input.lower() == 'skip':
            return 0
        elif self.choices[int(user_input)] == self.answer:
            return True
        else:
            return False


q1 = Mystery(question="Откуда на Беларусь готовилось нападение?",
             answer="Там 4 позиции, я карту принёс, сейчас покажу",
             choices=[
                 "Откуда мне знать?",
                 "Со склада грязи.",
                 "С планеты Нибиру.",
                 "С загнивающег запада."
             ])
print(q1.quiz())