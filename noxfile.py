import nox

@nox.session
def tests(session: nox.Session) -> None:
    session.install("-r","test_3Dgrid.py")
    session.run('pytest')
