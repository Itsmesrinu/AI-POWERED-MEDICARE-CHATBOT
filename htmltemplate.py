import streamlit as st

# CSS for chat messages
css = '''
<style>
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
}
.chat-message.user {
    background-color: #2b313e; /* Dark background for user */
    color: white; /* Text color for user */
}
.chat-message.bot {
    background-color: #475063; /* Dark background for bot */
    color: white; /* Text color for bot */
}
.chat-message .avatar {
    width: 20%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
}
.light-theme .chat-message.user {
    background-color: #e0e0e0; /* Light background for user */
    color: black; /* Text color for user */
}
.light-theme .chat-message.bot {
    background-color: #f0f0f0; /* Light background for bot */
    color: black; /* Text color for bot */
}
</style>
'''

# Bot and User message templates
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-2.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

def display_chat(messages):
    for message in messages:
        if message['role'] == 'user':
            st.markdown(user_template.replace("{{MSG}}", message['content']), unsafe_allow_html=True)
        elif message['role'] == 'bot':
            st.markdown(bot_template.replace("{{MSG}}", message['content']), unsafe_allow_html=True)

def main():
    st.title("Chat with Medicare AI")
    st.markdown(css, unsafe_allow_html=True)

    messages = []  # List to hold chat messages

    # Input field for user messages
    user_input = st.text_input("You: ")
    
    if st.button("Send"):
        if user_input:
            messages.append({'role': 'user', 'content': user_input})
            # Simulate a bot response (replace this with actual bot logic)
            bot_response = "This is a response from the bot."  # Placeholder response
            messages.append({'role': 'bot', 'content': bot_response})

    # Display chat messages
    display_chat(messages)

if __name__ == "__main__":
    main()
