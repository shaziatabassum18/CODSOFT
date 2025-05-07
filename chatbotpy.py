import urllib.parse
import datetime

def chatbot():
    print("🤖: Hi! I'm Chitti, your rule-based chatbot buddy. Type 'bye' anytime to exit.")

    while True:
        user_input = input("You: ").lower()

        # Rule-based responses
        if "hello" in user_input or "hi" in user_input:
            print("🤖: Hello there! How can I assist you today?")
        elif "how are you" in user_input:
            print("🤖: I'm just a bunch of code, but I'm functioning perfectly! 😄")
        elif "your name" in user_input:
            print("🤖: I'm Chitti, the robot 🤖. Just a simple chatbot with some rules!")
        elif "who created you" in user_input:
            print("🤖: A brilliant AIML student named Shazia built me! 👩‍💻✨")
        elif "what can you do" in user_input:
            print("🤖: I can answer basic questions, chat a little, and even guide you online! 🌐")
        elif "what is ai" in user_input:
            print("🤖: AI means Artificial Intelligence — machines that think smart like you! 🧠")
        elif "i am sad" in user_input:
            print("🤖: Oh no! Virtual hugs for you 🤗 You're stronger than your bugs.")
        elif "what's the time" in user_input:
            now = datetime.datetime.now()
            print(f"🤖: It's currently {now.strftime('%H:%M')} 🕒")
        elif "thank you" in user_input or "thanks" in user_input:
            print("🤖: You're welcome! I'm here for you 😇")
        elif "tell me a joke" in user_input:
            print("🤖: Why don't programmers like nature? It has too many bugs! 🐛😂")
        elif "what is your purpose" in user_input:
            print("🤖: To chat with awesome people like you and pass my project with flying colors! 🎯")
        elif "are you real" in user_input:
            print("🤖: I’m real in your terminal, and that’s all that matters 😉")
        elif "who is your favorite actor" in user_input:
            print("🤖: Rajinikanth, of course! Even I can’t process how cool he is 😎")
        elif "are you single" in user_input:
            print("🤖: Haha, I’m in a long-term relationship with Python 😜")
        elif "can you help me" in user_input:
            print("🤖: Of course! Ask me anything you’d like.")
        elif "what's your favorite food" in user_input:
            print("🤖: I feed on binary snacks... 101010 yum!")
        elif "sing a song" in user_input:
            print("🤖: Twinkle twinkle little bot, processing your every thought 🎶")
        elif "tell me a fun fact" in user_input:
            print("🤖: Fun fact! A group of flamingos is called a 'flamboyance'. Fancy, right? 😍")
        elif "where do you live" in user_input:
            print("🤖: I live in your code... rent-free! 😏")
        elif "bye" in user_input or "exit" in user_input:
            print("🤖: Alvida! Take care and keep coding! 👋")
            break
            
        # If the chatbot doesn't understand, suggest Google & YouTube
        else:
            encoded_query = urllib.parse.quote(user_input)
            google_url = f"https://www.google.com/search?q={encoded_query}"
            youtube_url = f"https://www.youtube.com/results?search_query={encoded_query}"

            print("🤖: Hmm... I’m not sure, but maybe this will help:")
            print(f"🔍 Google it: {google_url}")
            print(f"📺 Watch on YouTube: {youtube_url}")

# Call the function to start chatbot
chatbot()
