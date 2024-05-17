import java.util.Scanner; 
 class SimpleChatbot { 
    public static void main(String[] args) { 
        Scanner sc1 = new Scanner(System.in); 
        System.out.println("Chatbot: Hi! How can I help you today?"); 
        System.out.print("You: "); 
        while (true) { 
            String userInput = sc1.nextLine().toLowerCase(); 
            // Simple string matching for user input 
            if (userInput.contains("hello") || userInput.contains("hi")) { 
                System.out.println("Chatbot: Hello there!"); 
            } else if (userInput.contains("how are you")) { 
                System.out.println("Chatbot: I'm just a computer program, but thanks for asking!"); 
            } else if (userInput.contains("bye")) { 
                System.out.println("Chatbot: Goodbye! Have a great day!"); 
                break; 
            } else { 
                System.out.println("Chatbot: Sorry, I didn't understand that."); 
            } 
            System.out.print("You: "); 
        } 
        sc1.close(); 
    } 
}