import time
import threading
import random
from quiz_loader import QuizLoader

class Quiz:
    def __init__(self, questions, time_limit=10):
        self.questions = questions
        self.time_limit = time_limit
        self.time_expired = threading.Event()

    def filter_question(self, category, subcategory):
        return [q for q in self.questions if q.category == category and q.subcategory == subcategory]
    
    def select_option(self, prompt, options):
        while True:
            print(f'\n{prompt}')
            for i, option in enumerate(options):
                print(f'{i + 1}. {option}')

            try:
                choice = int(input(f'Select an option (1-{len(options)}): '))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print('Invalid choice! Try again.')
            except ValueError:
                print('Enter a valid integer!')

    def get_number_of_questions(self, max_number):
        while True:
            try:
                num_to_ask = int(input(f'Enter the number of questions to be asked (1-{max_number}): '))
                if 1 <= num_to_ask <= max_number:
                    return num_to_ask
                else:
                    print(f'Please enter a valid number between 1 and {max_number}.')
            except ValueError:
                print('Enter a number, not a string!')

    def ask_question_with_timer(self, question):
        self.time_expired.clear()
        answer_received = False
        result = False

        def timer():
            nonlocal answer_received, result
            time.sleep(self.time_limit)
            if not answer_received:
                self.time_expired.set()
                print(f'\nTime expired! The correct answer was: {question.answer}\n')

        timer_thread = threading.Thread(target=timer, daemon=True)
        timer_thread.start()

        # Display the question first
        question.display_question(0)

        while not self.time_expired.is_set() and not answer_received:
            try:
                answer = input('Enter your answer (A, B, C, D): ').strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    answer_received = True
                    correct_option = question.options[ord(question.answer) - 65]
                    user_option = question.options[ord(answer) - 65]
                    if user_option == correct_option:
                        print('Correct!')
                        result = True
                    else:
                        print(f'Wrong! The correct answer is: {question.answer}')
                        result = False
                else:
                    print('Enter a valid choice (A, B, C, D).')
            except ValueError:
                print('Enter a valid response!')
                answer_received = True
                result = False

        # Wait for the timer thread to finish if answer was received before timeout
        if answer_received and timer_thread.is_alive():
            timer_thread.join(timeout=0.1)  # Small timeout to avoid hanging

        return result

    def conduct(self):
        if not self.questions:
            print('No available questions!')
            return
        
        categories = list(set(q.category for q in self.questions))
        category = self.select_option('Available Categories:', categories)

        subcategories = list(set(q.subcategory for q in self.questions if q.category == category))
        subcategory = self.select_option('Available Subcategories:', subcategories)

        filtered_questions = self.filter_question(category, subcategory)
        if not filtered_questions:
            print('No questions available!')
            return
        
        random.shuffle(filtered_questions)
        num_questions = len(filtered_questions)
        num_to_ask = self.get_number_of_questions(num_questions)

        print('Starting the Quiz! Good luck!\n')
        score = 0
        for question in filtered_questions[:num_to_ask]:
            if self.ask_question_with_timer(question):
                score += 1

        print(f'\nQuiz Completed! Your final score is: {score}/{num_to_ask}')
        print('Thanks for playing!')