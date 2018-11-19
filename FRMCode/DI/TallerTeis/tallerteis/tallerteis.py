# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import xestionclientes
import datos



class Taller:
    def __init__(self):
        int_visual = Gtk.Builder();
        int_visual.add_from_file("XestionClientes.glade");
        self.but_alta=int_visual.get_object("but_alta")
        self.venPrincipal = int_visual.get_object("venPrincipal")
        self.listclientes = int_visual.get_object("listclientes")
        self.treeclientes = int_visual.get_object("treeclientes")
        self.entdni = int_visual.get_object("entdni")
        self.entapel = int_visual.get_object("entapel")
        self.entmat = int_visual.get_object("entmat")
        self.entnom = int_visual.get_object("entnom")
        self.entmail = int_visual.get_object("entmail")
        self.entmovil = int_visual.get_object("entmovil")
        self.entdata = int_visual.get_object("entdata")
        self.lblavisos = int_visual.get_object("lblavisos")
        self.venCalendar = int_visual.get_object("venCalendar")
        self.but_calendar = int_visual.get_object("but_calendar")
        self.selectorClientes = int_visual.get_object("selectorClientes")
        self.fecha = int_visual.get_object("fecha")
        dic = {
            'on_venPrincipal_destroy': self.sair,
            'on_but_alta_clicked': self.altacliente,
            'on_venCalendar_destroy': self.destroycalendar,
            'on_but_calendar_clicked': self.showcalendar,
            'on_fecha_day_selected_double_click': self.showfecha,
            'on_but_editar_clicked': datos.edicion,
            'on_but_eliminar_clicked': datos.eliminacion,
            'on_but_pechar_clicked': self.sair,
            'on_selectorClientes_changed': self.cargandodatos
        }
        int_visual.connect_signals(dic)
        self.lblavisos.hide()
        self.listarclientes()
        self.venPrincipal.show()
        #self.venPrincipal.maximize()

    def showfecha(self,widget):
        ano, mes, dia = self.fecha.get_date()
        self.entdata.set_text(str(dia)+'/'+str(mes)+'/'+str(ano))

    def cargandodatos(self,widget):
        model, iter = self.treeclientes.get_selection().get_selected()
        if iter != None:
            sdni = model.get_value(iter, 0)
            self.entdni.set_text(sdni)
            smat = model.get_value(iter, 1)
            self.entmat.set_text(smat)
            sapel = model.get_value(iter, 2)
            self.entapel.set_text(sapel)
            snome = model.get_value(iter, 3)
            self.entnom.set_text(snome)
            smail = model.get_value(iter, 4)
            self.entmail.set_text(smail)
            smovil = model.get_value(iter, 5)
            self.entmovil.set_text(smovil)
            sdata = model.get_value(iter, 6)
            self.entdata.set_text(sdata)

    def showcalendar(self, widget):
        self.venCalendar.show()

    def destroycalendar(self, widget):
        self.venCalendar.hide()

    def sair(self,widget):
        Gtk.main_quit()
        datos.pecharconexion()

    def listarclientes(self):
        lista = datos.listar()
        for registro in lista:
            self.listclientes.append(registro)

    def altacliente(self,widget):
            self.lblavisos.show()
            self.dni = self.entdni.get_text()
            self.mat = self.entmat.get_text()
            self.apel = self.entapel.get_text()
            self.nom = self.entnom.get_text()
            self.mail = self.entmail.get_text()
            self.movil = self.entmovil.get_text()
            self.data = self.entdata.get_text()
            if self.dni != '' and self.mat != '' and self.apel != '':
                if datos.comprobarDNI(self.entdni):
                    self.filacli = (self.dni, self.mat, self.apel, self.nom, self.mail, self.movil,self.data)
                    if datos.comprobarMail(self.mail):
                        xestionclientes.altacli(self.treeclientes, self.listclientes, self.filacli)
                        datos.altacliente(self.filacli)
                    else:
                        self.lblavisos.set_text("Email Incorrecto.")
                    self.limpacli()
                else:
                    self.lblavisos.set_text("DNI Incorrecto.")
            else:
                self.lblavisos.set_text("Faltan datos.")
    def limpacli(self):

        self.lmpcli = (self.entdni, self.entmat, self.entapel, self.entnom, self.entmail, self.entmovil,self.entdata)
        xestionclientes.limpiacli(self.lmpcli)

# engadir canlendario
# engadir as funcionalidades de medificacion "a tempo real"
# funcionalidade de BD
# Engadir boton de limpeza de seleccion.

if __name__ == "__main__":
    print("Inicio")
    main=Taller()
    Gtk.main()
