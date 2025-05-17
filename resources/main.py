from quiz_loader import QuizLoader
from quiz import Quiz

if __name__ == '__main__':
    FILE_PATH = '../question bank/python.csv'  # Ensure correct CSV file path
    questions = QuizLoader.load_questions(FILE_PATH)

    if questions:
        quiz = Quiz(questions, time_limit=10)
        quiz.conduct()
    else:
        print('No loaded questions!')