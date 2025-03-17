# Simple Chatbot with Tkinter GUI

## Overview
This project implements a simple AI chatbot using Python's Tkinter library for the graphical user interface (GUI). The chatbot, named **ChatPy**, can respond to basic conversational input, remember the user's name, and display time and date-related information. It also handles a variety of predefined responses using regular expressions to match patterns in user input.

## Features:
- **User Interaction**: The chatbot engages in simple conversations, asking questions like "How are you?" or responding to queries like "What is your name?".
- **Name Memory**: ChatPy can remember the user’s name and recall it when requested.
- **Time and Date**: It can provide the current time and date.
- **Simple Responses**: It offers default responses when it doesn't understand the input.
- **Goodbye Message**: When the user says goodbye, the chatbot shows a farewell message.

## Requirements
- Python 3.x
- Libraries:
  - `tkinter` (for GUI)
  - `random` (for generating random responses)
  - `re` (for regular expression matching)
  - `time` (for time-related queries)
  - `threading` (for handling asynchronous processing of messages)
  
You can install required packages by running:

```bash
pip install -r requirements.txt
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-chatbot.git
   cd simple-chatbot
   ```
   
2. Run the chatbot application:
   ```bash
   python chatbot_gui.py
   ```

3. The application window will open with the chatbot ready to converse with you!

## Code Structure
1. **SimpleChatbot Class**:
   - Handles all chatbot functionalities like greeting the user, remembering and recalling the user's name, handling time-related queries, and providing default responses.
   - The chatbot has predefined patterns it looks for in user input and uses the `re` module to match these patterns.
   
2. **ChatbotGUI Class**:
   - Manages the GUI elements using Tkinter.
   - Displays the user and bot's messages in a scrollable chat window.
   - Handles the sending of messages and processes responses asynchronously.
   - Displays a goodbye message when the user says goodbye.

## How it Works:
1. **User Message**:
   - When the user types a message and presses Enter or clicks the "Send" button, it gets displayed in the chat history window.
   
2. **Chatbot Response**:
   - The chatbot responds to the message based on predefined patterns using regular expressions.
   - Responses may include greetings, recalling the user's name, time, or other default responses.
   
3. **Goodbye**:
   - If the user says "bye" or "goodbye", the chatbot will display a messagebox with a goodbye message and close the app after a short delay.

4. **Asynchronous Processing**:
   - The chatbot's response is processed in a separate thread, ensuring that the GUI remains responsive even while the chatbot is "thinking".

## Example Conversation
- **User**: Hi
- **ChatPy**: Hello! I'm ChatPy. How can I help you today?

- **User**: What is my name?
- **ChatPy**: I don't think you've told me your name yet.

- **User**: My name is John
- **ChatPy**: Nice to meet you, John! I'll remember your name.

- **User**: What time is it?
- **ChatPy**: The current time is 14:30.

- **User**: Goodbye
- **ChatPy**: Thank you for chatting with ChatPy!

## Future Enhancements
- **More Complex Conversations**: The chatbot could be enhanced with more advanced natural language processing (NLP) capabilities.
- **Memory Expansion**: ChatPy could be extended to remember more details about the user, such as preferences, past conversations, etc.
- **Machine Learning Integration**: Implementing a machine learning model to improve chatbot responses based on past interactions.
- **Speech Recognition**: Add voice input and output features for a more interactive experience.

