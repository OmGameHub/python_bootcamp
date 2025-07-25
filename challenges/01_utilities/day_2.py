"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

import textwrap

def generate_bio(style, name, profession, passion, emoji, website):
    if style == "1":
        return f"{emoji} {name} | {profession}\n💡 {passion}\n🔗 {website}"
    elif style == "2":
        return f"{emoji} {name}\n{profession}🔥\n{passion}\n{website}🔥"
    elif style == "3":
        return f"{emoji * 3}\n{name} - {profession}\n{passion}\n{website}\n{emoji * 3}"

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion or goal in one-liner: ").strip()
emoji = input("Enter your favorite emoji (optional): ").split()
website = input("Enter your website or handle (optional): ").strip()

print("\n")
print("Choose your style: ")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")

style = input("Enter 1, 2 or 3: ").strip()
while style not in ["1", "2", "3"]:
    print("Invalid choice. Please select 1, 2, or 3.")
    style = input("Enter 1, 2 or 3: ").strip()

bio = generate_bio(style, name, profession, passion, emoji, website)

print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save_choice = input("Do you want to save this bio to a .txt file? (yes/no): ").strip().lower()
if save_choice == 'yes' or save_choice == 'y':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w") as file:
        file.write(bio)
    print(f"Bio saved to {filename}")

