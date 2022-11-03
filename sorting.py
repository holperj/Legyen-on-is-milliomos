class Question:
    question: str
    a: str
    b: str
    c: str
    d: str
    right: str

question_list = []

def make_list():
    file = open('kerdesek.csv', 'r', encoding='UTF-8')
    file.readline
    for row in file:
        splitted_data = row.split(';')
        temp = Question()
        temp.question = splitted_data[0]
        temp.a = splitted_data[1]
        temp.b = splitted_data[2]
        temp.c = splitted_data[3]
        temp.d = splitted_data[4]
        # temp.right = splitted_data[5]
        question_list.append(temp)
    file.close()

make_list()

for q in question_list:
    print(f'Kérdés: {q.question}')