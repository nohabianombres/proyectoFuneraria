import os
import copy
import sys
import functools
from PyQt5.QtWidgets import QMainWindow, QMenu, QInputDialog, QPlainTextEdit
from PyQt5 import QtWidgets
from datetime import datetime
from Front.administrador.Administrador import Ui_MainWindow
from Front.emerComunes.retorno import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QHeaderView,QListWidgetItem, QTableWidgetItem, QApplication, QMainWindow, QLineEdit, QPushButton, QWidget, QDialog, QTextEdit
from Back.gastos import Gastos
from Back.polizas import Polizas
from Back.colillas import Colillas
from Back.usuarios import Usuarios
from Back.adicionales import Adicionales
from Back.liquidacion import Liquidacion
from Back.informe import Informes
from BD.Conexion import *
from PyQt5.QtCore import QTimer

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

        self.ui.botEliUltPag.setVisible(False)


        self.session_closed = False
        self.inactivity_timer = QTimer()
        self.inactivity_timer.setInterval(300000)  # 30000 milisegundos = 30 segundos
        self.inactivity_timer.timeout.connect(self.cerrar_sesion)
        self.inactivity_timer.start()


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
        self.ui.botCreAntPol.clicked.connect(self.ventana_crear_poliza_antigua)

        self.ui.agrDocAnt.clicked.connect(self.agregar_lista_documentos_antigua)
        self.ui.agrNomAnt.clicked.connect(self.agregar_lista_nombres_antigua)
        self.ui.agrFecAnt.clicked.connect(self.agregar_lista_fechas_antigua)
        self.ui.agrParAnt.clicked.connect(self.agregar_lista_parentescos_antigua)

        self.ui.botAceCreAntPol.clicked.connect(self.funcion_crear_poliza_antigua)
        self.ui.agrDoc.clicked.connect(self.agregar_lista_documentos)
        self.ui.agrNom.clicked.connect(self.agregar_lista_nombres)
        self.ui.agrFec.clicked.connect(self.agregar_lista_fechas)
        self.ui.agrPar.clicked.connect(self.agregar_lista_parentescos)
        self.ui.botAceCrePol.clicked.connect(self.funcion_crear_poliza)
        self.ui.botAceAgrPer.clicked.connect(self.funcion_agregar_persona)
        self.ui.botAceModPol.clicked.connect(self.funcion_modificar_poliza)
        self.ui.botEliPerDat.clicked.connect(self.funcion_eliminar_persona_poliza)

        self.ui.botNomEdiCrePol.clicked.connect(self.editar_crear_nombre_poliza)
        self.ui.botDocEdiCrePol.clicked.connect(self.editar_crear_documento_poliza)
        self.ui.botFecEdiCrePol.clicked.connect(self.editar_crear_fnto_poliza)
        self.ui.botParEdiCrePol.clicked.connect(self.editar_crear_parentesco_poliza)

        self.ui.botNomEdiCreAntPol.clicked.connect(self.editar_crear_nombre_poliza_antigua)
        self.ui.botDocEdiCreAntPol.clicked.connect(self.editar_crear_documento_poliza_antigua)
        self.ui.botFecEdiCreAntPol.clicked.connect(self.editar_crear_fnto_poliza_antigua)
        self.ui.botParEdiCreAntPol.clicked.connect(self.editar_crear_parentesco_poliza_antigua)


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
        self.ui.botEliUltPag.clicked.connect(self.ventana_eliminar_ultimo_pago)


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
        self.ui.botAceBusAbo.clicked.connect(self.funcion_consultar_abonos_facturas_caja)

        self.ui.botMosCar.clicked.connect(self.venta_consultar_cartera)

        states_cities = ['Funeraria', 'Julio', 'Armando']

        menu = QMenu()
        menu.triggered.connect(lambda x: print(self.escoger_ventana_gastos(x.text())))
        self.ui.desGas.setMenu(menu)
        self.add_menu(states_cities, menu)
        self.ui.botAceGasFun.clicked.connect(self.funcion_gasto_funeraria)
        self.ui.botAceGasJef1.clicked.connect(self.funcion_gasto_jefe1)
        self.ui.botAceGasJef2.clicked.connect(self.funcion_gasto_jefe2)

        self.ui.botAceEliPag.clicked.connect(self.funcion_eliminar_ultimo_pago)
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
        self.ui.botCanGen.clicked.connect(lambda: self.clear_line_edits(self.ui.menu_generar_liquidacion))

        self.ui.botCanConFac.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_6))
        self.ui.botCanConFac.clicked.connect(lambda: self.cler_table_edits(self.ui.stackedWidget_6))
        self.ui.botCanAboFac.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_6))
        self.ui.botCanCreFac.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_6))
        self.ui.botCanCreFac.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_6))

        self.ui.botCanBusAbo.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_6))
        self.ui.botCanBusAbo.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_6))

        self.ui.botCanConPolDoc.clicked.connect(lambda: self.cler_table_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolDoc.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolDoc.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolSoc.clicked.connect(lambda: self.cler_table_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolSoc.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanConPolSoc.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))
        self.ui.botCanAgrPer.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanCrePol.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanCrePol.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))

        self.ui.botCanCreAntPol.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))
        self.ui.botCanCreAntPol.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))

        self.ui.botCanModPol.clicked.connect(lambda: self.clear_line_edits(self.ui.stackedWidget_2))
        self.ui.botCanModPol.clicked.connect(lambda: self.clear_list_edits(self.ui.stackedWidget_2))


    def clear_line_edits(self, stacked_widget):
        print('estoy en clear line edits')
        # Obtener el índice de la página actual
        current_index = stacked_widget.currentIndex()

        # Obtener el widget de la página actual
        current_widget = stacked_widget.widget(current_index)

        # Buscar todos los QLineEdits dentro del widget actual
        line_edits = current_widget.findChildren(QLineEdit)

        # Limpiar el contenido de los QLineEdits
        for line_edit in line_edits:
            line_edit.clear()

            # Buscar todos los QPlainTextEdits dentro del widget actual
        text_edits = current_widget.findChildren(QTextEdit)
        # Limpiar el contenido de los QTextEdits
        for text_edit in text_edits:
            text_edit.clear()

    def reset_inactivity_timer(self):
        # Reiniciar el temporizador
        self.inactivity_timer.stop()
        self.inactivity_timer.start()

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
        elif data == 'Julio':
            self.venta_gasto_jefe1()
        elif data == 'Armando':
            self.venta_gasto_jefe2()

    def show(self):
        self.ventanaAdmin.show()

    def ventana_polizas (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.polizas)
        self.reset_inactivity_timer()

    def ventana_colillas (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.colillas)
        self.reset_inactivity_timer()

    def ventana_gastos (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.gastos)
        self.reset_inactivity_timer()

    def ventana_usuarios (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.usuarios)
        self.reset_inactivity_timer()

    def ventana_facturas (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.facturas_caja)
        self.reset_inactivity_timer()

    def ventana_informes (self):
        self.ui.menu_admin1.setCurrentWidget(self.ui.informes)
        self.reset_inactivity_timer()

    def ventana_liquidacion(self):

        self.ui.menu_admin1.setCurrentWidget(self.ui.page_3)
        self.ui.menu_generar_liquidacion.setCurrentWidget(self.ui.generar_liquidacion)
        self.clear_line_edits(self.ui.menu_generar_liquidacion)
        self.reset_inactivity_timer()

    def ventana_consultar_poliza (self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.consultar_poliza)
        self.reset_inactivity_timer()

    def funcion_consultar_poliza_documento(self):
        poliza = Polizas ()
        ret_con_pol_doc = poliza.consultar_poliza_documento(self.ui.LDocConPol.text())
        del poliza
        print(len(ret_con_pol_doc))
        if isinstance(ret_con_pol_doc, str):
            self.crear_ventana_retorno(ret_con_pol_doc)
        else:
            if len(ret_con_pol_doc) == 1:
                print('lle')
                self.ui.LValMesPol.setText(str(ret_con_pol_doc[0][0]))
                self.ui.LDesPol.setText((ret_con_pol_doc[0][1].strftime("%Y-%m-%d")))
                self.ui.LHasPol.setText((ret_con_pol_doc[0][2].strftime("%Y-%m-%d")))
                self.ui.LSocConPol.setText(str(ret_con_pol_doc[0][7]))
                self.ui.LNotConPol.setText(str(ret_con_pol_doc[0][10]))
                self.ui.tabConPol.clearContents()
                self.ui.tabConPol.show()
                if self.ui.tabConPol != None:
                    fila = 0
                    self.ui.tabConPol.setRowCount(len(ret_con_pol_doc[0][3]))
                    i=0
                    print(len(ret_con_pol_doc[0][3]))
                    while i < len(ret_con_pol_doc[0][3]):
                        print('lle')
                        self.ui.tabConPol.setItem(i, 0, QtWidgets.QTableWidgetItem(str(ret_con_pol_doc[0][3][i])))
                        self.ui.tabConPol.setItem(i, 1, QtWidgets.QTableWidgetItem(str(ret_con_pol_doc[0][4][i])))
                        self.ui.tabConPol.setItem(i, 2, QtWidgets.QTableWidgetItem(ret_con_pol_doc[0][5][i].strftime("%Y-%m-%d")))
                        if len(ret_con_pol_doc[0][6]) > i:
                            self.ui.tabConPol.setItem(i, 3, QtWidgets.QTableWidgetItem(str(ret_con_pol_doc[0][6][i])))
                        if len(ret_con_pol_doc[0][8]) > i:
                            self.ui.tabConPol.setItem(i, 4, QtWidgets.QTableWidgetItem(ret_con_pol_doc[0][8][i].strftime("%Y-%m-%d")))
                        self.ui.tabConPol.setItem(i, 5, QtWidgets.QTableWidgetItem(str(ret_con_pol_doc[0][9][i])))

                        i = i+1
                    self.ui.tabConPol.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                    self.ui.tabConPol.horizontalHeader().setStretchLastSection(True)

                else:
                    print('no encontre')

            else:
                socios = [sublista[7] for sublista in ret_con_pol_doc]
                self.crear_ventana_retorno(socios)
                self.reset_inactivity_timer()


    def funcion_consultar_poliza(self):
        poliza = Polizas()
        ret_con_pol = poliza.consultar_poliza_socio(self.ui.LSocConPol.text())
        print(ret_con_pol)
        if isinstance(ret_con_pol, str):
            self.crear_ventana_retorno(ret_con_pol)
        else:
            self.ui.LValMesPol.setText(str(ret_con_pol[0]))
            self.ui.LDesPol.setText((ret_con_pol[1].strftime("%Y-%m-%d")))
            self.ui.LHasPol.setText((ret_con_pol[2].strftime("%Y-%m-%d")))
            self.ui.LNotConPol.setText(str(ret_con_pol[9]))
            self.ui.tabConPol.clearContents()
            self.ui.tabConPol.show()
            self.ui.tabConPol.setRowCount(len(ret_con_pol[3]))

            fila = 0
            while fila < len(ret_con_pol[3]):
                print('aca estoy')

                self.ui.tabConPol.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(ret_con_pol[3][fila])))
                self.ui.tabConPol.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(ret_con_pol[4][fila])))
                print((ret_con_pol[5][fila]))
                self.ui.tabConPol.setItem(fila, 2, QtWidgets.QTableWidgetItem(ret_con_pol[5][fila].strftime("%Y-%m-%d")))
                if len(ret_con_pol[6]) > fila:
                    self.ui.tabConPol.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(ret_con_pol[6][fila])))
                if len(ret_con_pol[7]) > fila:
                    self.ui.tabConPol.setItem(fila, 4,QtWidgets.QTableWidgetItem(ret_con_pol[7][fila].strftime("%Y-%m-%d")))

                self.ui.tabConPol.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(ret_con_pol[8][fila])))
                fila = fila + 1

            self.ui.tabConPol.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.tabConPol.horizontalHeader().setStretchLastSection(True)

        self.reset_inactivity_timer()



    def ventana_agregar_persona (self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.agregar_persona)
        self.reset_inactivity_timer()

    def funcion_agregar_persona (self):
        poliza = Polizas()
        self.fun_agr_per = poliza.agregar_persona_poliza(self.ui.LSocAgrPer.text(), self.ui.LDocAgrPer.text(), self.ui.LNomAgrPer.text(),
                                                         self.ui.LFecAgrPer.text(), self.ui.LParAgrPer.text(), self.ui.LValAgrPer.text())
        del poliza
        self.crear_ventana_retorno(self.fun_agr_per)
        self.clear_line_edits(self.ui.stackedWidget_2)
        self.reset_inactivity_timer()

    def ventana_modificar_poliza(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.modificar_poliza)
        self.reset_inactivity_timer()

    def funcion_modificar_poliza(self):
        poliza = Polizas()
        ret_con_pol = poliza.consultar_poliza_socio_mod(self.ui.LSocModPol.text())
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
            self.ui.LNotModPol.setText(str(ret_con_pol[7]))

        self.reset_inactivity_timer()

    def agregar_lista_nombres_modificar(self, nombres):
        for nombre in nombres:
            self.ui.lisNomModPol.addItem(str(nombre))
        self.reset_inactivity_timer()

    def agregar_lista_documentos_modificar(self, documentos):
        for documento in documentos:
            self.ui.lisDocModPol.addItem(str(documento))
        self.reset_inactivity_timer()

    def agregar_lista_fechas_modificar(self, fechas):
        for fecha in fechas:
            self.ui.lisFecModPol.addItem(str(fecha))
        self.reset_inactivity_timer()

    def agregar_lista_parentescos_modificar(self, parentescos):
        for parentesco in parentescos:
            self.ui.lisParModPol.addItem(str(parentesco))
        self.reset_inactivity_timer()

    def funcion_eliminar_persona_poliza(self):
        index_nom = self.ui.lisNomModPol.currentRow()

        # Verificar si hay una selección válida
        if index_nom != -1:

            poliza = Polizas()
            print('es el index')
            nombre = self.ui.lisNomModPol.item(index_nom).text()
            documento = self.ui.lisDocModPol.item(index_nom).text()
            fecha = self.ui.lisFecModPol.item(index_nom).text()
            parentesco = self.ui.lisParModPol.item(index_nom).text()
            self.ret_eli_per = poliza.eliminar_persona(self.ui.LSocModPol.text(), nombre, documento, fecha, parentesco)
            # Eliminar elemento de la lista de nombres
            self.ui.lisNomModPol.takeItem(index_nom)

            # Eliminar elemento correspondiente de la lista de documentos
            self.ui.lisDocModPol.takeItem(index_nom)

            self.ui.lisFecModPol.takeItem(index_nom)
            self.ui.lisParModPol.takeItem(index_nom)

        self.reset_inactivity_timer()



    def editar_dato_nombre_poliza(self):
        sel_items = self.ui.lisNomModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDatoAgregar.text())
        self.ui.LDatoAgregar.clear()
        self.reset_inactivity_timer()

    def editar_dato_documento_poliza(self):
        sel_items = self.ui.lisDocModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDatoAgregar.text())
        self.ui.LDatoAgregar.clear()
        self.reset_inactivity_timer()

    def editar_dato_fnto_poliza(self):
        sel_items = self.ui.lisFecModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LFechaAgregar.text())
        self.reset_inactivity_timer()


    def editar_dato_parentesco_poliza(self):
        sel_items = self.ui.lisParModPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDatoAgregar.text())
        self.ui.LDatoAgregar.clear()
        self.reset_inactivity_timer()

    def funcion_guardar_modificar_poliza(self):
        list_nom = [self.ui.lisNomModPol.item(index).text() for index in range(self.ui.lisNomModPol.count())]
        list_doc = [self.ui.lisDocModPol.item(index).text() for index in range(self.ui.lisDocModPol.count())]
        list_fec = [self.ui.lisFecModPol.item(index).text() for index in range(self.ui.lisFecModPol.count())]
        list_par = [self.ui.lisParModPol.item(index).text() for index in range(self.ui.lisParModPol.count())]
        poliza = Polizas()
        print('es la invocacion', list_nom, list_doc, list_fec, list_par)
        print(self.ui.LSocModPol.text())
        print(self.ui.LValMesModPol.text())
        self.fun_mod_pol = poliza.modificar_poliza(self.ui.LSocModPol.text(), list_nom,
                                                         list_doc,
                                                         list_fec, list_par,
                                                         self.ui.LValMesModPol.text(), self.ui.LNotModPol.toPlainText())
        self.crear_ventana_retorno(self.fun_mod_pol)
        del poliza
        print('sali de la carcel')
        self.clear_line_edits(self.ui.stackedWidget_2)
        self.clear_list_edits(self.ui.stackedWidget_2)
        self.reset_inactivity_timer()







    def ventana_crear_poliza(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.crear_poliza)
        self.reset_inactivity_timer()

    def agregar_lista_documentos(self):
        texto_documento = self.ui.LDocCrePol.text()

        # Si el campo está vacío, trátalo como una cadena vacía
        texto_documento = texto_documento if texto_documento else ''

        doc = QListWidgetItem(str(texto_documento))
        self.ui.LisDocCrePol.addItem(doc)
        self.ui.LDocCrePol.clear()
        self.reset_inactivity_timer()

    def agregar_lista_nombres(self):
        texto_nombre = self.ui.LNomCrePol.text()
        texto_nombre = texto_nombre if texto_nombre else ''

        nom = QListWidgetItem(str(texto_nombre))
        self.ui.LisNomCrePol.addItem(nom)
        self.ui.LNomCrePol.clear()
        self.reset_inactivity_timer()

    def agregar_lista_parentescos(self):
        texto_parentesco = self.ui.LParCrePol.text()
        texto_parentesco = texto_parentesco if texto_parentesco else ''

        par = QListWidgetItem(str(texto_parentesco))
        self.ui.LisParCrePol.addItem(par)
        self.ui.LParCrePol.clear()
        self.reset_inactivity_timer()

    def agregar_lista_fechas(self):
        texto_fecha = self.ui.LFecCrePol.text()
        texto_fecha = texto_fecha if texto_fecha else ''

        fec = QListWidgetItem(str(texto_fecha))
        self.ui.LisFecCrePol.addItem(fec)
        self.reset_inactivity_timer()

    def funcion_crear_poliza (self):
        list_nom = [self.ui.LisNomCrePol.item(index).text() for index in range(self.ui.LisNomCrePol.count())]
        list_doc = [self.ui.LisDocCrePol.item(index).text() for index in range(self.ui.LisDocCrePol.count())]
        list_fec = [self.ui.LisFecCrePol.item(index).text() for index in range(self.ui.LisFecCrePol.count())]
        list_par = [self.ui.LisParCrePol.item(index).text() for index in range(self.ui.LisParCrePol.count())]
        poliza = Polizas()
        self.reset_inactivity_timer()

        print('error en la funcion')
        self.fun_cre_pol = poliza.crear_poliza(self.ui.LSocCrePol.text(), list_nom, list_doc,
                                               list_fec, list_par, self.ui.LValCrePol.text(),
                                                  self.ui.LNumCrePol.text(), self.usuario[2],self.ui.LNotCrePol.toPlainText())
        print('el error esta en la devuelta')
        self.crear_ventana_retorno(self.fun_cre_pol)


        del poliza

        self.clear_line_edits(self.ui.stackedWidget_2)
        self.clear_list_edits(self.ui.stackedWidget_2)
        self.reset_inactivity_timer()





    def editar_crear_nombre_poliza(self):
        sel_items = self.ui.LisNomCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LNomCrePol.text())
        self.ui.LNomCrePol.clear()
        self.reset_inactivity_timer()

    def editar_crear_documento_poliza(self):
        sel_items = self.ui.LisDocCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDocCrePol.text())
        self.ui.LDocCrePol.clear()
        self.reset_inactivity_timer()

    def editar_crear_fnto_poliza(self):
        sel_items = self.ui.LisFecCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LFecCrePol.text())

        self.reset_inactivity_timer()


    def editar_crear_parentesco_poliza(self):
        sel_items = self.ui.LisParCrePol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LParCrePol.text())
        self.ui.LParCrePol.clear()
        self.reset_inactivity_timer()




















    def ventana_crear_poliza_antigua(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.crear_antigua)
        self.reset_inactivity_timer()

    def agregar_lista_documentos_antigua(self):
        texto_documento = self.ui.LDocCreAntPol.text()

        # Si el campo está vacío, trátalo como una cadena vacía
        texto_documento = texto_documento if texto_documento else ''

        doc = QListWidgetItem(str(texto_documento))
        self.ui.LisDocCreAntPol.addItem(doc)
        self.ui.LDocCreAntPol.clear()
        self.reset_inactivity_timer()

    def agregar_lista_nombres_antigua(self):
        texto_nombre = self.ui.LNomCreAntPol.text()
        texto_nombre = texto_nombre if texto_nombre else ''

        nom = QListWidgetItem(str(texto_nombre))
        self.ui.LisNomCreAntPol.addItem(nom)
        self.ui.LNomCreAntPol.clear()
        self.reset_inactivity_timer()

    def agregar_lista_parentescos_antigua(self):
        texto_parentesco = self.ui.LParCreAntPol.text()
        texto_parentesco = texto_parentesco if texto_parentesco else ''

        par = QListWidgetItem(str(texto_parentesco))
        self.ui.LisParCreAntPol.addItem(par)
        self.ui.LParCreAntPol.clear()
        self.reset_inactivity_timer()

    def agregar_lista_fechas_antigua(self):
        texto_fecha = self.ui.LFecCreAntPol.text()
        texto_fecha = texto_fecha if texto_fecha else ''

        fec = QListWidgetItem(str(texto_fecha))
        self.ui.LisFecCreAntPol.addItem(fec)
        self.reset_inactivity_timer()

    def funcion_crear_poliza_antigua(self):
        list_nom = [self.ui.LisNomCreAntPol.item(index).text() for index in range(self.ui.LisNomCreAntPol.count())]
        list_doc = [self.ui.LisDocCreAntPol.item(index).text() for index in range(self.ui.LisDocCreAntPol.count())]
        list_fec = [self.ui.LisFecCreAntPol.item(index).text() for index in range(self.ui.LisFecCreAntPol.count())]
        list_par = [self.ui.LisParCreAntPol.item(index).text() for index in range(self.ui.LisParCreAntPol.count())]
        poliza = Polizas()

        print('error en la funcion')
        self.fun_cre_pol_ant = poliza.crear_poliza_antigua(self.ui.LSocCreAntPol.text(), list_nom, list_doc,
                                               list_fec, list_par, self.ui.LValCreAntPol.text(),
                                                  self.ui.LNumCreAntPol.text(), self.usuario[2], self.ui.LFecDesCreAntPol.text(), self.ui.LFecAfiCreAntPol.text() ,self.ui.LNotCrePolAnt.toPlainText())
        print('el error esta en la devuelta')
        self.crear_ventana_retorno(self.fun_cre_pol_ant)


        del poliza

        self.clear_line_edits(self.ui.stackedWidget_2)
        self.clear_list_edits(self.ui.stackedWidget_2)
        self.reset_inactivity_timer()





    def editar_crear_nombre_poliza_antigua(self):
        sel_items = self.ui.LisNomCreAntPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LNomCreAntPol.text())
        self.ui.LNomCreAntPol.clear()
        self.reset_inactivity_timer()

    def editar_crear_documento_poliza_antigua(self):
        sel_items = self.ui.LisDocCreAntPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LDocCreAntPol.text())
        self.ui.LDocCreAntPol.clear()
        self.reset_inactivity_timer()

    def editar_crear_fnto_poliza_antigua(self):
        sel_items = self.ui.LisFecCreAntPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LFecCreAntPol.text())

        self.reset_inactivity_timer()


    def editar_crear_parentesco_poliza_antigua(self):
        sel_items = self.ui.LisParCreAntPol.selectedItems()

        for item in sel_items:
            item.setText(self.ui.LParCreAntPol.text())
        self.ui.LParCreAntPol.clear()

        self.reset_inactivity_timer()
















    def crear_ventana_retorno(self, retorno):

        self.ventana_emergente = EmerRetorno ()
        self.ventana_emergente.emerRetorno.show()
        self.ventana_emergente.imprimir_retorno(str(retorno))
        self.reset_inactivity_timer()

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
                self.ui.tableWidget.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(self.fun_ult_pag_soc[7][0])))
                self.ui.tableWidget.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(self.fun_ult_pag_soc[6][0])))
                self.ui.tableWidget.setItem(fila, 4,
                                            QtWidgets.QTableWidgetItem(self.fun_ult_pag_soc[2].strftime("%Y-%m-%d")))
                self.ui.tableWidget.setItem(fila, 5,
                                            QtWidgets.QTableWidgetItem(self.fun_ult_pag_soc[3].strftime("%Y-%m-%d")))
                self.ui.tableWidget.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(self.fun_ult_pag_soc[4])))
                self.ui.tableWidget.setItem(fila, 7,
                                            QtWidgets.QTableWidgetItem(self.fun_ult_pag_soc[5].strftime("%Y-%m-%d")))

                # Ajuste automático del ancho de las columnas
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

            else:
                print('No se encontró ninguna póliza')

        self.reset_inactivity_timer()


    def ventana_ultimo_pago_documento(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.buscar_colilla_documento)
        self.reset_inactivity_timer()

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
                    self.ui.tableWidget_2.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[7][0])))
                    self.ui.tableWidget_2.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[6][0])))
                    self.ui.tableWidget_2.setItem(fila, 4, QtWidgets.QTableWidgetItem( elementos[2].strftime("%Y-%m-%d")))
                    self.ui.tableWidget_2.setItem(fila, 5, QtWidgets.QTableWidgetItem(elementos[3].strftime("%Y-%m-%d")))
                    self.ui.tableWidget_2.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[4])))
                    self.ui.tableWidget_2.setItem(fila, 7, QtWidgets.QTableWidgetItem(elementos[5].strftime("%Y-%m-%d")))
                    fila = fila + 1
                self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.ui.tableWidget_2.horizontalHeader().setStretchLastSection(True)
            else:
                print('no encontre')
        self.reset_inactivity_timer()


    def ventana_crear_colilla(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.crear_colilla)
        self.reset_inactivity_timer()

    def funcion_crear_colilla (self):
        colilla = Colillas()
        self.fun_cre_col = colilla.crear_colilla_socio(self.ui.LSocCreCol.text(), self.ui.LNumCreCol.text(), self.usuario[2])
        del colilla
        self.clear_line_edits(self.ui.stackedWidget_3)
        self.crear_ventana_retorno(self.fun_cre_col)
        self.reset_inactivity_timer()



    def ventana_eliminar_ultimo_pago(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.eliminar_pago)
        self.reset_inactivity_timer()

    def funcion_eliminar_ultimo_pago (self):
        colilla = Colillas()
        self.fun_eli_pag = colilla.eliminar_ultimo_pago(self.ui.LSocEliPag.text())
        del colilla
        self.clear_line_edits(self.ui.stackedWidget_3)
        self.crear_ventana_retorno(self.fun_eli_pag)
        self.reset_inactivity_timer()





    def venta_gasto_jefe1 (self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.gasto_jefe1)
        self.reset_inactivity_timer()

    def funcion_gasto_jefe1 (self):
        gasto = Gastos ()
        ret_fun_gas_jef1 = gasto.gasto_jefe1(self.ui.LGasJef1.text() ,self.ui.LValJef1Gas.text(), 'julio')
        del gasto
        self.clear_line_edits(self.ui.stackedWidget_4)
        self.crear_ventana_retorno(ret_fun_gas_jef1)
        self.reset_inactivity_timer()

    def venta_gasto_jefe2 (self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.gasto_jefe2)
        self.reset_inactivity_timer()

    def funcion_gasto_jefe2 (self):
        gasto = Gastos ()
        print(self.ui.LGasJef2.text())
        ret_fun_gas_jef2 = gasto.gasto_jefe2(self.ui.LGasJef2.text(), self.ui.LValJef2Gas.text(), 'armando')
        del gasto
        self.clear_line_edits(self.ui.stackedWidget_4)
        self.crear_ventana_retorno(ret_fun_gas_jef2)
        self.reset_inactivity_timer()


    def venta_gasto_funeraria (self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.gasto_funeraria)
        self.reset_inactivity_timer()

    def funcion_gasto_funeraria (self):
        gasto = Gastos ()
        ret_fun_gas_fun = gasto.gasto_funeraria(self.ui.LGasFun.text(), self.ui.LValFunGas.text(), 'funeraria')
        del gasto
        self.clear_line_edits(self.ui.stackedWidget_4)
        self.crear_ventana_retorno(ret_fun_gas_fun)
        self.reset_inactivity_timer()

    def venta_revisar_gastos(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.revisar_gastos)
        self.funcion_revisar_gastos()
        self.reset_inactivity_timer()

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

            self.ui.tabla_gastos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.tabla_gastos.horizontalHeader().setStretchLastSection(True)

        else:
            print('no encontré')

        self.reset_inactivity_timer()

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

        self.reset_inactivity_timer()

    def venta_crear_usuario (self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.crear_usuario)
        self.reset_inactivity_timer()

    def funcion_crear_usuario (self):
        usuario = Usuarios ()
        cargo = self.ui.LCarCreUsu.currentText()
        self.ret_fun_cre_usu = usuario.crear_usuario(self.ui.LConCreUsu.text(), self.ui.LNomCreUsu.text(), self.ui.LDocCreUsu.text(), cargo)
        del usuario
        self.clear_line_edits(self.ui.stackedWidget_5)
        self.crear_ventana_retorno(self.ret_fun_cre_usu)
        self.reset_inactivity_timer()

    def venta_eliminar_usuario (self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.eliminar_usuario)
        self.reset_inactivity_timer()

    def funcion_eliminar_usuario (self):
        usuario = Usuarios ()
        self.ret_eli_usu = usuario.eliminar_usuario(self.ui.LIdEliUsu.text())
        del usuario
        self.clear_line_edits(self.ui.stackedWidget_5)
        self.crear_ventana_retorno(self.ret_eli_usu)
        self.reset_inactivity_timer()


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
                    print(elementos[0])
                    print(elementos[1])
                    self.ui.tabMosTod.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                    self.ui.tabMosTod.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                    self.ui.tabMosTod.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                    self.ui.tabMosTod.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                    fila = fila + 1

                self.ui.tabMosTod.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.ui.tabMosTod.horizontalHeader().setStretchLastSection(True)
            else:
                print('no encontre')

        self.reset_inactivity_timer()





    def venta_crear_factura(self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.crear_caja)
        self.reset_inactivity_timer()

    def funcion_crear_factura_caja (self):
        lis_des = [self.ui.lisDes.item(index).text() for index in range(self.ui.lisDes.count())]
        lis_can = [self.ui.lisCan.item(index).text() for index in range(self.ui.lisCan.count())]
        lis_val = [self.ui.lisVal.item(index).text() for index in range(self.ui.lisVal.count())]
        factura = Adicionales ()
        ret_fun_cre_fac = factura.crear_factura_caja(self.ui.LCiuCreFac.text(), self.ui.LNomCreFac.text(), self.ui.LDocCreFac.text(), lis_des, lis_can, lis_val, self.usuario[2], self.ui.LValAboCreFac.text(), self.ui.LNotCreFac.toPlainText())
        del factura
        self.clear_line_edits(self.ui.stackedWidget_6)
        self.clear_list_edits(self.ui.stackedWidget_6)
        self.crear_ventana_retorno(ret_fun_cre_fac)
        self.reset_inactivity_timer()


    def agregar_lista_descripciones(self):
        des = QListWidgetItem(str(self.ui.LDesCreFac.text()))
        self.ui.lisDes.addItem(des)
        self.ui.LDesCreFac.clear()
        self.reset_inactivity_timer()

    def agregar_lista_cantidades(self):
        can = QListWidgetItem(self.ui.LCanCreFac.text())
        self.ui.lisCan.addItem(can)
        self.ui.LCanCreFac.clear()
        self.reset_inactivity_timer()

    def agregar_lista_valores(self):
        val = QListWidgetItem(self.ui.LValCreFac.text())
        self.ui.lisVal.addItem(val)
        self.ui.LValCreFac.clear()
        self.reset_inactivity_timer()



    def venta_consultar_cartera (self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.mostrar_cartera)
        self.funcion_consultar_cartera()

    def funcion_consultar_cartera (self):
        adicionales = Adicionales ()
        ret_con_car = adicionales.mostrar_cartera()
        del adicionales
        self.ui.tabMosCar.clearContents()
        self.ui.tabMosCar.show()
        if ret_con_car != None:
            fila = 0
            self.ui.tabMosCar.setRowCount(len(ret_con_car))
            for elementos in ret_con_car:
                if isinstance(elementos[5], list):
                    descripciones = ", ".join(map(str, elementos[5]))
                else:
                    descripciones = elementos[5]
                print(elementos)
                self.ui.tabMosCar.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.ui.tabMosCar.setItem(fila, 1, QtWidgets.QTableWidgetItem((elementos[1]).strftime("%Y-%m-%d")))
                self.ui.tabMosCar.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.ui.tabMosCar.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.ui.tabMosCar.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.ui.tabMosCar.setItem(fila, 5, QtWidgets.QTableWidgetItem(descripciones))
                self.ui.tabMosCar.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.ui.tabMosCar.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))

                fila = fila + 1

            self.ui.tabMosCar.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.tabMosCar.horizontalHeader().setStretchLastSection(True)

        else:
            print('no encontre')

        self.reset_inactivity_timer()






    def venta_abonar_caja (self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.abonar_caja)
        self.reset_inactivity_timer()

    def funcion_abonar_factura_caja (self):
        facturas = Adicionales ()
        ret_abo_fac_caj = facturas.abonar_factura_caja(self.ui.LIdFacAbo.text(), self.ui.LPreAbo.text(),self.usuario[2])
        del facturas
        self.clear_line_edits(self.ui.stackedWidget_6)
        self.crear_ventana_retorno(ret_abo_fac_caj)
        self.reset_inactivity_timer()


    def venta_consultar_factura (self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.consultar_caja)
        self.reset_inactivity_timer()

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
                    self.ui.LNotConFac.setText(str(elementos[6]))
                    self.ui.tabConFac.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                    self.ui.tabConFac.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[2])))
                    self.ui.tabConFac.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[3])))
                    self.ui.tabConFac.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[-3])))
                    self.ui.tabConFac.setItem(fila, 4, QtWidgets.QTableWidgetItem((elementos[-2].strftime("%Y-%m-%d"))))
                    fila = fila + 1

                self.ui.tabConFac.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.ui.tabConFac.horizontalHeader().setStretchLastSection(True)
            else:
                print('no encontre')

        self.reset_inactivity_timer()

    def funcion_consultar_abonos_facturas_caja(self):
        facturas = Adicionales()
        ret_con_abo = facturas.consultar_abonos_facturas_documento(self.ui.LDocComAbo.text())
        del facturas
        if isinstance(ret_con_abo, str):
                self.crear_ventana_retorno(ret_con_abo)
        else:
                print(ret_con_abo[0])

                self.ui.tabConAbo.clearContents()
                self.ui.tabConAbo.show()

                fila = 0
                self.ui.tabConAbo.setRowCount(len(ret_con_abo[0]))
                for elementos in ret_con_abo:
                        self.ui.tabConAbo.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                        self.ui.tabConAbo.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                        self.ui.tabConAbo.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                        self.ui.tabConAbo.setItem(fila, 3,
                                                  QtWidgets.QTableWidgetItem((elementos[3].strftime("%Y-%m-%d"))))
                        self.ui.tabConAbo.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))

                        self.ui.tabConAbo.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                        fila = fila + 1

                self.ui.tabConAbo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.ui.tabConAbo.horizontalHeader().setStretchLastSection(True)

                self.reset_inactivity_timer()








    def funcion_generar_liquidacion(self):
        liquidacion = Liquidacion()
        self.ret_gen_liq = liquidacion.generar_liquidacion(self.ui.LIdJef1Gen.text(),self.ui.LIdJef2Gen.text(),self.ui.LConJef1Gen.text(),self.ui.LConJef2Gen.text())
        self.venta_liquidacion_generada(self.ret_gen_liq)
        self.reset_inactivity_timer()

    def venta_liquidacion_generada (self,datos_liquidacion):

        if isinstance(datos_liquidacion, str):
            self.crear_ventana_retorno(datos_liquidacion)
            self.clear_line_edits(self.ui.menu_generar_liquidacion)

        else:
            self.ui.menu_generar_liquidacion.setCurrentWidget(self.ui.liquidacion_generada)
            self.liquidacion_generada(datos_liquidacion)

        self.reset_inactivity_timer()

    def liquidacion_generada(self,ret_gen_liq):
        self.ui.LGasJef1Tot.setText(str(ret_gen_liq[0]))
        self.ui.LGasJef2Tot.setText(str(ret_gen_liq[1]))
        self.ui.LSalJef1Tot.setText(str(ret_gen_liq[2]))
        self.ui.LSalJef2Tot.setText(str(ret_gen_liq[3]))
        self.reset_inactivity_timer()


    def venta_ultimo_saldo(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.ultimo_saldo)
        self.funcion_consultar_informe_ultimo_saldo()
        self.reset_inactivity_timer()

    def venta_informe_saldos(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.saldo_informe)
        self.funcion_consultar_informe_saldo()
        self.reset_inactivity_timer()

    def venta_informe_colillas(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.colillas_informe)
        self.funcion_consultar_informe_colillas()
        self.reset_inactivity_timer()

    def venta_informe_gastos(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.gastos_informe)
        self.funcion_consultar_informe_gastos()
        self.reset_inactivity_timer()

    def venta_informe_facturas(self):
        self.ui.menu_admin2.setCurrentWidget(self.ui.factura_caja_informe)
        self.funcion_consultar_informe_facturas()
        self.reset_inactivity_timer()




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
                if isinstance(elementos[2], list):
                    descripciones = ", ".join(map(str, elementos[2]))
                else:
                    descripciones = elementos[2]
                print(elementos[1])
                self.ui.tabInfSal.setItem(fila, 0, QtWidgets.QTableWidgetItem(elementos[3].strftime("%Y-%m-%d")))
                self.ui.tabInfSal.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.ui.tabInfSal.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.ui.tabInfSal.setItem(fila, 3, QtWidgets.QTableWidgetItem(descripciones))
                self.ui.tabInfSal.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.ui.tabInfSal.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.ui.tabInfSal.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.ui.tabInfSal.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                fila = fila + 1

            self.ui.tabInfSal.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.tabInfSal.horizontalHeader().setStretchLastSection(True)

        else:
            print('no encontre')

        self.reset_inactivity_timer()

    def funcion_consultar_informe_colillas(self):
        informe = Informes()
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
                fila += 1

            self.ui.tabCol.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.tabCol.horizontalHeader().setStretchLastSection(True)

        else:
            print('no encontre')

        self.reset_inactivity_timer()

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
                self.ui.tabFac.setItem(fila, 1, QtWidgets.QTableWidgetItem((elementos[5]).strftime("%Y-%m-%d")))
                self.ui.tabFac.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.ui.tabFac.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.ui.tabFac.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.ui.tabFac.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[4])))

                fila = fila + 1

            self.ui.tabFac.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.tabFac.horizontalHeader().setStretchLastSection(True)

        else:
            print('no encontre')

        self.reset_inactivity_timer()

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

            self.ui.tabGas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.ui.tabGas.horizontalHeader().setStretchLastSection(True)

        else:
            print('no encontre')

        self.reset_inactivity_timer()

    def funcion_consultar_informe_ultimo_saldo(self):
        informe = Informes ()
        self.ret_fun_con_ult_sal = informe.mostrar_ultimo_saldo()
        del informe
        self.ui.tabUltSal.clearContents()
        self.ui.tabUltSal.show()
        self.ui.tabUltSal.setRowCount(1)

        if self.ret_fun_con_ult_sal is not None:
            print('voy a imprimir')
            try:
                if isinstance(self.ret_fun_con_ult_sal[2], list):
                    descripciones = ", ".join(map(str, self.ret_fun_con_ult_sal[2]))
                else:
                    descripciones = self.ret_fun_con_ult_sal[2]
                fila = 0
                self.ui.tabUltSal.setItem(fila, 0, QtWidgets.QTableWidgetItem(self.ret_fun_con_ult_sal[3].strftime("%Y-%m-%d")))
                self.ui.tabUltSal.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(self.ret_fun_con_ult_sal[0])))
                self.ui.tabUltSal.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(self.ret_fun_con_ult_sal[1])))
                self.ui.tabUltSal.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(descripciones)))
                self.ui.tabUltSal.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(self.ret_fun_con_ult_sal[4])))
                self.ui.tabUltSal.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(self.ret_fun_con_ult_sal[5])))
                self.ui.tabUltSal.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(self.ret_fun_con_ult_sal[6])))
                self.ui.tabUltSal.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(self.ret_fun_con_ult_sal[7])))
                self.ui.tabUltSal.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.ui.tabUltSal.horizontalHeader().setStretchLastSection(True)
            except psycopg2.Error as e:
                print(e)
        else:
            print('No se encontró ninguna póliza')

        self.reset_inactivity_timer()

    def generar_backup(self):
        basedatos.crear_copia_seguridad()
        self.reset_inactivity_timer()

    def recibir_datos(self, datos_usuario):
        self.usuario = datos_usuario
        self.ui.Nombre_usuario_2.setText(str(datos_usuario[2]))
        self.ui.Documento.setText(str(datos_usuario[3]))
        self.ui.conexion.setText('conexion exitosa')


    def cerrar_sesion(self):
        if not self.session_closed:
            self.session_closed = True
            self.ventanaAdmin.close()
            from Front.VentanaLogin import Login
            self.login = Login()
            self.login.login.show()



"""if __name__ == '__main__':
    app = QApplication(sys.argv)
    jaja = VentanasAdmin()
    jaja.show()
    sys.exit(app.exec())"""


