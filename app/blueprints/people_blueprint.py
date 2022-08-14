from flask import Blueprint, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

from app.adapters.repository import people_repo

people_blueprint = Blueprint('people_blueprint', __name__)


@people_blueprint.route('/')
def home():
    return render_template('home.html')


@people_blueprint.route('/people')
def list_people():
    return render_template('people_list.html', people=people_repo)


@people_blueprint.route('/people/<int:person_id>')
def person_view(person_id):
    for person in people_repo:
        if person.id == person_id:
            return render_template(
                'people_view.html',
                img_url=person.url,
                firstname=person.firstname,
                lastname=person.lastname,
            )
    return render_template('404.html')


@people_blueprint.route('/find', methods=['GET', 'POST'])
def find_person():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(
            url_for('people_blueprint.person_view', person_id=form.id.data)
        )
    else:
        return render_template(
            'people_search.html',
            form=form,
            handler_url=url_for('people_blueprint.find_person')
        )


class SearchForm(FlaskForm):
    id = IntegerField("No. of the prime minister", [DataRequired()])
    submit = SubmitField("Search")
