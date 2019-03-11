from flask import (
    Blueprint,
    jsonify,
    redirect,
    request,
    # flash,
    url_for,
    make_response,
    render_template
    )
# from flask_login import login_required, current_user
from bookmark_app.extensions import db
import models
from extractor import extract


news = Blueprint('news', __name__,
                 template_folder='templates')


@news.route('/')
def index():
    """
    Render Forms for user input.
    :return: Flask response
    """
    # These following lines initialize all dbs.
    # db.configure_mappers()
    # db.drop_all()
    # db.create_all()

    things = models.Page.query.filter()
    return render_template('news/app.html', things=things)


@news.route('/extract')
def extract_url():
    """
    Extract data from url provided by user.
    # :return: JSON
    :return: redirect
    """
    url = request.args.get('url', '')
    if not url:
        return jsonify(
            type='error', result='Provide a URL'
        ), 406
    save_url(url)
    # return jsonify(type='success')
    return redirect(url_for('news.index'))


@news.route('/search')
def search():
    """
    Use search terms to query database.
    :return: Something
    """
    search = request.args.get('terms', '')
    things = models.Page.query.search(search).all()
    print('------------------------------')
    return render_template('news/app.html', things=things)


def save_url(url):
    """
    helper function that allows extract_url() to save data
    to a database
    ":return: None"
    """
    page = extract(url)
    try:
        current = models.Page(
            title=page['title'],
            text=page['text'],
            html=page['html'],
            url=url
        )

        db.session.add(current)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

    return None


@news.route('/download/<int:page_id>')
def download(page_id):
    """
    Retrieve the html saved from a webpage added to database and display
    it in a browser.

    :param page_id: Id of page from database to retrieve.
    :type page_id: int
    :return: Flask response object
    """
    page = models.Page.query.filter(models.Page.id == page_id).one()
    response = make_response(page.html)
    response.headers['Content-Disposition'] = 'attachment filename=page.html'

    return response
