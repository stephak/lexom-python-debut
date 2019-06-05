import os
import datetime
import tarfile

def tar_py(dir):
    """
    Permet de créer un tar compressé des fichiers *.py d'un repertoire


    :param dir: le repertoire mis en paramètre
    :return: création d'un tar dans le repertoire avec pour nom ddmmyyyy_pgm_py.tar
    """
    if not os.path.isdir(dir):
        print("repertoire ",dir,"non valide")
        exit(1)
    else :
        os.chdir(dir)
        nom_archive = datetime.datetime.now().strftime('%Y%m%d') + '-' + 'pgm.py.tar.gz'
        if os.name == 'posix  ':
            dirPy = subprocess.getstatusoutput("ls *.py")
            listPy=dirPy[1].split(os.linesep)
            with tarfile.open(nom_archive,'w:gz') as f:
                for elt in listPy:
                    f.add(elt)
        else :
            liste_fichiers = os.listdir()
            nb_fichiers = len(liste_fichiers)
            with tarfile.open(nom_archive,'w:gz') as f:
                for elt in liste_fichiers:
                    if elt[-3:]=='.py':
                        f.add(elt)

    return None

if __name__ == "__main__":
    rep=os.getcwd()
    print("Création d'un tar compressé des programmes en extension py")
    tar_py(rep)
