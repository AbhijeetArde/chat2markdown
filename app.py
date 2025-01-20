from flask import Flask, request, render_template_string
import markdown

app = Flask(__name__)

# HTML templates as string (for single file application)
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat to Markdown</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
        main {
            padding: 20px;
        }
        h1 {
            font-size: 36px;
            margin-bottom: 20px;
        }
        textarea {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Chat to Markdown Converter</h1>
    </header>
    <main>
        <div class="container">
            <form action="/convert" method="POST">
                <textarea name="chat_input" rows="6" placeholder="Enter your chat message here"></textarea><br><br>
                <button type="submit">Convert to Markdown</button>
            </form>
        </div>
    </main>
</body>
</html>
"""

result_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Markdown</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
        main {
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
        h1 {
            font-size: 36px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-size: 16px;
            border: 1px solid #ddd;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f9f9f9;
        }
        .copy-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 20px;
        }
        .copy-btn:hover {
            background-color: #45a049;
        }
        .copy-btn:active {
            background-color: #388e3c;
        }
        a {
            color: #4CAF50;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>Converted Markdown</h1>
    </header>
    <main>
        <div class="container">
            <h3>Markdown Output:</h3>
            <div id="markdown-output">{{ md_output | safe }}</div>
            <button class="copy-btn" onclick="copyToClipboard()">Copy to Clipboard</button>
            <br><br>
            <a href="/">Go Back</a>
        </div>
    </main>
    <script>
        function copyToClipboard() {
            var copyText = document.getElementById("markdown-output");
            var range = document.createRange();
            range.selectNode(copyText);
            window.getSelection().removeAllRanges();
            window.getSelection().addRange(range);
            document.execCommand("copy");
            alert("Copied to clipboard!");
        }
    </script>
</body>
</html>
"""

# Route for the home page
@app.route('/')
def index():
    return render_template_string(index_html)

# Route to handle the form submission
@app.route('/convert', methods=['POST'])
def convert_to_markdown():
    chat_input = request.form['chat_input']
    
    # Convert chat input to markdown
    md_output = markdown.markdown(chat_input, extensions=['markdown.extensions.tables'])
    
    # Render the result with the safe HTML output
    return render_template_string(result_html, md_output=md_output)

if __name__ == '__main__':
    app.run(debug=True)
