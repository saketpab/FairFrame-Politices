
#testing the google api

import google.generativeai as genai


def test_google_api():

    genai.configure(api_key="AIzaSyCdo42_6KDtvGVqTSnGo3Hblcf9dHnvsdg")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        "I am going to give you an article title. Based on that classify it as one "
        "of the following and map your answer to one of the integers given. DO NOT SAY AN OPTION UNLESS IT IS STATED HERE (only say the classification as an integer nothing else): "
        "Pro-Democrat: 1, Pro-Republican: 2, Anti-Democrat: 3, Anti-Republican: 4, Neutral: 5"
        "Title: Another Democratic state lawmaker in Florida is joining the Republican party"
        )
    #use the conten section for more accuarcty 
    print(response.text)

if __name__ == "__main__":
    test_google_api()