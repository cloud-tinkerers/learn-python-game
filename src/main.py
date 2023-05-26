from browser import document, alert

def hello(event):
    alert("Hello, Python Puzzle Quest!")

document["mybutton"].bind("click", hello)