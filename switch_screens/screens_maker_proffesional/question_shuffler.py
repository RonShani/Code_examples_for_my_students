import random
class QuestionShuffler():

    def __init__(self):
        f = open("questions_file.txt", "r")
        q_str = f.read()
        self.q_str = q_str.split(",|,")
        random.shuffle(self.q_str)
        f.close()

    def get_questions(self):
        q_formatted = self.q_str.pop(0).split(",")
        for q in range(len(q_formatted)):
            q_formatted[q] = q_formatted[q][::-1]
        return q_formatted
