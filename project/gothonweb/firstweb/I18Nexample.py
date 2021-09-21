from flask import Flask, render_template, request, flash
from I18NQA import I18NForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/I18NHtml', methods=['GET', 'POST'])
def I18NHtml():
    form = I18NForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('I18NHtml.html', form=form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('I18NHtml.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)