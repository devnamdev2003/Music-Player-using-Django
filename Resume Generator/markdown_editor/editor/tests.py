import markdown
import webbrowser

# Your Markdown code
markdown_code = """
# Example Markdown

This is a **sample** *Markdown* code.
"""

# Convert Markdown to HTML
html_code = markdown.markdown(markdown_code)
print(html_code)

# Save HTML to a file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_code)

# Open the HTML file in a web browser
webbrowser.open("output.html")
