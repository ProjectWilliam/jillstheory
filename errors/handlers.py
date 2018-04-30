from app.errors import bp

@bp.app_errorhandler(404)
def not_found(error):
    return '<h1> Future custom error page </h1>', 404

