from flask import Blueprint, render_template

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


@people_blueprint.route('/find')
def find_person():
    return 'TODO: Placeholder'
