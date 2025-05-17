import csv
from question import LoadQuestion

class QuizLoader:
    @staticmethod
    def load_questions(file_path):
        questions = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)

                for rows in reader:
                    if len(rows) < 8:
                        print('Skipping an invalid row!')
                        continue

                    try:
                        question = LoadQuestion(
                            category=rows[0],
                            subcategory=rows[1],
                            question=rows[2],
                            options=rows[3:7],
                            answer=rows[7]
                        )
                        questions.append(question)
                    except ValueError:
                        print('Skipping invalid row due to incorrect data format.')

        except FileNotFoundError:
            print("Error: Couldn't find the specified file path.")
        except csv.Error as err:
            print(f'CSV error: {err}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

        return questions