import os
import copy
import sys
import functools
from PyQt5.QtWidgets import QMainWindow, QMenu, QInputDialog
from PyQt5 import QtWidgets
from datetime import datetime
from Front.administrador.Administrador import Ui_MainWindow
from Front.emerComunes.retorno import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QTableWidgetItem, QApplication, QMainWindow, QLineEdit, QPushButton, QWidget, QDialog
from Back.gastos import Gastos
from Back.polizas import Polizas
from Back.colillas import Colillas
from Back.usuarios import Usuarios
from Back.adicionales import Adicionales
from Back.liquidacion import Liquidacion
from Back.informe import Informes
from BD.Conexion import *


basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()
ventana_emergente = None

class EmerRetorno():

    def __init__(self):
        self.emerRetorno = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.emerRetorno)

        self.ui.botAceRet.clicked.connect(self.cerrar_ventana)

    def imprimir_retorno(self, retorno_emer):
        self.ui.LRetorno.setText(retorno_emer)

    def cerrar_ventana(self):
        self.emerRetorno.close()






class VentanasAdmin ():

    def __init__(self):

        self.ventanaAdmin = QMainWindow ()
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi(self.ventanaAdmin)

        self.ui.menu_admin1.setCurrentWidget(self.ui.polizas)
        self.ui.botCol.clicked.connect(self.ventana_colillas)
        self.ui.botPol.clicked.connect(self.ventana_polizas)
        self.ui.botGas.clicked.connect(self.ventana_gastos)
        self.ui.botUsu.clicked.connect(self.ventana_usuarios)
        self.ui.botFac.clicked.connect(self.ventana_facturas)
        self.ui.botInf.clicked.connect(self.ventana_informes)

        self.ui.botCer.clicked.connect(self.cerrar_sesion)


        self.ui.botAceLiq.clicked.connect(self.ventana_liquidacion)
        self.ui.botConPol.clicked.connect(self.ventana_consultar_poliza)
        self.ui.botModPolVen.clicked.connect(self.ventana_modificar_poliza)
        self.ui.botAceConPolSoc.clicked.connect(self.funcion_consultar_poliza)
        self.ui.botAgrPer.clicked.connect(self.ventana_agregar_persona)
        self.ui.botCrePol.clicked.connect(self.ventana_crear_poliza)
        self.ui.agrDoc.clicked.connect(self.agregar_lista_documentos)
        self.ui.agrNom.clicked.connect(self.agregar_lista_nombres)
        self.ui.agrFec.clicked.connect(self.agregar_lista_fechas)
        self.ui.agrPar.clicked.connect(self.agregar_lista_parentescos)
        self.ui.botAceCrePol.clicked.connect(self.funcion_crear_poliza)
        self.ui.botAceAgrPer.clicked.connect(self.funcion_agregar_persona)
        self.ui.botAceEliPer.clicked.connect(self.funcion_eliminar_persona)
        self.ui.botAceModPol.clicked.connect(self.funcion_modificar_poliza)
        self.ui.botEliPerDat.clicked.connect(self.funcion_eliminar_persona_poliza)

        self.ui.botNomEdiCrePol.clicked.connect(self.editar_crear_nombre_poliza)
        self.ui.botDocEdiCrePol.clicked.connect(self.editar_crear_documento_poliza)
        self.ui.botFecEdiCrePol.clicked.connect(self.editar_crear_fnto_poliza)
        self.ui.botParEdiCrePol.clicked.connect(self.editar_crear_parentesco_poliza)


        self.ui.botModPol.clicked.connect(self.funcion_guardar_modificar_poliza)
        self.ui.botEdiDatNom.clicked.connect(self.editar_dato_nombre_poliza)
        self.ui.botEdiDatDoc.clicked.connect(self.editar_dato_documento_poliza)
        self.ui.botEdiDatFec.clicked.connect(self.editar_dato_fnto_poliza)
        self.ui.botEdiDatPar.clicked.connect(self.editar_dato_parentesco_poliza)
        self.ui.botAceConPolDoc.clicked.connect(self.funcion_consultar_poliza_documento)

        self.ui.botCreCol.clicked.connect(self.ventana_ultimo_pago_documento)
        self.ui.botUltPagSoc.clicked.connect(self.ventana_ultimo_pago_socio)
        self.ui.botUltPagDoc.clicked.connect(self.ventana_crear_colilla)
        self.ui.botUltPagDoc.clicked.connect(self.ventana_crear_colilla)
        self.ui.botCreColSin.clicked.connect(self.ventana_crear_colilla_sin)
        self.ui.botAceCreColSin.clicked.connect(self.funcion_crear_colilla_sin)


        self.ui.botRevGas.clicked.connect(self.venta_revisar_gastos)

        self.ui.botCreUsu.clicked.connect(self.venta_crear_usuario)
        self.ui.botEliUsu.clicked.connect(self.venta_eliminar_usuario)
        self.ui.botMosTod.clicked.connect(self.venta_mostrar_todo_usuario)
        self.ui.botAceCreUsu.clicked.connect(self.funcion_crear_usuario)
        self.ui.botAceEliUsu.clicked.connect(self.funcion_eliminar_usuario)

        self.ui.botCreFac.clicked.connect(self.venta_crear_factura)
        self.ui.agrDes.clicked.connect(self.agregar_lista_descripciones)
        self.ui.AgrCan.clicked.connect(self.agregar_lista_cantidades)
        self.ui.agrVal.clicked.connect(self.agregar_lista_valores)
        self.ui.botAceCreFac.clicked.connect(self.funcion_crear_factura_caja)
        self.ui.botAboFac.clicked.connect(self.venta_abonar_caja)
        self.ui.botAceAboFac.clicked.connect(self.funcion_abonar_factura_caja)
        self.ui.botConEliFac.clicked.connect(self.venta_consultar_factura)
        self.ui.botAceConFac.clicked.connect(self.funcion_consultar_factura_caja)

        states_cities = ['Funeraria', 'Jefe 1', 'Jefe 2']

        menu = QMenu()
        menu.triggered.connect(lambda x: print(self.escoger_ventana_gastos(x.text())))
        self.ui.desGas.setMenu(menu)
        self.add_menu(states_cities, menu)
        self.ui.botAceGasFun.clicked.connect(self.funcion_gasto_funeraria)
        self.ui.botAceGasJef1.clicked.connect(self.funcion_gasto_jefe1)
        self.ui.botAceGasJef2.clicked.connect(self.funcion_gasto_jefe2)



        self.ui.botAceCreCol.clicked.connect(self.funcion_crear_colilla)
        self.ui.botAceUltSoc.clicked.connect(self.funcion_ultimo_socio)
        self.ui.botAceBusUltDoc.clicked.connect(self.funcion_ultimo_documento)

        self.ui.botGenLiq.clicked.connect(self.ventana_liquidacion)
        self.ui.botAceGen.clicked.connect(self.funcion_generar_liquidacion)



        informes = ['Ultimo saldo', 'Saldo', 'Colillas', 'Gastos', 'Facturas caja']

        menu_1 = QMenu()
        menu_1.triggered.connect(lambda x: print(self.escoger_ventana_informes(x.text())))
        self.ui.desInfNoLiq.setMenu(menu_1)
        self.add_menu_inf(informes, menu_1)

        self.ui.botCanUltSoc.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_3))
        self.ui.botCanUltSoc.clicked.connect(lambda: self.cler_table_edits(self.ui.stackedWidget_3))
        self.ui.botCanCreCol.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_3))
        self.ui.botInvAdm_27.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_3))
        self.ui.botInvAdm_27.clicked.connect(lambda: self.cler_table_edits(self.ui.stackedWidget_3))


        self.ui.botCanGasJef1.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_4))
        self.ui.botCanGasJef2.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_4))
        self.ui.botCanGasFun.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_4))

        self.ui.botCanEliUsu.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_5))

        self.ui.botCanConFac.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_6))
        self.ui.botCanConFac.clicked.connect(lambda: self.cler_table_edits(self.ui.stackedWidget_6))
        self.ui.botCanAboFac.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_6))
        self.ui.botCanCreFac.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_6))
        self.ui.botCanCreFac.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_6))

        self.ui.botCanConPolDoc.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolDoc.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolSoc.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolSoc.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))
        self.ui.botCanEliPer.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanAgrPer.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanCrePol.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanCrePol.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))



    def clear_line_edits(self, stacked_widget):
        # Obtener el índice de la página actual
        current_index = stacked_widget.currentIndex()

        # Obtener el widget de la página actual
        current_widget = stacked_widget.widget(current_index)

        # Buscar todos los QLineEdits dentro del widget actual
        line_edits = current_widget.findChildren(QLineEdit)

        # Limpiar el contenido de los QLineEdits
        for line_edit in line_edits:
            line_edit.clear()

    def clear_list_edits(self, stacked_widget):

        current_index = stacked_widget.currentIndex()

        # Obtener el widget de la página actual
        current_widget = stacked_widget.widget(current_index)

        list_widgets = current_widget.findChildren(QtWidgets.QListWidget)  # Obtener todos los QListWidget en la página

        for list_widget in list_widgets:
            list_widget.clear()  # Borrar el contenido de cada QListWidget

    def cler_table_edits(self, stacked_widget):
        current_index = stacked_widget.currentIndex()

        current_widget = stacked_widget.widget(current_index)
        table_widgets = current_widget.findChildren(QtWidgets.QTableWidget)  # Obtener todas las QTableWidget en la página

        for table_widget in table_widgets:
            table_widget.clearContents()  # Borrar el contenido de las celdas de cada QTableWidget
            table_widget.setRowCount(0)

    def add_menu_inf(self, data, menu_obj):
        print('este es data ', data)

        if isinstance(data, dict):
            for k, v in data.items():
                sub_menu = QMenu(k, menu_obj)
                menu_obj.addMenu(sub_menu)
                self.add_menu_inf(v, sub_menu)
        elif isinstance(data, list):
            for element in data:
                self.add_menu_inf(element, menu_obj)
        else:
            action = menu_obj.addAction(data)
            action.setIconVisibleInMenu(False)


    def escoger_ventana_informes (self, data):
        print(data)
        print('llegue a escoger_venta_informe')
        if data == 'Ultimo saldo':
            self.venta_ultimo_saldo()
        elif data == 'Saldo':
            self.venta_informe_saldos()
        elif data == 'Colillas':
            self.venta_informe_colillas()
        elif data == 'Gastos':
            self.venta_informe_gastos()
        elif data == 'Facturas caja':
            self.venta_informe_facturas()


    def add_menu(self, data, menu_obj):
        print('este es data ', data)

        if isinstance(data, dict):
            for k, v in data.items():
                sub_menu = QMenu(k, menu_obj)
                menu_obj.addMenu(sub_menu)
                self.add_menu(v, sub_menu)
        elif isinstance(data, list):
            for element in data:
                self.add_menu(element, menu_obj)
        else:
            action = menu_obj.addAction(data)
            action.setIconVisibleInMenu(False)


    def escoger_ventana_gastos (self, data):
        print(data)
        print('llegue a escoger_venta_gastos')
        if data == 'Funeraria':
            self.venta_gasto_funeraria()
        elif data == 'Jefe 1':
            self.venta_gasto_jefe1()
        elif data == 'Jefe 2':
            self.venta_gasto_jefe2()

    def show(self):
        self.ventanaAdmin.show()

    def ventana_polizas (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.polizas)

    def ventana_colillas (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.colillas)

    def ventana_gastos (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.gastos)

    def ventana_usuarios (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.usuarios)

    def ventana_facturas (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.facturas_caja)

    def ventana_informes (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.informes)

    def ventana_liquidacion(self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.page_3)
        self.ui.menu_generar_liquidacion.setCurrentWidget(self.ui.generar_liquidacion)


    def ventana_consultar_poliza (self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.consultar_poliza)

    def funcion_consultar_poliza_documento(self):
        poliza = Polizas ()
        ret_con_pol_doc = poliza.consultar_poliza_documento(self.ui.LDocConPol.text())
        del poliza
        print(len(ret_con_pol_doc))
        if isinstance(ret_con_pol_doc, str):
            self.crear_ventana_retorno(ret_con_pol_doc)
        else:
            if len(ret_con_pol_doc) == 1:

                self.ui.LValMesPol.setText(str(ret_con_pol_doc[0][0]))
                self.ui.LDesPol.setText(str(ret_con_pol_doc[0][1]))
                self.ui.LHasPol.setText(str(ret_con_pol_doc[0][2]))
                self.agregar_lista_nombres_consultar(ret_con_pol_doc[0][3])
                self.agregar_lista_documentos_consultar(ret_con_pol_doc[0][4])
                self.agregar_lista_fechas_consultar(ret_con_pol_doc[0][5])
                self.agregar_lista_parentescos_consultar(ret_con_pol_doc[0][6])
                self.ui.LSocConPol.setText(str(ret_con_pol_doc[0][7]))
            else:
                socios = [sublista[7] for sublista in ret_con_pol_doc]
                self.crear_ventana_retorno(socios)

    def funcion_consultar_poliza(self):
        poliza = Polizas()
        ret_con_pol = poliza.consultar_poliza_socio(self.ui.LSocConPol.text())
        if isinstance(ret_con_pol, str):
            self.crear_ventana_retorno(ret_con_pol)
        else:
            self.ui.LValMesPol.setText(str(ret_con_pol[0]))
            self.ui.LDesPol.setText(str(ret_con_pol[1]))
            self.ui.LHasPol.setText(str(ret_con_pol[2]))
            self.agregar_lista_nombres_consultar(ret_con_pol[3])
            self.agregar_lista_documentos_consultar(ret_con_pol[4])
            self.agregar_lista_fechas_consultar(ret_con_pol[5])
            self.agregar_lista_parentescos_consultar(ret_con_pol[6])


    def agregar_lista_nombres_consultar (self, nombres):
        for nombre in nombres:
            self.ui.lisNomPol.addItem(str(nombre))

    def agregar_lista_documentos_consultar (self, documentos):
        for documento in documentos:
            self.ui.lisDocPol.addItem(str(documento))

    def agregar_lista_fechas_consultar (self, fechas):
        for fecha in fechas:
            self.ui.lisFecPol.addItem(str(fecha))

    def agregar_lista_parentescos_consultar (self, parentescos):
        for parentesco in parentescos:
            self.ui.lisParPol.addItem(str(parentesco))





    def ventana_agregar_persona (self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.agregar_persona)

    def funcion_agregar_persona (self):
        poliza = Polizas()
        self.fun_agr_per = poliza.agregar_persona_poliza(self.ui.LSocAgrPer.text(), self.ui.LDocAgrPer.text(), self.ui.LNomAgrPer.text(),
                                                         self.ui.LFecAgrPer.text(), self.ui.LParAgrPer.text(), self.ui.LValAgrPer.text())
        del poliza
        self.clear_line_edits(self.ui.stackedWidget_2)
        self.crear_ventana_retorno(self.fun_agr_per)

    def ventana_eliminar_persona(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.eliminar_persona)

    def funcion_eliminar_persona (self):
        poliza = Polizas()
        self.fun_eli_per = poliza.eliminar_persona(self.ui.LSocEliPer.text(), self.ui.LDocEliPer.text(), self.ui.LValEliPer.text())
        del poliza
        self.clear_line_edits(self.ui.stackedWidget_2)
        self.crear_ventana_retorno(self.fun_eli_per)

    def ventana_modificar_poliza(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.modificar_poliza)

    def funcion_modificar_poliza(self):
        poliza = Polizas()
        ret_con_pol = poliza.consultar_poliza_socio(self.ui.LSocModPol.text())
        if isinstance(ret_con_pol, str):
            self.crear_ventana_retorno(ret_con_pol)
        else:
            self.ui.LValMesModPol.setText(str(ret_con_pol[0]))
            self.ui.LDesdModPol.setText(str(ret_con_pol[1]))
            self.ui.LHasModPol.setText(str(ret_con_pol[2]))
            self.agregar_lista_nombres_modificar(ret_con_pol[3])
            self.agregar_lista_documentos_modificar(ret_con_pol[4])
            self.agregar_lista_fechas_modificar(ret_con_pol[5])
            self.agregar_lista_parentescos_modificar(ret_con_pol[6])

    def agregar_lista_nombres_modificar(self, nombres):
        for nombre in nombres:
            self.ui.lisNomModPol.addItem(str(nombre))

    def agregar_lista_documentos_modificar(self, documentos):
        for documento in documentos:
            self.ui.lisDocModPol.addItem(str(documento))

    def agregar_lista_fechas_modificar(self, fechas):
        for fecha in fechas:
            self.ui.lisFecModPol.addItem(str(fecha))

    def agregar_lista_parentescos_modificar(self, parentescos):
        for parentesco in parentescos:
            self.ui.lisParModPol.addItem(str(parentesco))

    def funcion_eliminar_persona_poliza(self):
        pass

    def editar_dato_nombre_poliza(self):
        sel_items = self.ui.lisNomModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDatoAgregar.text())
        self.ui.LDatoAgregar.clear()

    def editar_dato_documento_poliza(self):
        sel_items = self.ui.lisDocModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDatoAgregar.text())
        self.ui.LDatoAgregar.clear()

    def editar_dato_fnto_poliza(self):
        sel_items = self.ui.lisFecModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LFechaAgregar.text())


    def editar_dato_parentesco_poliza(self):
        sel_items = self.ui.lisParModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDatoAgregar.text())
        self.ui.LDatoAgregar.clear()

    def funcion_guardar_modificar_poliza(self):
        list_nom = [self.ui.lisNomModPol.item(index).text() for index in range(self.ui.lisNomModPol.count())]
        list_doc = [self.ui.lisDocModPol.item(index).text() for index in range(self.ui.lisDocModPol.count())]
        list_fec = [self.ui.lisFecModPol.item(index).text() for index in range(self.ui.lisFecModPol.count())]
        list_par = [self.ui.lisParModPol.item(index).text() for index in range(self.ui.lisParModPol.count())]
        poliza = Polizas()
        self.fun_mod_pol = poliza.modificar_poliza(self.ui.LSocModPol.text(), list_nom,
                                                         list_doc,
                                                         list_fec, list_par,
                                                         self.ui.LValMesModPol.text())
        del poliza

        self.clear_line_edits(self.ui.stackedWidget_2)
        self.clear_list_edits(self.ui.stackedWidget_2)
        self.crear_ventana_retorno(self.fun_mod_pol)






    def ventana_crear_poliza(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.crear_poliza)

    def agregar_lista_documentos (self):
        doc = QListWidgetItem(str(self.ui.LDocCrePol.text()))
        self.ui.LisDocCrePol.addItem(doc)
        self.ui.LDocCrePol.clear()

    def agregar_lista_nombres (self):
        nom = QListWidgetItem(self.ui.LNomCrePol.text())
        self.ui.LisNomCrePol.addItem(nom)
        self.ui.LNomCrePol.clear()

    def agregar_lista_parentescos (self):
        par = QListWidgetItem(self.ui.LParCrePol.text())
        self.ui.LisParCrePol.addItem(par)
        self.ui.LParCrePol.clear()

    def agregar_lista_fechas (self):
        fec = QListWidgetItem(self.ui.LFecCrePol.text())
        self.ui.LisFecCrePol.addItem(fec)


    def funcion_crear_poliza (self):
        list_nom = [self.ui.LisNomCrePol.item(index).text() for index in range(self.ui.LisNomCrePol.count())]
        list_doc = [self.ui.LisDocCrePol.item(index).text() for index in range(self.ui.LisDocCrePol.count())]
        list_fec = [self.ui.LisFecCrePol.item(index).text() for index in range(self.ui.LisFecCrePol.count())]
        list_par = [self.ui.LisParCrePol.item(index).text() for index in range(self.ui.LisParCrePol.count())]
        poliza = Polizas()

        print('error en la funcion')
        self.fun_cre_pol = poliza.crear_poliza(self.ui.LSocCrePol.text(), list_nom, list_doc,
                                               list_fec, list_par, self.ui.LValCrePol.text(),
                                                  self.ui.LNumCrePol.text(), 'marica')
        print('el error esta en la devuelta')
        self.crear_ventana_retorno(self.fun_cre_pol)


        del poliza

        self.clear_line_edits(self.ui.stackedWidget_2)
        self.clear_list_edits(self.ui.stackedWidget_2)





    def editar_crear_nombre_poliza(self):
        sel_items = self.ui.LisNomCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LNomCrePol.text())
        self.ui.LNomCrePol.clear()

    def editar_crear_documento_poliza(self):
        sel_items = self.ui.LisDocCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDocCrePol.text())
        self.ui.LDocCrePol.clear()

    def editar_crear_fnto_poliza(self):
        sel_items = self.ui.LisFecCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LFecCrePol.text())


    def editar_crear_parentesco_poliza(self):
        sel_items = self.ui.LisParCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LParCrePol.text())
        self.ui.LParCrePol.clear()






    def crear_ventana_retorno(self, retorno):

        self.ventana_emergente = EmerRetorno ()
        self.ventana_emergente.emerRetorno.show()
        self.ventana_emergente.imprimir_retorno(str(retorno))

    def ventana_ultimo_pago_socio(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.buscar_colilla_poliza)

    def funcion_ultimo_socio(self):
        colilla = Colillas()
        self.fun_ult_pag_soc = colilla.consultar_ultimo_pago(self.ui.LSocUltPag.text())
        del colilla

        if isinstance(self.fun_ult_pag_soc, str):
            self.crear_ventana_retorno(self.fun_ult_pag_soc)

        else:
            print('entre a crear tabla de ultimo socio')
            self.ui.tableWidget.clearContents()
            print(self.fun_ult_pag_soc)
            self.ui.tableWidget.show()
            self.ui.tableWidget.setRowCount(1)
            if self.fun_ult_pag_soc is not None:
                print('voy a imprimir')
                fila = 0
                self.ui.tableWidget.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(self.fun_ult_pag_soc[0])))
                self.ui.tableWidget.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(self.fun_ult_pag_soc[1])))
                self.ui.tableWidget.setItem(fila, 2,
                                            QtWidgets.QTableWidgetItem(self.fun_ult_pag_soc[2].strftime("%Y-%m-%d")))
                self.ui.tableWidget.setItem(fila, 3,
                                            QtWidgets.QTableWidgetItem(self.fun_ult_pag_soc[3].strftime("%Y-%m-%d")))
                self.ui.tableWidget.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(self.fun_ult_pag_soc[4])))
                self.ui.tableWidget.setItem(fila, 5,
                                            QtWidgets.QTableWidgetItem(self.fun_ult_pag_soc[5].strftime("%Y-%m-%d")))
            else:
                print('No se encontró ninguna póliza')


    def ventana_ultimo_pago_documento(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.buscar_colilla_documento)

    def funcion_ultimo_documento (self):
        colilla = Colillas()
        print('entre a consultar con documento')
        self.fun_ult_pag_doc = colilla.consultar_colilla_documento(self.ui.LDocUltPag.text())
        del colilla
        print(self.fun_ult_pag_doc)
        if isinstance(self.fun_ult_pag_doc, str):
            print('estoy en la creacion de la ventana')
            self.crear_ventana_retorno(str(self.fun_ult_pag_doc))

        else:
            print(self.fun_ult_pag_doc)
            self.ui.tableWidget_2.clearContents()
            print(self.fun_ult_pag_doc)
            self.ui.tableWidget_2.show()
            if self.fun_ult_pag_doc != None:
                fila = 0
                self.ui.tableWidget_2.setRowCount(len(self.fun_ult_pag_doc))
                for elementos in self.fun_ult_pag_doc:
                    print(elementos)
                    self.ui.tableWidget_2.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                    self.ui.tableWidget_2.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                    self.ui.tableWidget_2.setItem(fila, 2, QtWidgets.QTableWidgetItem( elementos[2].strftime("%Y-%m-%d")))
                    self.ui.tableWidget_2.setItem(fila, 3, QtWidgets.QTableWidgetItem(elementos[3].strftime("%Y-%m-%d")))
                    self.ui.tableWidget_2.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                    self.ui.tableWidget_2.setItem(fila, 5, QtWidgets.QTableWidgetItem(elementos[5].strftime("%Y-%m-%d")))
                    fila = fila + 1
            else:
                print('no encontre')


    def ventana_crear_colilla(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.crear_colilla)

    def funcion_crear_colilla (self):
        colilla = Colillas()
        self.fun_cre_col = colilla.crear_colilla_socio(self.ui.LSocCreCol.text(), self.ui.LNumCreCol.text(), self.usuario[2])
        del colilla
        self.clear_line_edits(self.ui.stackedWidget_3)
        self.crear_ventana_retorno(self.fun_cre_col)

    def ventana_crear_colilla_sin(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.crear_colilla_sin)

    def funcion_crear_colilla_sin (self):
        colilla = Colillas()
        self.fun_cre_col_sin = colilla.crear_colilla_socio_sin(self.ui.LSocCreColSin.text(),self.ui.LValCreColSin.text(), self.ui.LDesCreColSin.text(),self.ui.LNumCreColSin.text(), self.usuario[2])
        del colilla
        self.clear_line_edits(self.ui.stackedWidget_3)
        self.crear_ventana_retorno(self.fun_cre_col_sin)




    def venta_gasto_jefe1 (self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.gasto_jefe1)

    def funcion_gasto_jefe1 (self):
        gasto = Gastos ()
        ret_fun_gas_jef1 = gasto.gasto_jefe1(self.ui.LGasJef1.text() ,self.ui.LValJef1Gas.text(), 'julio')
        del gasto
        self.clear_line_edits(self.ui.stackedWidget_4)
        self.crear_ventana_retorno(ret_fun_gas_jef1)

    def venta_gasto_jefe2 (self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.gasto_jefe2)

    def funcion_gasto_jefe2 (self):
        gasto = Gastos ()
        print(self.ui.LGasJef2.text())
        ret_fun_gas_jef2 = gasto.gasto_jefe2(self.ui.LGasJef2.text(), self.ui.LValJef2Gas.text(), 'armando')
        del gasto
        self.clear_line_edits(self.ui.stackedWidget_4)
        self.crear_ventana_retorno(ret_fun_gas_jef2)


    def venta_gasto_funeraria (self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.gasto_funeraria)

    def funcion_gasto_funeraria (self):
        gasto = Gastos ()
        ret_fun_gas_fun = gasto.gasto_funeraria(self.ui.LGasFun.text(), self.ui.LValFunGas.text(), 'funeraria')
        del gasto
        self.clear_line_edits(self.ui.stackedWidget_4)
        self.crear_ventana_retorno(ret_fun_gas_fun)

    def venta_revisar_gastos(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.revisar_gastos)
        self.funcion_revisar_gastos()

    def funcion_revisar_gastos(self):
        gastos = Gastos()
        ret_gas_rev = gastos.gastos_sin_revisar()

        self.ui.tabla_gastos.clearContents()
        self.ui.tabla_gastos.show()

        if ret_gas_rev is not None:
            self.ui.tabla_gastos.setRowCount(len(ret_gas_rev))

            for fila, elementos in enumerate(ret_gas_rev):
                self.ui.tabla_gastos.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.ui.tabla_gastos.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.ui.tabla_gastos.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.ui.tabla_gastos.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.ui.tabla_gastos.setItem(fila, 4,
                                             QtWidgets.QTableWidgetItem(str(elementos[4].strftime("%Y-%m-%d"))))
                self.ui.tabla_gastos.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.ui.tabla_gastos.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.ui.tabla_gastos.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                self.ui.tabla_gastos.setItem(fila, 8, QtWidgets.QTableWidgetItem(str(elementos[8])))

                button = QtWidgets.QPushButton("Revisar")
                self.ui.tabla_gastos.setCellWidget(fila, 9, button)

                self.ret_gas_rev_copy = copy.deepcopy(ret_gas_rev)

                # Conectar la señal clicked del botón a una función lambda para capturar el valor actual de fila
                button.clicked.connect(functools.partial(self.handle_button_clicked, fila))
        else:
            print('no encontré')

    def handle_button_clicked(self, fila):

        valor = self.ui.tabla_gastos.item(fila, 0).text()
        gasto = Gastos()
        print(valor)
        print(fila)
        gasto.revisar_gastos(int(valor))
        print('hice el gasto')


        # Eliminar la fila correspondiente
        self.ui.tabla_gastos.removeRow(fila)
        self.ret_gas_rev_copy.pop(fila)

        # Actualizar el número de fila en todos los botones "Revisar" restantes
        for fila, elementos in enumerate(self.ret_gas_rev_copy):
            # ...

            button = QtWidgets.QPushButton("Revisar")
            self.ui.tabla_gastos.setCellWidget(fila, 9, button)

            # Conectar la señal clicked del botón usando functools.partial para pasar la fila como argumento adicional
            button.clicked.connect(functools.partial(self.handle_button_clicked, fila))

        # Actualizar el número de filas en la tabla
        self.ui.tabla_gastos.setRowCount(len(self.ret_gas_rev_copy))

    def venta_crear_usuario (self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.crear_usuario)

    def funcion_crear_usuario (self):
        usuario = Usuarios ()
        self.ret_fun_cre_usu = usuario.crear_usuario(self.ui.LConCreUsu.text(), self.ui.LNomCreUsu.text(), self.ui.LDocCreUsu.text(), self.ui.LCarCreUsu.text())
        del usuario
        self.clear_line_edits(self.ui.stackedWidget_5)
        self.crear_ventana_retorno(self.ret_fun_cre_usu)


    def venta_eliminar_usuario (self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.eliminar_usuario)

    def funcion_eliminar_usuario (self):
        usuario = Usuarios ()
        self.ret_eli_usu = usuario.eliminar_usuario(self.ui.LIdEliUsu.text())
        del usuario
        self.clear_line_edits(self.ui.stackedWidget_5)
        self.crear_ventana_retorno(self.ret_eli_usu)


    def venta_mostrar_todo_usuario(self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.mostrar_todos)
        usuario = Usuarios ()
        self.todos_usuarios = usuario.mostrar_usuarios()
        del usuario
        if isinstance(self.todos_usuarios, str):
            self.crear_ventana_retorno(self.todos_usuarios)

        else:
            print(self.todos_usuarios)
            self.ui.tabMosTod.clearContents()
            print(self.todos_usuarios)
            self.ui.tabMosTod.show()
            if self.todos_usuarios != None:
                fila = 0
                self.ui.tabMosTod.setRowCount(len(self.todos_usuarios))
                for elementos in self.todos_usuarios:
                    print(elementos)
                    self.ui.tabMosTod.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                    self.ui.tabMosTod.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                    self.ui.tabMosTod.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                    self.ui.tabMosTod.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                    fila = fila + 1
            else:
                print('no encontre')





    def venta_crear_factura(self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.crear_caja)

    def funcion_crear_factura_caja (self):
        lis_des = [self.ui.lisDes.item(index).text() for index in range(self.ui.lisDes.count())]
        lis_can = [self.ui.lisCan.item(index).text() for index in range(self.ui.lisCan.count())]
        lis_val = [self.ui.lisVal.item(index).text() for index in range(self.ui.lisVal.count())]
        factura = Adicionales ()
        ret_fun_cre_fac = factura.crear_factura_caja(self.ui.LCiuCreFac.text(), self.ui.LNomCreFac.text(), self.ui.LDocCreFac.text(), self.ui.LNomCreFac.text(), lis_des, lis_can, lis_val, self.usuario[2])
        del factura
        self.clear_line_edits(self.ui.stackedWidget_6)
        self.clear_list_edits(self.ui.stackedWidget_6)
        self.crear_ventana_retorno(ret_fun_cre_fac)


    def agregar_lista_descripciones(self):
        des = QListWidgetItem(str(self.ui.LDesCreFac.text()))
        self.ui.lisDes.addItem(des)

    def agregar_lista_cantidades(self):
        can = QListWidgetItem(self.ui.LCanCreFac.text())
        self.ui.lisCan.addItem(can)

    def agregar_lista_valores(self):
        val = QListWidgetItem(self.ui.LValCreFac.text())
        self.ui.lisVal.addItem(val)



    def venta_abonar_caja (self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.abonar_caja)

    def funcion_abonar_factura_caja (self):
        facturas = Adicionales ()
        ret_abo_fac_caj = facturas.abonar_factura_caja(self.ui.LIdFacAbo.text(), self.ui.LPreAbo.text(),self.usuario[2])
        del facturas
        self.clear_line_edits(self.ui.stackedWidget_6)
        self.crear_ventana_retorno(ret_abo_fac_caj)


    def venta_consultar_factura (self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.consultar_caja)

    def funcion_consultar_factura_caja (self):
        facturas = Adicionales ()
        ret_con_fac_caj = facturas.consultar_saldo_facturas_documento(self.ui.LDocConfac.text())
        self.ui.LValTotDoc.setText(str(ret_con_fac_caj[1]))
        del facturas
        if isinstance(ret_con_fac_caj, str):
            self.crear_ventana_retorno(ret_con_fac_caj)

        else:

            print(ret_con_fac_caj[0])

            self.ui.tabConFac.clearContents()
            print(ret_con_fac_caj[0])
            self.ui.tabConFac.show()
            if ret_con_fac_caj[0] != None:
                fila = 0
                self.ui.tabConFac.setRowCount(len(ret_con_fac_caj[0]))
                for elementos in ret_con_fac_caj[0]:
                    print(elementos)
                    self.ui.tabConFac.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                    self.ui.tabConFac.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[2])))
                    self.ui.tabConFac.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[3])))
                    self.ui.tabConFac.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[-2])))
                    self.ui.tabConFac.setItem(fila, 4, QtWidgets.QTableWidgetItem((elementos[-1].strftime("%Y-%m-%d"))))
                    fila = fila + 1
            else:
                print('no encontre')

    def funcion_generar_liquidacion(self):
        liquidacion = Liquidacion ()
        ret_gen_liq = liquidacion.generar_liquidacion('', '', '', '')
        self.venta_liquidacion_generada(ret_gen_liq)
        self.clear_line_edits(self.ui.menu_generar_liquidacion)

    def venta_liquidacion_generada (self, ret_gen_liq):
        self.ui.menu_generar_liquidacion.setCurrentWidget(self.ui.liquidacion_generada)
        self.ui.LGasJef1Tot.setText(str(ret_gen_liq[0]))
        self.ui.LGasJef2Tot.setText(str(ret_gen_liq[1]))
        self.ui.LSalJef1Tot.setText(str(ret_gen_liq[2]))
        self.ui.LSalJef2Tot.setText(str(ret_gen_liq[3]))


    def venta_ultimo_saldo(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.ultimo_saldo)
        self.funcion_consultar_informe_ultimo_saldo()

    def venta_informe_saldos(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.saldo_informe)
        self.funcion_consultar_informe_saldo()

    def venta_informe_colillas(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.colillas_informe)
        self.funcion_consultar_informe_colillas()

    def venta_informe_gastos(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.gastos_informe)
        self.funcion_consultar_informe_gastos()

    def venta_informe_facturas(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.factura_caja_informe)
        self.funcion_consultar_informe_facturas()




    def funcion_consultar_informe_saldo (self):
        informe = Informes ()
        ret_con_inf_sal = informe.mostrar_saldo_no_liquidado()
        del informe
        print('estoy en informe saldo')
        print(ret_con_inf_sal)
        self.ui.tabInfSal.clearContents()
        self.ui.tabInfSal.show()
        if ret_con_inf_sal != None:
            fila = 0
            self.ui.tabInfSal.setRowCount(len(ret_con_inf_sal))
            for elementos in ret_con_inf_sal:
                print(elementos)
                self.ui.tabInfSal.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.ui.tabInfSal.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.ui.tabInfSal.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.ui.tabInfSal.setItem(fila, 3, QtWidgets.QTableWidgetItem((elementos[3])))
                self.ui.tabInfSal.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.ui.tabInfSal.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.ui.tabInfSal.setItem(fila, 6, QtWidgets.QTableWidgetItem((elementos[6].strftime("%Y-%m-%d"))))
                fila = fila + 1
        else:
            print('no encontre')

    def funcion_consultar_informe_colillas (self):
        informe = Informes ()
        ret_con_inf_col = informe.mostrar_colillas_no_liquidadas()
        del informe
        print('estoy en informe colillas')
        print(ret_con_inf_col)
        self.ui.tabCol.clearContents()
        self.ui.tabCol.show()
        if ret_con_inf_col != None:
            fila = 0
            self.ui.tabCol.setRowCount(len(ret_con_inf_col))
            for elementos in ret_con_inf_col:
                print(elementos)
                self.ui.tabCol.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.ui.tabCol.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.ui.tabCol.setItem(fila, 2, QtWidgets.QTableWidgetItem((elementos[2].strftime("%Y-%m-%d"))))
                self.ui.tabCol.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3].strftime("%Y-%m-%d"))))
                self.ui.tabCol.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.ui.tabCol.setItem(fila, 5, QtWidgets.QTableWidgetItem((elementos[5].strftime("%Y-%m-%d"))))

                fila = fila + 1
        else:
            print('no encontre')

    def funcion_consultar_informe_facturas (self):
        informe = Informes ()
        ret_con_inf_fac = informe.mostrar_adicionales_no_liquidado()
        del informe
        print('estoy en informe facturas caja')
        print(ret_con_inf_fac)
        self.ui.tabFac.clearContents()
        self.ui.tabFac.show()
        if ret_con_inf_fac != None:
            fila = 0
            self.ui.tabFac.setRowCount(len(ret_con_inf_fac))
            for elementos in ret_con_inf_fac:
                print(elementos)
                self.ui.tabFac.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.ui.tabFac.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.ui.tabFac.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.ui.tabFac.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.ui.tabFac.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.ui.tabFac.setItem(fila, 5, QtWidgets.QTableWidgetItem((elementos[5].strftime("%Y-%m-%d"))))

                fila = fila + 1
        else:
            print('no encontre')

    def funcion_consultar_informe_gastos (self):
        informe = Informes ()
        ret_con_inf_gas = informe.mostrar_gastos_no_liquidados()
        del informe
        print('estoy en informe gastos')
        print(ret_con_inf_gas)
        self.ui.tabGas.clearContents()
        self.ui.tabGas.show()
        if ret_con_inf_gas != None:
            fila = 0
            self.ui.tabGas.setRowCount(len(ret_con_inf_gas))
            for elementos in ret_con_inf_gas:
                print(elementos)
                self.ui.tabGas.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.ui.tabGas.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.ui.tabGas.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.ui.tabGas.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.ui.tabGas.setItem(fila, 4, QtWidgets.QTableWidgetItem((elementos[4].strftime("%Y-%m-%d"))))

                fila = fila + 1
        else:
            print('no encontre')

    def funcion_consultar_informe_ultimo_saldo(self):
        informe = Informes ()
        ret_fun_con_ult_sal = informe.mostrar_ultimo_saldo()
        del informe
        self.ui.tabUltSal.clearContents()
        print(ret_fun_con_ult_sal)
        self.ui.tabUltSal.show()
        self.ui.tabUltSal.setRowCount(1)
        if ret_fun_con_ult_sal is not None:
            print('voy a imprimir')
            fila = 0
            self.ui.tabUltSal.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(ret_fun_con_ult_sal[0])))
            self.ui.tabUltSal.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(ret_fun_con_ult_sal[1])))
            self.ui.tabUltSal.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(ret_fun_con_ult_sal[2])))
            self.ui.tabUltSal.setItem(fila, 3, QtWidgets.QTableWidgetItem((ret_fun_con_ult_sal[3])))
            self.ui.tabUltSal.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(ret_fun_con_ult_sal[4])))
            self.ui.tabUltSal.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(ret_fun_con_ult_sal[5])))
            self.ui.tabUltSal.setItem(fila, 6, QtWidgets.QTableWidgetItem((ret_fun_con_ult_sal[6].strftime("%Y-%m-%d"))))
        else:
            print('No se encontró ninguna póliza')

    def recibir_datos(self, datos_usuario):
        self.usuario = datos_usuario
        self.ui.Nombre_usuario_2.setText(str(datos_usuario[2]))
        self.ui.Documento.setText(str(datos_usuario[3]))
        self.ui.conexion.setText('conexion exitosa')


    def cerrar_sesion(self):
        self.ventanaAdmin.close()
        from Front.VentanaLogin import Login
        self.login = Login ()
        self.login.login.show()



"""if __name__ == '__main__':
    app = QApplication(sys.argv)
    jaja = VentanasAdmin()
    jaja.show()
    sys.exit(app.exec())"""


