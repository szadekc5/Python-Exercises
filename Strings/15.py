#Write a Python function to create an HTML string with tags around the word(s).
def add_html_tags(text, tag):
    return f"<{tag}>{text}</{tag}>"

word = "merito"
tag = "h1"
html_string = add_html_tags(word, tag)
print(html_string)
