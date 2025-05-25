from question import personality_type
def print_question(question, index):
    print(f"\n{question['q']}")
    for i, answer_option in enumerate(question["answer"], 1):
        text = answer_option[0]
        print(f"{i}. {text}")

def ask_question(question):
    while True:
        try:
            score = int(input("Your choice is: "))
            if 1 <= score <= 5:
                return question["answer"][score - 1][1]
            else:
                print("Wrong answer!")
        except ValueError:
            print("Please enter a valid number here!")

def calculate_score(questions, answer):
    score_dict = {}
    for dim in personality_type:
        score_dict[dim] = 0
    for i in range(len(questions)):
        dim = questions[i]["personality"]
        answer_score = answer[i]
        score_dict[dim] = score_dict[dim] + answer_score
    return score_dict

def mbti(score_dict):
    result = []
    for dim, type_4 in personality_type.items():
        type_1 = type_4[0]
        type_2 = type_4[1]
        if score_dict[dim] >= 15:
            result.append(type_1)
        else:
            result.append(type_2)
    mbti = "".join(result)
    return mbti
