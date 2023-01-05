from app.main import bp
from app.utils.api import download_file
from app.store.postgres import index_files

@bp.route('/')
def index():
    return 'This is The Main Blueprint'


@bp.route('/download')
def download():
    return download_file()


@bp.route('/store')
def store():
    return index_files()