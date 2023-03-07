# scrhrprjs - uses hrprjs GUI design
import datetime

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from stock_categories import Ui_StockCategoriesDialog
import sqlCnnSql as scs
from globals import dbinfo

print(dbinfo.localhost)

class scrPrjs(qtw.QWidget):
    ''' Defines the Project CRUD function. '''
    authsuccess = qtc.pyqtSignal(str)
    dlg_mode = 'edit'
    table_row = 0
    dpt_dict = {}
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # get the screen layout
        self.ui = Ui_StockCategoriesDialog()
        # attach to form widget
        self.ui.setupUi(self)
        # Trigger functionality
        self.signals()
        # Load table data
        #if self.prjsLogin():
        db = self.cnnSql()
        if db:
            self.rtvPrjs(db)
            self.rtvdpts(db)
        db.close()
        self.set_mode("add")
      
        # now we add the functionality!
    def signals(self):
        self.ui.tblPrjs.cellClicked.connect(self.tblSelect) # table row selected
        self.ui.cmdUpd.clicked.connect(self.upd_prj)  # Update button
        self.ui.cmdAddMode.clicked.connect(self.add_mode) # add mode button
        self.ui.cmdAdd.clicked.connect(self.add_prj) # add/insert a project
        self.ui.cmdDlt.clicked.connect(self.dlt_prj) # deletes a project
            
    def cnnSql(self):
        '''  Obtain database connection using SQL Server Authentication'''
        db = scs.crtCnnSql(dbinfo.server,dbinfo.database,'hruser','hruserpwd',dbinfo.cnx_nbr)
        return db

    def rtvPrjs(self,db):
        ''' Query database and load the project data '''
        qry = QSqlQuery(db)
        sql_statement = f'SELECT ProjectId, Name, StartDate,' \
                        f'Budget, DeptName FROM project ' \
                        f'INNER JOIN Department on Project.DeptID ' \
                        f'= Department.DeptID' 
        #sql_statement = "SELECT ProjectId, Name, StartDate, Budget FROM project"
        qry.prepare(sql_statement)
        qry.exec()
        #print(sql_statement)
        while qry.next():
            rows = self.ui.tblPrjs.rowCount()
            self.ui.tblPrjs.setRowCount(rows + 1)                     
            self.ui.tblPrjs.setItem(rows, 0, qtw.QTableWidgetItem(str(qry.value(0))))
            #print("row", str(qry.value(0)))
            self.ui.tblPrjs.setItem(rows, 1, qtw.QTableWidgetItem(qry.value(1)))
            
            fmtDate = datetime.datetime.strptime(qry.value(2), '%Y-%m-%d').strftime('%d/%m/%Y')
            self.ui.tblPrjs.setItem(rows, 2, qtw.QTableWidgetItem(fmtDate))
            self.ui.tblPrjs.setItem(rows, 3, qtw.QTableWidgetItem(str(int(qry.value(3)))))
            self.ui.tblPrjs.setItem(rows, 4, qtw.QTableWidgetItem(qry.value(4)))
        # need to set all items to read-only
        for row in  range(self.ui.tblPrjs.rowCount()):
            for column in range (self.ui.tblPrjs.columnCount()):
                pass
                #self.ui.tblPrjs(row,column).setFlags()
                #table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)
                #print(column)
        
        self.ui.tblPrjs.resizeColumnsToContents()
        qry.clear()
        # db.close()

    def rtvdpts(self,db):
        ''' Retrieve all departmenst and load into combo '''
        self.dpt_dict = {}
        qry = QSqlQuery(db)
        sql_statement = f'SELECT DeptID, DeptName FROM Department ' \
                        f'ORDER BY DeptName'

        qry.prepare(sql_statement)
        qry.exec()
        rcd_count = 0
        while qry.next():           
            self.dpt_dict[qry.value(1)] = [qry.value(0),rcd_count]
            rcd_count += 1
            self.ui.cboDept.addItem(qry.value(1))            
        qry.clear()
        #print(self.dpt_dict)
                
    def tblSelect(self,row,column):
        '''Handles selection of a table row.  Moves row data to
            edit area.
            '''
        self.table_row = row
        # print("row = " , row)  # checks row selected identified correctly.
        prjId = self.ui.tblPrjs.item(row,0).text()
        prjName = self.ui.tblPrjs.item(row,1).text()
        prjSDte = self.ui.tblPrjs.item(row,2).text()
        # re-format date
        lclSDte = datetime.datetime.strptime(prjSDte, "%d/%m/%Y")
        #  Id, Prj Name, Start Date, Budget
        self.ui.txtId.setText(self.ui.tblPrjs.item(row,0).text())
        self.ui.txtNme.setText(self.ui.tblPrjs.item(row,1).text())
        self.ui.dteSDte.setDate(lclSDte)
        self.ui.txtBdgt.setText(self.ui.tblPrjs.item(row,3).text())
        #print(self.dpt_dict['Admin'])
        sel_text = ((self.ui.tblPrjs.item(row,4).text()))
        sel_index = self.dpt_dict[sel_text][1]
        self.ui.cboDept.setCurrentIndex(sel_index)
        self.set_mode("edit")        
        self.repaint()
        self.show()
    
    def add_prj(self):
        ''' Adds (inserts) a project record '''
        ins_rcd = self.get_prj()
        #print(ins_rcd)
        if ins_rcd[1] == '':
           qtw.QMessageBox.critical(self,"Add Project","Project Name cannot be blank." )
           #print("User cannot be blank")
           return
        else:
            db = self.cnnSql()
        if db:
            upd_rcd = self.get_prj()
            qry = QSqlQuery(db)
            
            sql_statement = f'INSERT INTO Project (Name,' \
                            f' StartDate, Budget, DeptID) VALUES ( \'' \
                        f'{ins_rcd[1]}\'' \
                        f' ,\'' \
                        f'{ins_rcd[2]}\' ' \
                        f' , ' \
                        f'{ins_rcd[3]},{ins_rcd[4]}   ' \
                        f' ) ' 
                        
            #print(sql_statement)
            qry.prepare(sql_statement)
            qry.exec()
            if qry.isActive():
                qtw.QMessageBox.information(self,"Project Add","Project " + ins_rcd[1] + " created." )
                # reinitialise
                self.ui.tblPrjs.setRowCount(0)
                self.clr_edits()
                db = self.cnnSql()
                if db:
                    self.rtvPrjs(db)
                db.close()
                
            else:
                qtw.QMessageBox.critical(self,"Project Add","Project " + ins_rcd[1] + " not created." )
            qry.clear()
            #print(upd_rcd)
        db.close()
               
    def upd_prj(self):
        ''' Updates a project '''
        prj_dta = self.get_prj()
        db = self.cnnSql()
        if db:
            upd_rcd = self.get_prj()
            qry = QSqlQuery(db)
            
            sql_statement = f'UPDATE Project SET Name = \'' \
                        f'{prj_dta[1]}\'' \
                        f' , StartDate = \'' \
                        f'{prj_dta[2]}\' ' \
                        f' , Budget = ' \
                        f'{prj_dta[3]}'\
                        f', DeptID = ' \
                        f'{prj_dta[4]}'\
                        f' WHERE ProjectId = ' \
                        f'{prj_dta[0]}'
            #print(sql_statement)
            qry.prepare(sql_statement)
            qry.exec()
            if qry.isActive():
                qtw.QMessageBox.information(self,"Project Updated","Project " + prj_dta[1] + " updated." )
                self.upd_row(upd_rcd)
                self.add_mode()
                self.clr_edits()
            else:
                qtw.QMessageBox.critical(self,"Project Updated","Project " + prj_dta[1] + " update failed." )
            qry.clear()
            #print(upd_rcd)
        db.close()
    
    def dlt_prj(self):
        ''' Deletes a project '''
        #print("Delete called")
        #prj_dta = self.get_prj()
        db = self.cnnSql()
        if db:
            dlt_rcd = self.get_prj()
            qry = QSqlQuery(db)
            
            sql_statement = f'DELETE FROM Project ' \
                            f' WHERE ProjectId = ' \
                            f'{dlt_rcd[0]}'
            #print(sql_statement)
            qry.prepare(sql_statement)
            qry.exec()
            if qry.isActive():
                qtw.QMessageBox.information(self,"Delete Project", "Project " + dlt_rcd[1] + " deleted." )
                self.ui.tblPrjs.setRowCount(0)
                self.clr_edits()
                db = self.cnnSql()
                if db:
                    self.rtvPrjs(db)
                db.close()
            else:
                qtw.QMessageBox.critical(self,"Delete Project", "Project " + dlt_rcd[1] + " delete failed." )
            qry.clear()            
        db.close()
           
    def upd_row(self,upd_rcd):   
        ''' Update a table row.  Used after record update. '''
        #print(upd_rcd[2])
        self.ui.tblPrjs.setItem(self.table_row, 1, qtw.QTableWidgetItem(upd_rcd[1]))
        rcdSDte = datetime.datetime.strptime(upd_rcd[2], '%Y-%m-%d').strftime('%d/%m/%Y')
        self.ui.tblPrjs.setItem(self.table_row, 2, qtw.QTableWidgetItem(rcdSDte ))
        self.ui.tblPrjs.setItem(self.table_row, 3, qtw.QTableWidgetItem(upd_rcd[3]))
        self.ui.tblPrjs.setItem(self.table_row, 4, qtw.QTableWidgetItem(self.ui.cboDept.currentText()))
 
    def get_prj(self):
        ''' Get project from edit area '''
        prj_rcd = []
        prj_rcd.append(self.ui.txtId.text()) 
        prj_rcd.append(self.ui.txtNme.text())
        scr_date = self.ui.dteSDte.date()
        #print(scr_date)
        date_text = scr_date.toString('yyyy-MM-dd')
        #print(date_text)
        prj_rcd.append(date_text)
        prj_rcd.append(self.ui.txtBdgt.text())
        # dept id is require
        rcd_deptid = self.dpt_dict[self.ui.cboDept.currentText()][0]
        prj_rcd.append(rcd_deptid)
        return prj_rcd
    
    def add_mode(self):
        ''' Changes mode to Add mode. '''
        self.ui.cmdAdd.setEnabled(True)
        self.ui.cmdDlt.setEnabled(False)
        self.ui.cmdUpd.setEnabled(False)
        self.ui.cmdAddMode.setEnabled(False)
        self.clr_edits()
    
    def set_mode(self,mode):
        ''' Configures screen according to mode; add or edit '''
        #print(mode)
        if mode  == 'add':
            self.add_mode()
           
        else:  # edit mode
            # disable add button
            self.ui.cmdAdd.setEnabled(False)
            self.ui.cmdDlt.setEnabled(True)
            self.ui.cmdUpd.setEnabled(True)
            self.ui.cmdAddMode.setEnabled(True)
        
    def clr_edits(self):
        ''' Clear the edit text boxes '''
        self.ui.txtNme.clear()
        self.ui.txtId.clear()
        today_date = qtc.QDate.currentDate()
        self.ui.dteSDte.setDate(today_date)
        self.ui.txtBdgt.setText('0')
                
if __name__ == '__main__':
    app = qtw.QApplication([])
    dbinfo.username = 'hrtest'
    dbinfo.password = 'hrtestpwd'
    widget = scrPrjs()
    widget.show()
    
    app.exec_()
        