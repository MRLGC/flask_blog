from flask_script import Manager, Server
from app import app
from models import tags, topic, users, db
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
manage = Manager(app)
migrate = Migrate(app=app, db=db)
manage.add_command('db', MigrateCommand)
@manage.shell
def flask_context_shell():
    shell_opt = dict(
        app=app,
        db=db,
        tags=tags.Tags,
        topics=topic.Topics,
        users=users.Users,
    )
    return shell_opt

if __name__ == '__main__':
    manage.run()
