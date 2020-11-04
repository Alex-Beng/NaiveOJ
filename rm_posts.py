from app import app, db
from app.models import Post

t = Post.query.all()
[db.session.delete(tt) for tt in t]
db.session.commit()