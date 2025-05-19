
from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True


#render_template("t.html")
@app.route('/')
@app.route('/form')
def form():
    return render_template("t.html")
@app.route('/thanks')
def thanks():
      person = "Bob"
      action = "dancing"
      return render_template("tynote.html", name = person, verb = action)
@app.route('/results', methods=["POST"])
def results():
    color_choice = request.form['color']
    lucky_number = request.form['luck_num']
    fav_class = request.form['fav_class']
    best_pix = request.form['best_pix'].lower().strip()

    # Properly indented list of Pixar films
    films = [
        "toy story", "a bug's life", "toy story 2", "monsters, inc.",
        "finding nemo", "the incredibles", "cars", "ratatouille", "wall-e", "up",
        "toy story 3", "cars 2", "brave", "monsters university", "inside out",
        "the good dinosaur", "finding dory", "cars 3", "coco", "incredibles 2",
        "toy story 4", "onward", "soul"
    ]

    if best_pix not in films:
        best_pix = "Sorry, '{0}' isn't a Pixar film.".format(best_pix.title())
    else:
        best_pix = best_pix.title()

    return render_template('form_results.html',
                           color=color_choice,
                           lucky_number=lucky_number,
                           fav_class=fav_class,
                           best_pix=best_pix)

if __name__ == '__main__':
    app.run()

