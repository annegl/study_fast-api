from dataclasses import asdict
from sqlalchemy import select
from src.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        try:
            new_user = User(
                username='alice', password='test123', email='alice@example.com'
            )
            session.add(new_user)
            session.commit()

            user = session.scalar(  # converts what's in the db into a py obj
                select(User).where(User.username == 'alice')
            )

            # breakpoint() # pp user - pretty print to see what was created
        except Exception:
            session.rollback()
            raise

    assert new_user.username == 'alice'
    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'test123',
        'email': 'alice@example.com',
        'created_at': time,
        'updated_at': time,
    }
