import nox

@nox.session
def tests(session: nox.Session) -> None:
    session.install("-r","tests/test_3Dgrid.py")
    session.run('pytest')
