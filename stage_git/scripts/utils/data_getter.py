import os
import netrc
from ftplib import FTP
import logging
import tarfile
from ftp_checker import checkFile

def get_file(hendrix_path, filename, local_path, local_fname=""):
    """Récupère le fichier sur hendrix pour le ramener sur le repertoire local.

    Args:
        hendrix_path (str): Path sur hendrix 
        filename (str): Nom du fichier sur hendrix 
        local_path (str): Path sur la machine
        local_fname, Optional (str): Nom du fichier en local (si non renseigné copie celui sur hendrix)
    
    """
    FileChecker = checkFile("hendrix", hendrix_path, filename)
    if FileChecker.check():
        net_handler = netrc.netrc()
        user, _, mdp = net_handler.authenticators("hendrix")
        syn = FTP("hendrix")
        syn.login(user, mdp)
        syn.cwd(hendrix_path)
        with open(os.path.join(local_path, local_fname), "wb") as fp:
            syn.retrbinary("RETR " + filename, fp.write)
        syn.close()
        return True
    else:
        logging.error(f"File does not exist on hendrix {hendrix_path}{filename}")
        return False


if __name__ == "__main__":

    print('File name :    ', os.path.basename(__file__))
    print('Directory Name:     ', os.path.dirname(__file__)) 
    print("Absolute path : ", os.path.abspath(__file__))
    abs_path = os.path.abspath(__file__)
    data_dir = os.path.dirname(os.path.dirname(os.path.dirname(abs_path)))
    print("Data_dir",data_dir)
    hendrix_path = "/home/chabotv/stage_git"
    filename = "data.tar.xz"
    local_path = data_dir 
    get_file(hendrix_path, filename, local_path, filename)

    local_file = os.path.join(local_path, filename)
    with tarfile.open(local_file) as f:
        f.extractall('.')