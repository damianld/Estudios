import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk,Gtk
import XestionDatos
import BDProvinciasLocalidades
import informes
import servicios
import time
from os.path import abspath, dirname, join
WHERE_AM_I = abspath(dirname(__file__))
#Colocar no readme o user:pass
#grabar ejemplo

class Restaurante:
    def __init__(self):
        int_visual = Gtk.Builder()
        int_visual.add_from_file("Restaurante.glade")
        self.set_style()
        self.vent_principal = int_visual.get_object("vent_principal")
        self.ven_about = int_visual.get_object("ven_about")
        self.ven_about.connect('delete-event', lambda w, e: w.hide() or True)
        self.tree_mesa = int_visual.get_object("tree_mesa")
        self.sair_barra = int_visual.get_object("sair_barra")
        self.listCliente = int_visual.get_object("listCliente")
        self.listMesa = int_visual.get_object("listMesa")
        self.i_mesa1 = int_visual.get_object("Mesa1")
        self.i_mesa2 = int_visual.get_object("Mesa2")
        self.i_mesa3 = int_visual.get_object("Mesa3")
        self.i_mesa4 = int_visual.get_object("Mesa4")
        self.i_mesa5 = int_visual.get_object("Mesa5")
        self.i_mesa6 = int_visual.get_object("Mesa6")
        self.i_mesa7 = int_visual.get_object("Mesa7")
        self.i_mesa8 = int_visual.get_object("Mesa8")
        self.listaMesas = int_visual.get_object("listaMesas")
        self.combo_provincia = int_visual.get_object("combo_provincia")
        self.combo_localidade = int_visual.get_object("combo_localidade")
        self.ven_login = int_visual.get_object("ven_login")
        self.ent_usuario = int_visual.get_object("ent_usuario")
        self.ent_contrasinal = int_visual.get_object("ent_contrasinal")
        self.but_login = int_visual.get_object("but_login")
        self.but_alta_cliente = int_visual.get_object("but_alta_cliente")
        self.but_baixa_cliente = int_visual.get_object("but_baixa_cliente")
        self.but_mod_cliente = int_visual.get_object("but_mod_cliente")
        self.tex_dni = int_visual.get_object("tex_dni")
        self.tex_nome = int_visual.get_object("tex_nome")
        self.tex_apelidos = int_visual.get_object("tex_apelidos")
        self.tex_direccion = int_visual.get_object("tex_direccion")
        self.tree_clientes = int_visual.get_object("tree_clientes")
        self.limpacaixas_cliente()
        self.combo_Cliente = int_visual.get_object("combo_Cliente")
        self.combo_Mesa = int_visual.get_object("combo_Mesa")
        self.combo_Camareiro = int_visual.get_object("combo_Camareiro")
        self.tree_Facturas = int_visual.get_object("tree_Facturas")
        self.list_Facturas = int_visual.get_object("list_Facturas")
        self.but_creaFactura = int_visual.get_object("but_creaFactura")
        self.but_pagar =int_visual.get_object("but_pagar")
        self.listServicio = int_visual.get_object("listServicio")
        self.tree_Servicios = int_visual.get_object("tree_Servicios")
        self.combo_facturas = int_visual.get_object("combo_facturas")
        self.combo_servicios = int_visual.get_object("combo_servicios")
        self.cantidade = int_visual.get_object("cantidade")
        self.cantidade.set_text("0")
        self.but_lineaFactura = int_visual.get_object("but_lineaFactura")
        self.but_novo_servicio = int_visual.get_object("but_novo_servicio")
        self.barra_error = int_visual.get_object("gtk_error")
        self.ven_Servicios = int_visual.get_object("ven_Servicios")
        self.ven_Servicios.connect('delete-event', lambda w, e: w.hide() or True)
        self.ven_Avisos = int_visual.get_object("ven_Avisos")
        self.ven_Avisos.connect('delete-event', lambda w, e: w.hide() or True)
        self.but_sair_total = int_visual.get_object("but_sair_total")
        self.but_sair_servizos= int_visual.get_object("but_sair_servicio")
        self.list_Ser = int_visual.get_object("list_Ser")
        self.but_add_servicio = int_visual.get_object("but_add_servicio")
        self.ent_producto_servicio = int_visual.get_object("ent_producto_servicio")
        self.ent_precio_servicio = int_visual.get_object("ent_precio_servicio")
        self.ent_producto_servicio.set_text("")
        self.ent_precio_servicio.set_text("")
        self.lbl_error = int_visual.get_object("lbl_Error")
        self.but_copiaSeguridade = int_visual.get_object("but_copiaSeguridade")
        self.but_creaFactura_simple = int_visual.get_object("but_creaFactura_simple")
        """

            Diccionario de eventos.

        """
        dic = {
            'on_vent_principal_destroy': self.sair,
            'on_ven_login_destroy': self.sair,
            'on_sair_activate': self.sair,
            'on_sair_barra_clicked': self.sair,
            'on_selector_mesa_changed': self.seleccionar_mesa,
            'on_selector_factura_changed': self.seleccionar_Factura,
            'on_selector_clientes_changed': self.cargandodatos_clientes,
            'on_boton1_clicked': self.click_mesa_1,
            'on_boton2_clicked': self.click_mesa_2,
            'on_boton3_clicked': self.click_mesa_3,
            'on_boton4_clicked': self.click_mesa_4,
            'on_boton5_clicked': self.click_mesa_5,
            'on_boton6_clicked': self.click_mesa_6,
            'on_boton7_clicked': self.click_mesa_7,
            'on_boton8_clicked': self.click_mesa_8,
            'on_combo_provincia_changed': self.seleccion_provincia,
            'on_but_login_clicked': self.login,
            'on_but_ocupar_clicked': self.ocupar,
            'on_but_baleirar_clicked': self.baleirar,
            'on_but_about_activate': self.show_about,
            'on_but_imprimir_clicked': self.probaImpresion,
            'on_but_creaFactura_simple_clicked': self.probaImpresion2,
            'on_but_alta_cliente_clicked': self.alta_cliente,
            'on_but_baixa_cliente_clicked': self.baixa_cliente,
            'on_but_mod_cliente_clicked': self.mod_cliente,
            'on_but_creaFactura_clicked': self.crear_factura,
            'on_but_pagar_clicked': self.pagarfactura,
            'on_but_lineaFactura_clicked': self.crear_fFactura,
            'on_combo_facturas_changed': self.buscar_fFactura,
            'on_gtk_error_activate': self.mostrar_venAvisos,
            'on_but_novo_servicio_clicked': self.mostrar_novoServicio,
            'on_but_sair_total_clicked': self.sair,
            'on_but_sair_servicio_clicked': self.pecharVenta,
            'on_but_add_servicio_clicked': self.crear_plato,
            'on_but_error_clicked': self.sair_error,
            'on_but_copiaSeguridade_activate': self.creaCopia

        }
        int_visual.connect_signals(dic)
        self.vent_principal.hide()
        self.actualizar_listas()
        self.ven_login.show()
        self.pagouse=None

    def set_style(self):
        """
            # Método de carga la paleta CSS
        """
        provider = Gtk.CssProvider()
        provider.load_from_path(join(WHERE_AM_I, 'estilo.css'))
        screen = Gdk.Display.get_default_screen(Gdk.Display.get_default())
        GTK_STYLE_PROVIDER_PRIORITY_APPLICATION = 600
        Gtk.StyleContext.add_provider_for_screen(
            screen, provider,
            GTK_STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def login(self, widget):
        """

            Método de control do login.

        """
        if XestionDatos.login(self.ent_usuario.get_text(), self.ent_contrasinal.get_text(), self.ven_login):
            self.actualizar_mesas()
            self.vent_principal.show()
            #self.vent_principal.maximize()
            BDProvinciasLocalidades.cargar_provincias(self.combo_provincia)
            self.actualizar_listas()



    def ocupar_mesa_P(self, imaxemesa):
        """

            Metodo de asignación das imaxes de Ocupado das mesas dos botóns pequenos.

        """
        imaxemesa.set_from_file("Imaxes/MesaPequenaOcuoada.png")

    def ocupar_mesa_M(self, imaxemesa):
        """

            Metodo de asignación das imaxes de Ocupado das mesas dos botóns medianos.

        """
        imaxemesa.set_from_file("Imaxes/MesaMediaOcupada.png")

    def ocupar_mesa_G(self, imaxemesa):
        """

            Metodo de asignación das imaxes de Ocupado das mesas dos botóns grandes.

        """
        imaxemesa.set_from_file("Imaxes/MesaGrandeOcupada.png")

    def liberar_mesa_P(self, imaxemesa):
        """

            Metodo de asignación das imaxes de Libre das mesas dos botóns pequenos.

        """
        imaxemesa.set_from_file("Imaxes/MesaPequena.png")

    def liberar_mesa_M(self, imaxemesa):
        """

            Metodo de asignación das imaxes de Libre das mesas dos botóns medianos.

        """
        imaxemesa.set_from_file("Imaxes/Mesa8.png")

    def liberar_mesa_G(self, imaxemesa):
        """

            Metodo de asignación das imaxes de Libre das mesas dos botóns grandes.

        """
        imaxemesa.set_from_file("Imaxes/Mesa10.png")



    def click_mesa_1(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 1.

        """
        self.listaMesas.set_active(1)
        self.combo_Mesa.set_active(0)

    def click_mesa_2(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 2.

        """
        self.listaMesas.set_active(2)
        self.combo_Mesa.set_active(1)

    def click_mesa_3(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 3.

        """
        self.listaMesas.set_active(3)
        self.combo_Mesa.set_active(2)

    def click_mesa_4(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 4.

        """
        self.listaMesas.set_active(4)
        self.combo_Mesa.set_active(3)

    def click_mesa_5(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 5.

        """
        self.listaMesas.set_active(5)
        self.combo_Mesa.set_active(4)

    def click_mesa_6(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 6.

        """
        self.listaMesas.set_active(6)
        self.combo_Mesa.set_active(5)

    def click_mesa_7(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 7.

        """
        self.listaMesas.set_active(7)
        self.combo_Mesa.set_active(6)

    def click_mesa_8(self, widget):
        """

             Metodo para o lanzado de eventos do botón da mesa 8.

        """
        self.listaMesas.set_active(8)
        self.combo_Mesa.set_active(7)

    def sair(self,widget):
        """

            Metodo para a finalización do programa.

        """
        XestionDatos.pechar_conexion()
        BDProvinciasLocalidades.pechar_conexion()
        Gtk.main_quit()

    def actualizar_listas(self):
        """

            Metodo para a actualización de todalas listas de datos(ListViews) do programa.

        """
        self.listServicio.clear()
        lista1 = XestionDatos.consultar_servicio()
        for registro1 in lista1:
            self.listServicio.append(registro1)
        self.listCliente.clear()
        lista2 = XestionDatos.consultar_cliente()
        for registro2 in lista2:
            self.listCliente.append(registro2)
        self.listMesa.clear()
        lista3 = XestionDatos.consultar_mesas()
        for registro3 in lista3:
            self.listMesa.append(registro3)
        self.list_Facturas.clear()
        lista4 = XestionDatos.consultar_facturas()
        for registro4 in lista4:
            self.list_Facturas.append(registro4)
        self.list_Ser.clear()
        lista5 = XestionDatos.consultar_plato()
        for registro5 in lista5:
            self.list_Ser.append(registro5)
        self.combo_facturas.remove_all()
        self.combo_servicios.remove_all()
        self.combo_Mesa.remove_all()
        self.combo_Camareiro.remove_all()
        self.combo_Cliente.remove_all()
        XestionDatos.cargar_clientes(self.combo_Cliente)
        XestionDatos.cargar_mesa(self.combo_Mesa)
        XestionDatos.cargar_camareiro(self.combo_Camareiro)
        XestionDatos.cargar_facturas_activas(self.combo_facturas)
        XestionDatos.cargar_servicios(self.combo_servicios)

    def show_about(self, widget):
        """

            Método de ocultación da ventana de About.

        """
        self.ven_about.show()

    def actualizar_mesas(self):
        """

            Metodo para a actualización automática dos iconos dos botóns das mesas.

        """
        listaMesas = XestionDatos.consultar_mesas()
        for columna in listaMesas:
            if columna[0] == "1" and columna[2] == "True":
                self.ocupar_mesa_P(self.i_mesa1)
            elif columna[0] == "2" and columna[2] == "True":
                self.ocupar_mesa_P(self.i_mesa2)
            elif columna[0] == "3" and columna[2] == "True":
                self.ocupar_mesa_M(self.i_mesa3)
            elif columna[0] == "4" and columna[2] == "True":
                self.ocupar_mesa_P(self.i_mesa4)
            elif columna[0] == "5" and columna[2] == "True":
                self.ocupar_mesa_P(self.i_mesa5)
            elif columna[0] == "6" and columna[2] == "True":
                self.ocupar_mesa_M(self.i_mesa6)
            elif columna[0] == "7" and columna[2] == "True":
                self.ocupar_mesa_G(self.i_mesa7)
            elif columna[0] == "8" and columna[2] == "True":
                self.ocupar_mesa_G(self.i_mesa8)
            if columna[0] == "1" and columna[2] == "False":
                self.liberar_mesa_P(self.i_mesa1)
            elif columna[0] == "2" and columna[2] == "False":
                self.liberar_mesa_P(self.i_mesa2)
            elif columna[0] == "3" and columna[2] == "False":
                self.liberar_mesa_M(self.i_mesa3)
            elif columna[0] == "4" and columna[2] == "False":
                self.liberar_mesa_P(self.i_mesa4)
            elif columna[0] == "5" and columna[2] == "False":
                self.liberar_mesa_P(self.i_mesa5)
            elif columna[0] == "6" and columna[2] == "False":
                self.liberar_mesa_M(self.i_mesa6)
            elif columna[0] == "7" and columna[2] == "False":
                self.liberar_mesa_G(self.i_mesa7)
            elif columna[0] == "8" and columna[2] == "False":
                self.liberar_mesa_G(self.i_mesa8)

    def seleccionar_mesa(self, widget):
        """

            Método que controla o selector do TreeView de Mesas.

        """
        model, iter = self.tree_mesa.get_selection().get_selected()
        if iter != None:
            self.listaMesas.set_active(int(model.get_value(iter, 0)))

    def ocupar(self, widget):
        """

            Método que ocupa a mesa en función do seleccionado no ComboBoxText.

        """
        XestionDatos.modificar_mesas("True", str(self.listaMesas.get_active()))
        self.actualizar_listas()
        self.actualizar_mesas()

    def ocupar_factura(self, mesa):
        """

            Método que se encarga de ocupar automáticamente a mesa seleccionada polo ComboBoxText da pestaña de Facturas.

        """
        XestionDatos.modificar_mesas("True", mesa)
        self.actualizar_listas()
        self.actualizar_mesas()

    def baleirar(self, widget):
        """

            Método que se encarga de baleirar as mesas en función do ComboBoxText.

        """
        XestionDatos.modificar_mesas("False", str(self.listaMesas.get_active()))
        self.actualizar_listas()
        self.actualizar_mesas()

    def seleccion_provincia(self, widget):
        """

            Método que se ocupa de cargar as Localidades en función da Provincia seleccionada no seu correspondente ComboBoxText.

        """
        self.combo_localidade.remove_all()
        BDProvinciasLocalidades.cargar_localidades(self.combo_localidade, self.combo_provincia.get_active_text())

    def creafilas_clientes(self):
        """

            Método que se ocupa de crear e devolver a fila construida para a creación dos clientes na BBDD.

        """
        dni = self.tex_dni.get_text()
        direccion = self.tex_direccion.get_text()
        apel = self.tex_apelidos.get_text()
        nom = self.tex_nome.get_text()
        provincia = self.combo_provincia.get_active_text()
        localidade = self.combo_localidade.get_active_text()
        filacli = (dni, apel, nom, direccion, provincia, localidade)
        return filacli

    def creafilas_clientes_mod(self):
        """

            Método que se ocupa de crear e devolver a fila construida para a creación dos clientes na BBDD.

        """
        dni = self.tex_dni.get_text()
        direccion = self.tex_direccion.get_text()
        apel = self.tex_apelidos.get_text()
        nom = self.tex_nome.get_text()
        provincia = self.combo_provincia.get_active_text()
        localidade = self.combo_localidade.get_active_text()
        filacli = (dni, apel, nom, direccion, provincia, localidade,self.dniProvisional)
        return filacli

    def alta_cliente(self, widget):
        """

            Método que se ocupa de controlar a accion do botón alta_cliente.

        """
        XestionDatos.insertar_cliente(self.comprobar_entradas_cliente())
        self.actualizar_listas()
        self.limpacaixas_cliente()

    def baixa_cliente(self, widget):
        """

            Método que se ocupa de controlar a accion do botón baixa_cliente.

        """
        if self.tex_dni.get_text() != "":
            XestionDatos.baixa_cliente(str(self.tex_dni.get_text()))
            self.actualizar_listas()
            self.limpacaixas_cliente()
        else:
            self.imprimir_error("Faltan datos para a eliminación");

    def mod_cliente(self, widget):

        """

            Método que se ocupa de controlar a accion do botón modificar_cliente.

        """
        XestionDatos.modificar_cliente(self.comprobar_entradas_cliente_mod())
        self.actualizar_listas()
        self.limpacaixas_cliente()

    def cargandodatos_clientes(self, widget):
        """

            Método que se ocupa de cargar os datos do TreeView do cliente nos Entry correspondentes.

        """
        model, iter = self.tree_clientes.get_selection().get_selected()
        if iter != None:
            self.tex_dni.set_text(str(model.get_value(iter, 0)))
            self.dniProvisional =str(model.get_value(iter, 0))
            self.tex_apelidos.set_text(model.get_value(iter, 1))
            self.tex_nome.set_text(model.get_value(iter, 2))
            self.tex_direccion.set_text(model.get_value(iter, 3))

    def comprobar_entradas_cliente(self):
        """

            Método que se ocupa de comprobar que os datos para a creación do cliente son correctos, devolvendo True se o son, e False se non.

        """
        if self.tex_dni != '' and self.tex_direccion != '' and self.tex_apelidos != '' and self.tex_nome != '':
            if servicios.comprobarDNI(self.tex_dni):
                return self.creafilas_clientes()
            else:
                self.imprimir_error("DNI Incorrecto.")
        else:
            self.imprimir_error("Faltan datos.")

    def comprobar_entradas_cliente_mod(self):
        """

            Método que se ocupa de comprobar que os datos para a actualización do cliente son correctos, devolvendo True se o son, e False se non.

        """
        if self.tex_dni != '' and self.tex_direccion != '' and self.tex_apelidos != '' and self.tex_nome != '':
            if servicios.comprobarDNI(self.tex_dni):
                return self.creafilas_clientes_mod()
            else:
                self.imprimir_error("DNI Incorrecto.")
        else:
            self.imprimir_error("Faltan datos.")

    def limpacaixas_cliente(self):
        """

            Método que se ocupa de limpar os entry e os combo da pestaña de Clientes.

        """
        self.tex_dni.set_text("")
        self.tex_nome.set_text("")
        self.tex_apelidos.set_text("")
        self.tex_direccion.set_text("")
        self.combo_localidade.remove_all()
        self.combo_provincia.remove_all()

    def comprobar_entradas_factura(self):
        """

            Método que se ocupa de comprobar que os datos para a creación de Factura son correctos, devolvendo True se o son, e False se non.

        """
        if self.combo_Camareiro.get_active_text() != None and self.combo_Mesa.get_active_text() != None and self.combo_Cliente.get_active_text() != None:
            return True
        else:
            return False

    def creafilas_Factura(self):
        """

            Método que se ocupa de crear a fila de datos precisa para a inserción de Factura na BBDD.

        """
        cliente = self.combo_Cliente.get_active_text()
        camareiro = self.combo_Camareiro.get_active_text()
        mesa = self.combo_Mesa.get_active_text()
        data = time.strftime("%d/%m/%y")
        self.ocupar_factura(mesa)

        filafact = (cliente, camareiro, mesa, data, "No")
        return filafact

    def crear_factura(self, widget):
        """

            Método que se ocupa de desencadear o evento de insercion de Factura na BBDD.

        """
        if self.comprobar_entradas_factura():
            XestionDatos.insertar_factura(self.creafilas_Factura())
            self.actualizar_listas()
        else:
            self.imprimir_error("Faltan datos para a inserción da Factura.")

    def pagarfactura(self, widget):
        """

            Método que se ocupa de desencadear o evento de modificación de Factura na BBDD.

        """
        model, iter = self.tree_Facturas.get_selection().get_selected()
        if iter != None:
            XestionDatos.pagar_factura(str(model.get_value(iter, 0)))
        else:
            self.imprimir_error("Non se seleccionou ningunha factura.")
        self.actualizar_listas()

    def comprobar_entradas_fFactura(self):
        """

            Método que se ocupa de comprobar que os datos para a creación de FilaFactura son correctos, devolvendo True se o son, e False se non.

        """
        if self.combo_servicios.get_active() != -1 and self.combo_facturas.get_active() != -1 and (int(self.cantidade.get_text()) > 0):
            return True
        else:
            return False

    def creafilas_fFactura(self):
        """

            Método que se ocupa de crear a fila de datos precisa para a inserción de FilaFactura na BBDD.

        """
        filafFact = (self.combo_facturas.get_active_text(), (int(self.combo_servicios.get_active())+1), self.cantidade.get_text())
        return filafFact

    def buscar_fFactura(self, widget):
        """

            Método que se ocupa de Filtrar as facturas do TreeView en funcion do contido dun ComboBoxText.

        """
        if self.combo_facturas.get_active() != -1:
            self.listServicio.clear()
            lista4 = XestionDatos.consultar_lineaFactura_mod(self.combo_facturas.get_active_text())
            for registro4 in lista4:
                self.listServicio.append(registro4)

    def crear_fFactura(self, widget):
        """

            Método que se ocupa de desencadear o evento de insercion de FilaFactura na BBDD.

        """
        if self.comprobar_entradas_fFactura():
            XestionDatos.insertar_lineaFactura(self.creafilas_fFactura())
            self.cantidade.set_text("0")
            self.combo_servicios.set_active(-1)
            self.combo_facturas.set_active(-1)
            self.actualizar_listas()
        else:
            self.imprimir_error("Faltan datos para a inserción de Servicio.")

    def seleccionar_Factura(self, widget):
        """

            Método que se ocupa de seleccionar o id da factura indicada no TreeView para a posterior impresión da Factura/Ticket.

        """
        model, iter = self.tree_Facturas.get_selection().get_selected()
        if iter != None:
            self.Factura_Seleccionada = model.get_value(iter, 0)
            self.pagouse = model.get_value(iter,5)

    def mostrar_venAvisos(self, widget):
        """

            Método que se ocupa de mostrar a ventá de Avisos.

        """
        self.ven_Avisos.show()

    def mostrar_novoServicio(self, widget):
        """

            Método que se ocupa de mostrar a ventá para a inserción de novos servicios.

        """
        self.ven_Servicios.show()

    def pecharVenta(self, widget):
        """

            Método que se ocupa de ocultar dita ventá.

        """
        self.ven_Servicios.hide()

    def comprobar_entradas_plato(self):
        """

            Método que se ocupa de comprobar que os datos para a creación de Servicio son correctos, devolvendo True se o son, e False se non.

        """
        if self.ent_producto_servicio.get_text() == "" or self.ent_precio_servicio.get_text() == "":
            self.imprimir_error("Faltan datos para a inserción deste prato.")
            return False
        else:
            return True

    def creafilas_plato(self):
        """

            Método que se ocupa de crear a fila de datos precisa para a inserción de Servicio na BBDD.

        """
        filapla = self.ent_producto_servicio.get_text(), servicios.colocarEuro(float(self.ent_precio_servicio.get_text()))
        return filapla

    def imprimir_error(self, texto):
        """

            Método que se ocupa de desencadear o mostrado e impresión dos erros, mediante o texto proporcionado.

        """
        self.ven_Avisos.show()
        self.lbl_error.set_text(texto)

    def crear_plato(self, widget):
        """

            Método que se ocupa de desencadenar a inserción de datos na taboa de Servicio.

        """
        if self.comprobar_entradas_plato():
            XestionDatos.insertar_plato(self.creafilas_plato())
            self.ent_precio_servicio.set_text("")
            self.ent_producto_servicio.set_text("")
            self.actualizar_listas()

    def sair_error(self, widget):
        """

            Método que se ocupa de pechar a ventá de avisos.

        """
        self.ven_Avisos.hide()

    def creaCopia(self, widget):
        """

            Método que se ocupa de desencadear a creación da copia de seguridade da BBDD principal.

        """
        self.imprimir_error("Creando a copia de seguridade.")
        servicios.xerar_copia_seg()

    def probaImpresion(self, widget):
        """

            Método que se ocupa de desencadear a impresión dunha factura, se esta está pagada.

        """
        if(self.pagouse==None):
            self.imprimir_error("Non se seleccionou ningunha factura.")
        else:
            if (self.pagouse == "Si"):
                informes.reportservicios(self.Factura_Seleccionada)
            else:
                self.imprimir_error("A factura seleccionada non está pagada.")

    def probaImpresion2(self, widget):
        """

            Método que se ocupa de desencadear a impresión dun ticket.

        """
        if (self.pagouse == None):
            self.imprimir_error("Non se seleccionou ningunha factura.")
        else:
            if (self.pagouse=="Si"):
                informes.reportservicios2(self.Factura_Seleccionada)
            else:
                self.imprimir_error("A factura seleccionada non está pagada.")



if __name__ == "__main__":
    print("Lanzase a aplicación.")
    main = Restaurante()
    Gtk.main()
