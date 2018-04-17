from flask_script import Manager, Server
from app import app
import models

manage = Manager(app)

@manage.shell
def flask_context_shell():
    shell_opt = dict(
        app=app,
        db=models.db,
        tags=models.tags.Tags,
        topics=models.topic.Topics,
    )
    return shell_opt

if __name__ == '__main__':
    manage.run()
