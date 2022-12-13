import nox

@nox.session
def tests(session: nox.Session) -> None:
    session.install(".[test]")
    test_files = ['tests/test_3Dgrid.py','tests/test_pg.py']
    session.run('pytest', *test_files)
