from app.main import bp
from app.utils.api import download_file

@bp.route('/')
def index():
    return 'This is The Main Blueprint'


@bp.route('/download')
def download():
    return download_file()