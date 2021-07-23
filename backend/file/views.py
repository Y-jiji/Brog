from flask.blueprints import Blueprint
from flask\
    import request, session
from werkzeug.utils import secure_filename
import json
from user.models import *
import user.public
from file.public import *
import os

ALLOWED_SUFFIX = ['pdf', 'txt']

bp = Blueprint(
    name='read',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/read'
)


@bp.route('/tags/', methods=["GET", "POST"])
@user.public.login_required
def tags():
    # 未完成
    tags_ = []
    return json.dumps(tags_)


@bp.route('/upload/', methods=["POST"])
@user.public.login_required
def upload():
    for x in request.files:
        x = request.files[x]
        if x.filename.split('.')[-1] not in ALLOWED_SUFFIX:
            return json.dumps({'status': 500, 'reason': 'invalid file suffix', })
        request.files['file'].save(
            os.path.join(FILE_DIR, secure_filename(x.filename)),
            buffer_size=512
        )
    return json.dumps({'status': 200, })