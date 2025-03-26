from bs4 import BeautifulSoup

def remove_span_tags(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove <span> tags but keep their content
    for span in soup.find_all("span"):
        span.unwrap()

    return soup.prettify()

def main():
    print("Paste your HTML code below. Press Enter, then Ctrl+D (or Ctrl+Z on Windows) to finish:")
    
    # Read multiline input from the user
    html_content = ""
    while True:
        try:
            line = input()
            html_content += line + "\n"
        except EOFError:  # End input with Ctrl+D (Linux/macOS) or Ctrl+Z (Windows)
            break

    # Process HTML
    updated_html = remove_span_tags(html_content)

    # Output result
    print("\nUpdated HTML:\n")
    print(updated_html)

if __name__ == "__main__":
    main()
