from __future__ import with_statement
from fabric.api import task, prefix, env, local

env.shell = '/bin/bash -l -c'

###### Local Tasks

@task
def runserver(port=3333):
    with prefix('. .env/bin/activate'):
        ip = local("""ip addr list eth0 |grep "inet " |cut -d' ' -f6|cut -d/ -f1""", capture=True)
        local('django_ett/manage.py runserver %s:%s' % (ip, port), capture=False)

@task
def test():
    with prefix('. .env/bin/activate'):
        local('django_ett/manage.py test --noinput --failfast')


