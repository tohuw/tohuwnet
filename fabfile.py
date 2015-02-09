from fabric.api import *
import fabric.contrib.project as project
import os
import sys

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path
env.listen_port = 8000

# Remote server configuration
production = 'tohuw@tohuw.net:22'
dest_path = '/srv/www/tohuwnet'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

# def serve():
#     os.chdir(env.deploy_path)

#     PORT = 8000
#     class AddressReuseTCPServer(SocketServer.TCPServer):
#         allow_reuse_address = True

#     server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

#     sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
#     server.serve_forever()

def serve():
    local('cd {deploy_path} && python ../fake_server.py {listen_port}'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )
