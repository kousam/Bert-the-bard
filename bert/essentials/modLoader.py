
import os
import importlib.util
from importlib import reload


class ModLoader():

    def __init__(self):

        self.script_module_lib = {}
        self.script_dir = '{}\\mods\\'.format(os.getcwd())
        


    def getFiles(self, path):
        files = os.listdir(path)
        return files

    def loadMods(self):
        # old project copy paste code
        garbage_collection = [self.script_module_lib[script_name]for script_name in self.script_module_lib]
        for i in garbage_collection:
            del i
            
        self.script_module_lib = {}
        
        
        for file in self.getFiles(self.script_dir):
            script_name = file.split('.')[0] #this just takes the extension away
            try:
                if script_name not in self.script_module_lib and file.split('.')[1] == 'py':
                    path = '{}{}'.format(self.script_dir, file)
                    
                    spec = importlib.util.spec_from_file_location(file, path)
                    script_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(script_module)
                    
                    self.script_module_lib[script_name] = script_module
            except Exception as e:
                pass

    def getMods(self):
        return self.script_module_lib


