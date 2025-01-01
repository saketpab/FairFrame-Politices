
#testing the google api

import google.generativeai as genai

def test_google_api():

    genai.configure(api_key="AIzaSyCdo42_6KDtvGVqTSnGo3Hblcf9dHnvsdg")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        "I am going to give you an article title. Based on that classify it as one "
        "of the following DO NOT SAY ANYTHING ELSE(only say the classification nothing else): Pro-Democrat, Pro-Republican, Anti-Democrat, Anti-Republican, Neutral"
        "Title: Another Democratic state lawmaker in Florida is joining the Republican party"
        )
    #use the conten section for more accuarcty 
    print(response.text)

if __name__ == "__main__":
    test_google_api()