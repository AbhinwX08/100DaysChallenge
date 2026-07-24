from Question_Model import Question
from Question_set import Question_Bank
from Quiz_brain import QuizBrain

Extracted_question= []
for item in Question_Bank:
    q_test= item['test']
    q_answer= item['answer']

    new_question = Question(q_test,q_answer)
    Extracted_question.append(new_question)

quiz= QuizBrain(Extracted_question)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.q_no} ")