from quiz_loader import QuizLoader
from quiz import Quiz
import os

def get_subject_choice():
    """Get user's subject choice with proper validation"""
    subjects = {
        1: ("Python", "../question bank/python.csv"),
        2: ("Science and Engineering", "../question bank/science.csv")  # Fixed incomplete path
    }
    
    print('=== Welcome to the Quiz Application ===')
    print('Choose the subject:')
    for key, (name, _) in subjects.items():
        print(f'{key}. {name}')
    
    while True:
        try:
            choice = int(input('Enter the subject number to conduct test: '))
            if choice in subjects:
                subject_name, file_path = subjects[choice]
                print(f'You selected: {subject_name}')
                return file_path
            else:
                print(f'Please enter a valid choice (1-{len(subjects)})')
        except ValueError:
            print('Please enter a number, not text!')
        except KeyboardInterrupt:
            print('\nExiting application...')
            exit(0)

def validate_file_path(file_path):
    """Validate if the CSV file exists and is readable"""
    if not os.path.exists(file_path):
        print(f'Error: File not found at {file_path}')
        return False
    
    if not os.access(file_path, os.R_OK):
        print(f'Error: Cannot read file at {file_path}')
        return False
    
    return True

def main():
    try:
        # Get subject choice
        file_path = get_subject_choice()
        
        # Validate file exists
        if not validate_file_path(file_path):
            print('Please check the file path and try again.')
            return
        
        # Load questions
        print('Loading questions...')
        questions = QuizLoader.load_questions(file_path)
        
        if not questions:
            print('No questions were loaded! Please check the CSV file format.')
            return
        
        print(f'Successfully loaded {len(questions)} questions.')
        
        # Start quiz with configurable time limit
        while True:
            try:
                time_limit = int(input('Enter time limit per question in seconds (10-60): '))
                if 10 <= time_limit <= 60:
                    break
                else:
                    print('Time limit must be between 10 and 60 seconds.')
            except ValueError:
                print('Please enter a valid number!')
        
        quiz = Quiz(questions, time_limit=time_limit)
        quiz.conduct()
        
    except KeyboardInterrupt:
        print('\n\nQuiz application terminated by user.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        print('Please contact support if this issue persists.')

if __name__ == '__main__':
    main()
