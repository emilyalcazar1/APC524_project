import nox

@nox.session
def tests(session: nox.Session) -> None:
    session.install("pytest")
    session.install("matplotlib")
    session.run("pytest",*session.posargs)
