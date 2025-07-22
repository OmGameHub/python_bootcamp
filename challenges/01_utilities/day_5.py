"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

# Emoji Dictionary
emoji_map = {
    "happy": "😊",
    "love": "❤️",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

message = input("Enter your message: ")

updated_words = []
for word in message.split():
    # Remove punctuation from the word for matching
    clean_word = word.lower().strip(",.!?;:")

    # Check if the cleaned word is in the emoji map (case-insensitive)
    if clean_word in emoji_map:
        # Add the emoji after the word
        updated_words.append(f"{word} {emoji_map[clean_word]}")
    else:
        updated_words.append(word)

print(" ".join(updated_words))