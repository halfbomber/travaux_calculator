import yaml, os
from yamlinclude import YamlIncludeConstructor as ymlconstructor

class yamlloader():
    def __init__(self, DirPath):
        self.dir_path = DirPath
        ymlconstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=str(self.dir_path))

    def open(self, File, Mode='r'):
        with open(os.path.join(self.dir_path+'/'+File), Mode) as stream:
            self.datafile = yaml.load(stream, Loader=yaml.FullLoader)
        return self.datafile

    def show(self, FlowStyle=False):
        print(yaml.dump(self.datafile, default_flow_style=FlowStyle))

    def append(self, **KeysValues):
        print(KeysValues)
        for key,value in KeysValues.items() :
            for datakey in self.datafile :
                if self.datafile[datakey] == key :
                    yaml.dump(self.datafile[datakey], value)
                else:
                    next
    def close(self):
        close(os.path.join(self.dir_path+'/'+File))
