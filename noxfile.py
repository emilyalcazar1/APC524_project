import nox

@nox.session
def tests(session: nox.Session) -> None:
    session.install(".[test]")
    session.run('pytest')
