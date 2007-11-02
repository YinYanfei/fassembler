import os
from fassembler.project import Project
from fassembler import tasks

class ToppProject(Project):
    """
    Create the basic layout used at TOPP for a set of applications.
    """
    name = 'topp'
    project_base_dir = os.path.join(os.path.dirname(__file__), 'topp-files')

    setting_defaults = dict(
        etc_svn_repository='http://svn.openplans.org/svn/config/',
        ## FIXME: make this properly settable:
        #etc_svn_repository='file:///home/ianb/src/fassembler/repo',
        etc_svn_subdir='{{env.hostname}}-{{os.path.basename(env.base_path)}}',
        )

    actions = [
        tasks.CopyDir('create layout', project_base_dir, './'),
        tasks.SvnCheckout('check out etc/', '{{config.etc_svn_subdir}}',
                          'etc/',
                          base_repository='{{config.etc_svn_repository}}',
                          create_if_necessary=True),
        ]

