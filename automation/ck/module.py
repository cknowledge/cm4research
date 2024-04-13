import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          automation (str): automation as CM string object

          parsed_automation (list): prepared in CM CLI or CM access function
                                    [ (automation alias, automation UID) ] or
                                    [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

          (artifact) (str): artifact as CM string object

          (parsed_artifact) (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}

    ############################################################
    def add(self, i):
        """
        Add CM script

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (tags) (str): tags to find an CM script (CM artifact)

          (script_name) (str): name of script (it will be copied to the new entry and added to the meta)

          (tags) (string or list): tags to be added to meta

          (new_tags) (string or list): new tags to be added to meta (the same as tags)

          (json) (bool): if True, record JSON meta instead of YAML

          (meta) (dict): preloaded meta

          (template) (string): template to use (python)
          (python) (bool): template=python
          (pytorch) (bool): template=pytorch
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        import shutil
        import copy

        console = i.get('out') == 'con'

        parsed_automation_obj = i.get('parsed_automation',[])[0]
        parsed_artifact = i.get('parsed_artifact',[])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else None
        artifact_repo = parsed_artifact[1] if len(parsed_artifact)>1 else None
        
        target_repo = utils.assemble_cm_object2(artifact_repo) if artifact_repo != None else os.environ.get('CM_AUTOMATION_CK_REPO', '')

        artifact = i.get('artifact', '')
        j = artifact.find(':')
        if j>=0:
            artifact = artifact[j+1:]

        tags = i.get('tags', '')

        extra_tags = []

        r = utils.get_current_date_time({})
        if r['return']>0: return r

        iso_datetime = r['iso_datetime']
        j = iso_datetime.find('T')
        if j>0:
            iso_datetime = iso_datetime[:j].replace('-','')

        
        no_name = False
        if artifact == '':
            no_name = True

            artifact = iso_datetime

            extra_tags.append(iso_datetime)

            name = input('Input name for this Collective Knowledge or press Enter to use current date: ')

            if name !='':
                no_name = False

                name = name.strip().lower()

                artifact += '.' + name.replace(' ','-')

        if tags == '':
            tags = input('Input tags for this Collective Knowledge separate by space: ')

            tags = tags.strip().lower().replace(' ',',')

        if tags!='':
            extra_tags += tags.split(',')

        x = os.environ.get('CM_AUTOMATION_CK_EXTRA_TAGS', '')
        if x != '':
            extra_tags += x.split(',')

        if target_repo != '':
            artifact = target_repo + ':' + artifact


        # Search if exists
        ii = {'action': 'find',
              'common': True,
              'automation': utils.assemble_cm_object2(parsed_automation_obj)}

        if no_name:
            ii['tags'] = iso_datetime
            if target_repo != '':
                ii['artifact'] = target_repo+':'
        else:
            ii['artifact'] = artifact

        iii = copy.deepcopy(ii)
        
        r = self.cmind.access(ii)
        if r['return'] >0 : return r
        
        lst = r['list']

        # Create if doesn't
        paths = []

        if len(lst) > 0:
            for l in lst:
                paths.append(l.path)
        else:
            ii = copy.deepcopy(iii)
            
            ii['action'] = 'add'
            ii['yaml'] = True
            ii['meta'] = {'tags': extra_tags, 'license':''}

            r = self.cmind.access(ii)
            if r['return'] >0 : return r

            paths = [r['path']]

        # Found paths
        print ('')
        print ('Found Collective Knowledge:')
        print ('')
        for p in paths:
            print (p)

            readme = os.path.join(p, 'README.md')

            if not os.path.isfile(readme):
                with open (readme, 'w') as f:
                    f.write('\n')
                     

        # Opening CMD
        for p in paths:
            cmd = os.environ.get('CM_AUTOMATION_CK_CMD', '')
            if cmd == '': cmd = 'cd {PATH} ; bash'

            cmd = cmd.replace('{PATH}', p)

            os.system(cmd)
 
        
        
        
        return {'return':0}
