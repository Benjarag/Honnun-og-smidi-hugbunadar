import pyfiglet
import emoji

# this is a comment
name = input("Enter your name: ")
pyfiglet.print_figlet(name)

print(emoji.emojize(":thumbsup:", use_aliases=True))