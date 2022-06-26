

# ? --- symptoms --- ? #
depression_symptoms = ["discomfort", "sadness", "upset", "sleeping too much",
                       "sleeping", "suicide", "death", "die", "fatigue", "tired", "guilt"]
anxiety_symptoms = ["panic", "worry", "stress", "shortness of breath",
                    "trembling", "headache", "fatigue", "insomnia"]
sleeping_symptoms = ["memory disorder", "memory", "learning disorder",
                     "learning", "boredom", "oversleeping", "sleeping too much", "sleeping"]
mood_symptoms = ["very sad", "sad", "talking", "feeling useless", "useless",
                 "worthless", "feeling worthless", "away", "stay away", "stay away from others"]
social_anxiety_symptoms = ["fear", "avoid from people", "lovely", "alone",
                           "sweating", "nausea", "tremor", "there is no love", "not talking"]


disorders_list = [depression_symptoms, anxiety_symptoms,
                  sleeping_symptoms, mood_symptoms, social_anxiety_symptoms]

# ? --- counseling results --- ? #
counseling_results = {
    1: "Depression Disorder",
    2: "Anxiety Disorder",
    3: "Sleeping Disorder",
    4: "Mood Disorder",
    5: "Social Anxiety Disorder"
}


def TakeUserDescription():

    main_sentences = []

    print(f"Please explain about your feelings (at least 4 sentences. separated by:'. ') :")

    while(len(main_sentences) < 4):
        user_text = input()

        sentences = user_text.split(".")
        for item in sentences:
            sentences[sentences.index(item)] = item.strip()
            if(item == ""):
                sentences.remove(item)

        for sentence in sentences:
            main_sentences.append(sentence.lower())
        
        if(len(main_sentences) < 4):
            print(f"Please Explain a fwe fore details : ")


        

    if(len(sentences) >= 4):
        return main_sentences


def FindCounselingResult(sentencesList):

    word_list = []

    for sentence in sentencesList:
        for word in sentence.split():
            word_list.append(word)

    depression_words = []
    anxiety_words = []
    sleeping_words = []
    mood_words = []
    social_anxiety_words = []

    for word in word_list:
        if(word in depression_symptoms):
            depression_words.append("True")
        elif(word in anxiety_symptoms):
            anxiety_words.append("True")
        elif(word in sleeping_symptoms):
            sleeping_words.append("True")
        elif(word in mood_symptoms):
            mood_words.append("True")
        elif(word in social_anxiety_symptoms):
            social_anxiety_words.append("True")

    trues_list = [len(depression_words), len(anxiety_words), len(
        sleeping_words), len(mood_words), len(social_anxiety_words)]

    if(max(trues_list) < 4):
        print("Little information available. Explain a little more! :(")
        TakeUserDescription()
    else:
        True_count_dictionary = {
            "Depression": len(depression_words),
            "Anxiety": len(anxiety_words),
            "Sleeping": len(sleeping_words),
            "Mood": len(mood_words),
            "Social Anxiety": len(social_anxiety_words)
        }

        final_disorder = max(True_count_dictionary,
                             key=True_count_dictionary.get)
        
        return final_disorder


def PrintCounselingResult(consultationResult):
    print(f"--- Counseling Result ---\nYou have {consultationResult} Disorder.")
