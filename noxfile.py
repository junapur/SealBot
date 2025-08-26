import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "type_check"]


@nox.session(venv_backend="none")
def lint(session: nox.Session) -> None:
    session.run("ruff", "format", "--check")
    session.run("ruff", "check", "--no-fix")


@nox.session(venv_backend="none")
def tidy(session: nox.Session) -> None:
    session.run("ruff", "format")
    session.run("ruff", "check", "--fix")


@nox.session(venv_backend="none")
def type_check(session: nox.Session) -> None:
    session.run("pyright")
