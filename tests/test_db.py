from sqlalchemy import select

from fastapi_project.models import User


def test_create_user(session):
    user = User(
        username='alsombra',
        email='alsombra@gmail.com',
        password='minha-senha-segura',
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'alsombra@gmail.com')
    )
    assert result.username == 'alsombra'
    assert result.id == 1
