#Today I am learning SQLAlchemy, ORM (Oject Relational Mapping)
from sqlalchemy import Column,Integer,String,ForeignKey,Sequence,create_engine
from sqlalchemy.orm import sessionmaker,relationship,declarative_base
import sqlite3

conn = sqlite3.connect('orm.db')
cursor = conn.cursor()

engine = create_engine('sqlite:///orm.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    
    posts = relationship('Post',back_populates='user')

class Post(Base):
    __tablename__="posts"
    id = Column(Integer,primary_key=True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))
    
    user = relationship('User',back_populates='posts')

Base.metadata.create_all(engine)

user1 = User(name='Darshil',email ='darshil@gmail.com')
user2 = User(name='Kalp',email ='kalp@gmail.com')
post1 = Post(title='Darshil First Post',content='This is the content from Darshil first post',user=user1)
post2 = Post(title='Darshil Second Post',content='This is the content from Darshil second post',user=user1)
post3 = Post(title='Kalp First Post',content='This is the content from Kalp first post',user=user2)

# session.add_all([user1,user2,post1,post2,post3])
# session.commit()

posts_with_user = session.query(Post,User).join(User).all()

for post ,user in posts_with_user:
    print(f"{post.title} {user.name}")

# user = session.query(User).filter_by(name = 'Kalp').first()
# session.delete(user)
# user = session.add_all([user1,user2])
# session.commit()
cursor.execute("SELECT * FROM posts")

rows = cursor.fetchall()
for row in rows:
    print(row)
