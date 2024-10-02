"""
Module checking that FTP file seems correct before doing any action
"""
from ftplib import FTP, error_perm
import netrc
import logging
import time


class checkFile:
    """
    An object which chek ftp files
    """

    def __init__(self, serverName: str, path: str, filename: str):
        """Initialise the object

        Args:
            serverName (str): The server
            path (str): Path on server
            filename (str): First file to check
        """
        self.serverName = serverName
        self.path = path
        self.filename = filename
        self.ftp = FTP()

    def open_connection(self) -> FTP:
        """Open a connection on the server

        Returns:
            FTP: the FTP connection
        """
        try:
            # On reduit le timeout a 5s (pour la connection). Accelere grandement le
            # process sans trop de perte.
            ftp = FTP(self.serverName, timeout=10)
        except Exception as e:
            logging.error(f"Erreur de connection a {self.serverName}. {e}")
        net_handler = netrc.netrc()
        user, _, mdp = net_handler.authenticators(self.serverName)
        ftp.login(user, mdp)
        return ftp

    def change_file(self, path: str, filename: str):
        """Change where we look on the server

        Args:
            path ([str]): Le nouveau chemin
            filename ([type]): Le fichier
        """
        self.path = path
        self.filename = filename

    def check(self):
        """
            Check the file existence on the Ftp servor.
            Also check that the file is large enough.

        Returns:
            [boolean]: 1 if file seems ok. False (file not present or file too small).
        """
        self.ftp = self.open_connection()
        start_time = time.perf_counter()
        res = self.check_present()
        end_time = time.perf_counter()
        logging.debug(
            f"Execution Time for check presence : {end_time - start_time:0.4f}"
        )
        end_time = time.perf_counter()
        logging.debug(f"Execution Time for Ftp check : {end_time - start_time:0.4f}")
        self.ftp.quit()
        return res

    def check_present(self):
        """Check file presence on servor

        Returns:
            [type]: [description]
        """
        try:
            self.ftp.cwd(self.path)
            if self.filename not in self.ftp.nlst():
                logging.debug(f"{self.filename} is not in {self.ftp.nlst()}")
                return False
        except error_perm:
            logging.error(f"Not able to connect to {self.path}")
            return False
        return True
