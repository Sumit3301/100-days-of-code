question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question():

    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer



class QuizBrain:
    def __init__(self,q_list):
        self.q_number=0
        self.question_list=q_list
        
def still_has_questions(self):
    if(self.question_number<len(self.question_list)):
        return True
    else:
        return False


def next_question(self):
    current_question=self.question_list[self.question_number]
    self.question_number+=1
    input(f'{self.question_number}:{self.question_text}')
