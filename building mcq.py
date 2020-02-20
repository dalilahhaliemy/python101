from Question import Question

question_prompts = [                                                         # Defining list of question
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",     # Q1
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",        # Q2
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"        # Q3
]

questions = [                                # Defining list of question with correct answer
    Question(question_prompts[0], "a"),     # Input the question prompt and the answer respectively in a list
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# Now ask the questions


def run_test(questions):         # parameter of the lists of questions (the variable)

    score = 0                    # as usual set an empty variable to tell user their score at the end
    for question in questions:   # for each question object in the question list
        answer = input(question.prompt)      # store values of the answer
        if answer == question.answer:        # check if the answer given is correct
            score += 1                       # if true, add a score
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")


run_test(questions)
