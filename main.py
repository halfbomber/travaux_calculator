#main
import yaml_loader, os
"""
{
maison: {
Hauteur: 0,
Largeur: 0,
Longueur: 0,
pieces:
    [{Salon:
        {Hauteur: 0,
        Largeur: 0,
        Longueur: 0,
        couleurs: [blanc],
        mur1: {Largeur: 0, Longueur: 0, couleur: null,type: null},
        mur2: {Largeur: 0, Longueur: 0, couleur: null, type: null},
        mur3: {Largeur: 0, Longueur: 0, couleur: null, type: null},
        mur4: {Largeur: 0,Longueur: 0, couleur: null, type: null},
        plafon: {Largeur: 0, Longueur: 0,couleur: null, type: null},
        sol: {Largeur: 0, Longueur: 0, couleur: null,type: null},
        superficie: null}
    }],
terrain: {Largeur: 0, Longueur: 0}}
}
"""

if __name__ == '__main__':
    YamlProjetPath = os.getcwd()+'/structure_maison/'
    # KeyToModify = ['maison']['Hauteur']
    # pieces':[{'salon':{'superficie':50}}]}}

    YML = yaml_loader.yamlloader(YamlProjetPath)
    MyYaml = YML.load(Stream=YML.open('test_architecture.yaml', Mode='r'))
    YML.append(Stream=MyYaml,KeysValue={"maison1","Hauteur"=50})
