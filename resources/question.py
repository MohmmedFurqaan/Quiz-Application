class LoadQuestion:
    """Represents a quiz question with multiple choice options"""
    
    def __init__(self, category, subcategory, question, options, answer):
        """
        Initialize a question object
        
        Args:
            category (str): Main category of the question
            subcategory (str): Subcategory of the question
            question (str): The question text
            options (list): List of answer options
            answer (str): Correct answer (A, B, C, or D)
        """
        self.category = category.strip()
        self.subcategory = subcategory.strip()
        self.question = question.strip()
        self.options = [option.strip() for option in options if option.strip()]
        self.answer = answer.strip().upper()
        
        # Validate inputs
        self._validate_question_data()
    
    def _validate_question_data(self):
        """Validate question data integrity"""
        if not self.category:
            raise ValueError("Category cannot be empty")
        
        if not self.subcategory:
            raise ValueError("Subcategory cannot be empty")
        
        if not self.question:
            raise ValueError("Question text cannot be empty")
        
        if len(self.options) < 2:
            raise ValueError("At least 2 options are required")
        
        if len(self.options) > 4:
            raise ValueError("Maximum 4 options are allowed")
        
        # Validate answer corresponds to available options
        max_option_index = len(self.options) - 1
        if not (0 <= ord(self.answer) - ord('A') <= max_option_index):
            valid_options = [chr(65 + i) for i in range(len(self.options))]
            raise ValueError(f"Answer '{self.answer}' is not valid. Valid options: {valid_options}")
    
    def check_correct(self, user_answer):
        """
        Check if the user's answer is correct
        
        Args:
            user_answer (str): User's answer choice
            
        Returns:
            bool: True if correct, False otherwise
        """
        if not user_answer:
            return False
        
        normalized_answer = user_answer.strip().upper()
        return normalized_answer == self.answer
    
    def display_question(self, index=None):
        """
        Display the question with options
        
        Args:
            index (int, optional): Question number for display
        """
        header = f"Question {index + 1}" if index is not None else "Question"
        print(f'\n{header}: {self.question}')
        print('-' * (len(header) + len(self.question) + 2))
        
        for i, option in enumerate(self.options):
            option_letter = chr(65 + i)  # A, B, C, D
            print(f'{option_letter}. {option}')
        print()  # Empty line for better readability
    
    def get_valid_options(self):
        """Return list of valid option letters for this question"""
        return [chr(65 + i) for i in range(len(self.options))]
    
    def get_correct_option_text(self):
        """Return the text of the correct answer option"""
        correct_index = ord(self.answer) - ord('A')
        return self.options[correct_index]
    
    def get_user_answer_text(self, user_answer):
        """
        Get the text of the user's selected option
        
        Args:
            user_answer (str): User's answer choice (A, B, C, D)
            
        Returns:
            str: Text of the selected option or empty string if invalid
        """
        try:
            user_index = ord(user_answer.upper()) - ord('A')
            if 0 <= user_index < len(self.options):
                return self.options[user_index]
        except (TypeError, AttributeError):
            pass
        return ""
    
    def __str__(self):
        """String representation of the question"""
        preview = self.question[:50] + "..." if len(self.question) > 50 else self.question
        return f"Q: {preview} (Category: {self.category}/{self.subcategory})"
    
    def __repr__(self):
        """Detailed string representation for debugging"""
        return f"LoadQuestion(category='{self.category}', subcategory='{self.subcategory}', question='{self.question[:30]}...', options={len(self.options)}, answer='{self.answer}')"
