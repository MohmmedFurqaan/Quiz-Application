class LoadQuestion:
    def __init__(self, category, subcategory,question, options, answer):
        self.category = category
        self.subcategory = subcategory
        self.question = question
        self.options = options
        self.answer = answer.upper()

    def check_correct(self, answer):
        return answer.strip().upper() == self.answer

    def display_question(self, index):
        print(f'\nQuestion {index + 1}: {self.question}')
        for i, option in enumerate(self.options):
            print(f'{chr(65 + i)}. {option}')