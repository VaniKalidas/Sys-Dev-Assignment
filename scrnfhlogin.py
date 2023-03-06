from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from nfhlogin import Ui_dlg_login # login screen GUI
import sqlCnnSql as scs # connection to SQL Server
from globals import dbinfo # gloabl varaiables

class scrLogin(qtw.QDialog,qtw.QWidget):
    # successful authentication signal
    authsuccess = qtc.pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # get the ui form and layout
        self.ui = Ui_dlg_login()
        # attach to form widget
        self.ui.setupUi(self)
        # Trigger functionality
        #self.ui.cmdOK.clicked.connect(self.authenticate)
        self.signals()
        
    def signals(self):
        ''' Connect slots '''
        self.ui.OKbtn.clicked.connect(self.authenticate)
        self.ui.Cnlbtn.clicked.connect(self.reject)
     
    def authenticate(self):
        ''' Authenticate the login details.  '''
        if self.ui.usrbox.text() == '':
           qtw.QMessageBox.critical(self,"Username","Username cannot be blank." )
           #print("User cannot be blank")
           return
        if self.ui.passbox.text() == '':
           qtw.QMessageBox.critical(self,"Password","Password cannot be blank." )
           return
        db = scs.crtCnnSql(dbinfo.server,dbinfo.database,self.ui.txtUnme.text(),self.ui.passbox.text(),dbinfo.cnx_nbr)
        
        if scs.chkSqlUsr(dbinfo.server,dbinfo.database,self.ui.txtUnme.text(),self.ui.passbox.text()):     
            qtw.QMessageBox.information(self,"Login","Login successful." )
            # Successful authentication signal
            dbinfo.username = self.ui.txtUnme.text()
            dbinfo.password = self.ui.txtPwd.text()
            self.authsuccess.emit('Y')
            qtw.QDialog.close(self)
        else:
            qtw.QMessageBox.critical(self,"Login","Login failed." )
        return
    
    def cancelLogin(self):
        ''' Close the Login dialog. '''
        if isinstance(self.parent(), QMdiSubWindow):
            self.parent().close()
        else:
           self.close()       

if __name__ == '__main__':
    import sys
    app = qtw.QApplication([])
    widget = scrLogin()
    widget.show()
    sys.exit(app.exec_())
