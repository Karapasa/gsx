from app import create_app, db
from app.models import Owner, Post, Indicator

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Owner': Owner, 'Post': Post, 'Indicator': Indicator}


if __name__ == '__main__':
    app.run()
