from flask import Flask, request, render_template, redirect, flash, session, g

app = Flask(__name__)


@app.route('/')
def show_accueil():
    return render_template('layout.html')



if __name__ == '__main__':
    app.run()
