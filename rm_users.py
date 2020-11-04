from app import app, db
from app.models import User

t = User.query.all()
[db.session.delete(tt) for tt in t]
db.session.commit()