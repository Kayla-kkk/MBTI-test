personality_type = {
    "EI": ("E","I"),
    "SN": ("S","N"),
    "TF": ("T","F"),
    "JP": ("J","P")
}
def create_question():
    questions = [
        {
            "q": "1. You're a person who makes a lot of friends.",
            "personality": "EI",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "2. In your free time, you prefer to hang out with friends rather than stay at home.",
            "personality": "EI",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "3. You will feel lonely when alone.",
            "personality": "EI",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "4. After participating in the party or communicating with people, you will be full of energy.",
            "personality": "EI",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "5. You enjoy being the focus of the public.",
            "personality": "EI",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "6. You prefer to focus on the facts and details rather than on concepts and theories.",
            "personality": "SN",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "7. You tend to focus on abstract theories and ideas rather than concrete facts in reality.",
            "personality": "SN",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "8. You are used to sensing your surroundings with your five senses, and you believe in what you can see, hear, and touch.",
            "personality": "SN",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "9. You like to think about future possibilities and new ideas, rather than focusing on the present reality.",
            "personality": "SN",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "10. You like to work in a variety of ways.",
            "personality": "SN",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "11. You are more concerned with the feelings and needs of others than with pure rational analysis.",
            "personality": "TF",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "12. When you express your opinions, you prefer to be frank rather than tactful and subtle.",
            "personality": "TF",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "13. You prefer to express care and thoughtfulness in the relationship, rather than focusing on facts and efficiency.",
            "personality": "TF",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "14. You think empathy and understanding of other people's emotions are an integral part of decision-making.",
            "personality": "TF",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "15. You believe that maintaining harmony is more important than fairness and reasonableness.",
            "personality": "TF",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "16. You prefer to take things as they come rather than plan your daily activities in advance.",
            "personality": "JP",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "17. You tend to maintaining a casual and open-minded attitude rather than organize your work and life in an organized way.",
            "personality": "JP",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "18. You prefer to thinking while doing it rather than sort out your ideas before you start doing things.",
            "personality": "JP",
            "answer": [
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "19. You generally prefer to hesitate or procrastinate rather than make decisions ahead of time.",
            "personality": "JP",
            "answer":[
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
         {
            "q": "20. You don't like stable arrangements.",
            "personality": "JP",
            "answer":[
                ("Absolutely Not", 1),
                ("Basically Not", 2),
                ("Not Sure", 3),
                ("Sometimes", 4),
                ("Yes", 5)
            ],
        },
    ]
    return questions
