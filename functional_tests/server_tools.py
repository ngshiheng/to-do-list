from fabric.api import run
from fabric.context_managers import settings, shell_env


def _get_manage_dot_py(host):
    return f'/home/ubuntu/to-do-list/venv-to-do-list/bin/python ~/to-do-list/manage.py'


def reset_database(host):
    host = 'ubuntu'
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'ubuntu@ip-172-31-18-227'):
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host):
    env_lines = run(f'cat ~/to-do-list/.env').splitlines()
    return dict(l.split('=') for l in env_lines if l)


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'ubuntu@ip-172-31-18-227'):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')
            return session_key.strip()
