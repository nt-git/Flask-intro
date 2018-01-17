"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
    <body>
    <a href='http://localhost:5000/hello'>Hi! This is the home page.</a>
    </body>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Choose your compliment:<br>
          <input type="radio" value='awesome' name="compliment">Awesome
          <input type="radio" value='terrific' name="compliment">Terrific
          <input type="radio" value = 'fantastic' name="compliment">Fantastic<br>
          <input type="radio" value='neato' name="compliment">Neato
          <input type="radio" value='fantabulous' name="compliment">fantabulous
          <input type="radio" value='wowza' name="compliment">wowza<br>
          <input type="radio" value='oh-so-not-meh' name="compliment">oh-so-not-meh
          <input type="radio" value="brilliant" name="compliment">brilliant
          <input type="radio" value="ducky" name="compliment">ducky<br>
          <input type="radio" value='coolio' name="compliment">coolio
          <input type="radio" value='incredible' name="compliment">incredible<br>
          <input type="radio" value='wonderful' name="compliment">wonderful
          <input type="radio" value='smashing' name="compliment">smashing
          <input type="radio" value='lovely' name="compliment">lovely<br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    print request.args

    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
