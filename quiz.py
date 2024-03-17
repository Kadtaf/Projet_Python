questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "options": {
            "a": "Marseille",
            "b": "Nice",
            "c": "Paris",
            "d": "Nantes"
        },
        "correct_answer": "c"
    },
    {
        "question": "Quel est le plus grand océan du monde ?",
        "options": {
            "a": "Océan Atlantique",
            "b": "Océan Arctique",
            "c": "Océan Indien",
            "d": "Océan Pacifique"
        },
        "correct_answer": "d"
    },
    {
        "question": "Qui a peint la Joconde ?",
        "options": {
            "a": "Pablo Picasso",
            "b": "Vincent van Gogh",
            "c": "Leonardo da Vinci",
            "d": "Michel-Ange"
        },
        "correct_answer": "c"
    },
    {
        "question": "Quelle est la planète la plus proche du soleil ?",
        "options": {
            "a": "Vénus",
            "b": "Mercure",
            "c": "Mars",
            "d": "Jupiter"
        },
        "correct_answer": "b"
    }
]


def display_question(question):
    print(question["question"])
    for option, value in question["options"].items():
        print(f"{option} => {value}")
    response_user = input("Votre réponse : ").lower()
    return response_user


def verify_response(question, response):
    if response in question["options"]:
        if response == question["correct_answer"]:
            print("Bonne réponse!\n")
            return True
        else:
            print("Mauvaise réponse.\n")
            return False
    else:
        print("Choix invalide.\n")
        return False


score = 0

print("Bienvenue au questionnaire !\n")

for q in questions:
    reponse_utilisateur = display_question(q)
    if verify_response(q, reponse_utilisateur):
        score += 1

print(f"Votre score final est de {score}/{len(questions)}")
