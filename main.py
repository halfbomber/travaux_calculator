#main
import yaml_loader, os

if __name__ == '__main__':
    YamlProjetPath = os.getcwd()+'/structure_maison/'
    # PROJECT_PATH+'/structure_maison/test_architecture.yaml
    YML = yaml_loader.yamlloader(YamlProjetPath)
    data = YML.open('test_architecture.yaml', Mode='r')
    YML.show()
    data.close()
    # print(data)
    KeyToModify = 'superficie'
    Value = 50
    # YML.append(superficie=Value)
