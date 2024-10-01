import pyfiglet
import emoji

name = input("Enter your name: ")

with open("data/names.txt", "a+", encoding="utf-8") as names_file:
    jazzled_name = pyfiglet.figlet_format(name)
    thumbs_up = emoji.emojize(":thumbsup:", use_aliases=True)
    names_file.write(f"{jazzled_name} {thumbs_up} {":thumbsup:"}")


# pyfiglet.print_figlet(name)

# print(emoji.emojize(":thumbsup:", use_aliases=True))