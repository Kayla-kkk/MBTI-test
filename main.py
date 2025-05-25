from question import create_question, personality_type
from function import print_question, ask_question, calculate_score, mbti

def main():
    print("Welcome to the MBTI Test System!")
    last = None
    while True:
        if last:
            print(f"The last testing result is : {last['mbti']}")
        else:
            print(f"Please start the test!")
        command = input("Do you want to start the test? Yes|No|Result: ").strip().lower()
        if command == "no":
            break
        elif command == "result":
            if last:
                print(f"The last testing result is : {last['mbti']}")
            else:
                print(f"Please start the test!")
        elif command == "yes":
            questions = create_question()
            answer = []
            for i, question in enumerate(questions, 1):
                print_question(question, i)
                score = ask_question(question)
                answer.append(score)

            score_dict = calculate_score(questions, answer)
            result = mbti(score_dict)
            print(f"Your MBTI is : {result}!")
            last = {"mbti": result}
        else:
            print("Sorry! This command is not recognized!")
            
    
if __name__ == "__main__":
    main()
