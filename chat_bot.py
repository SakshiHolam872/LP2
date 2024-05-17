import random 
class ElementaryChatbot: 
    def __init__(self): 
        self.greetings = ["Hello!", "Hi there!", "Greetings!"] 
        self.goodbyes = ["Goodbye!", "See you later!", "Bye!"] 
        self.responses = { 
            "how are you": ["I'm good, thank you!", "I'm doing well, how about you?"], 
            "your name": ["I'm a chatbot, you can call me Bot.", "I don't have a name, just call me Bot."],             
            "joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"], 
            "default": ["I'm not sure how to respond to that.", "Sorry, I didn't understand."]
        
        } 
    def greet(self): 
        print(random.choice(self.greetings)) 
 
    def respond(self, user_input): 
        user_input_lower = user_input.lower() 
 
        for key, value in self.responses.items(): 
            # print(user_input_lower) 
            if key in user_input_lower: 
                return random.choice(value) 
 
        return random.choice(self.responses["default"]) 
 
    def say_goodbye(self): 
        print(random.choice(self.goodbyes)) 
    def chat(self): 
        self.greet() 
 
         
        while True: 
            user_input = input("You: ") 
             
            if user_input.lower() == "exit": 
                self.say_goodbye() 
                break 
             
            response = self.respond(user_input) 
            print(f"Bot: {response}") 
 
if __name__ == "__main__": 
    bot = ElementaryChatbot() 
    bot.chat()