from flask_script import Manager, Server
from app import app
import models
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
manage = Manager(app)
migrate = Migrate(app=app, db=models.db)
manage.add_command('db', MigrateCommand)
@manage.shell
def flask_context_shell():
    shell_opt = dict(
        app=app,
        db=models.db,
        tags=models.tags.Tags,
        topics=models.topic.Topics,
        users=models.users.Users,
    )
    return shell_opt

if __name__ == '__main__':
    manage.run()
