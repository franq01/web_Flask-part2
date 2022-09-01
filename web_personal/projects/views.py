################# Import de Flask #####################
from flask import render_template, request, Blueprint

project_blueprint = Blueprint('project', __name__)

########################### TODO: List project ##################


@project_blueprint.route('/')
def list():
    return render_template('project/list.html')


########################### TODO: Show project ##################
@project_blueprint.route('/<project_id>')
def show(project_id):
    return render_template('project/show.html', project_id=project_id)


########################### TODO: create a project ##################
@project_blueprint.route('/new')
def new():
    return render_template('project/new.htm')

########################### TODO: update a project ##################



########################### TODO: delete project ##################



