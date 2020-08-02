import os, yaml
# ruamel.yaml
from yamlinclude import YamlIncludeConstructor as ymlconstructor

class yamlloader():
    def __init__(self, DirPath):
        # yaml = ruamel.yaml.YAML()
        self.dir_path = DirPath
        self.datafile = dict()
        ymlconstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=str(self.dir_path))

    def open(self, File, Mode='r'):
        # self.rawfile = open(os.path.join(self.dir_path+'/'+File), Mode)
        return open(os.path.join(self.dir_path+'/'+File), Mode, encoding='utf8')
        # return self.rawfile

    def load(self, Stream):
        self.datafile = yaml.load(Stream, Loader=yaml.FullLoader)
        return self.datafile
        # print(yaml.dump(self.datafile, default_flow_style=FlowStyle))
    def human(self, FlowStyle=False):
        return yaml.dump(self.datafile, default_flow_style=FlowStyle)

    def append(self, Stream, FlowStyle=False, AllowUnicode=True, **KeysValues):
        print(KeysValues)
        for data in self.datafile:
            print(data)
            # if data[]
            # yaml.dump(KeysValues, Stream, default_flow_style = FlowStyle, allow_unicode = AllowUnicode)
        # # print(KeysValues)
        # for key,value in KeysValues.items() :
        #     for datakey in self.datafile :
        #         if self.datafile[datakey] == key :
        #             yaml.dump(self.datafile[datakey], value)
        #         else:
        #             next

    def close(self):
        self.rawfile.close()
