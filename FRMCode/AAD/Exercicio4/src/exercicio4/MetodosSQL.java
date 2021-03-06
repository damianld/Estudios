/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicio4;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *
 * @author a18franciscorm
 */
public class MetodosSQL {
    Connection conect=null;
    public void creaTaboas(){
        
        try{
            conect=DriverManager.getConnection("jdbc:mysql://localhost:3306/?user=root");
            System.out.println("Base creada correctamente.");
        }catch(SQLException sqle1){
            System.out.println("Error na instancia da conexión: "+sqle1.getMessage());
        }
        try{
            Statement creacion=conect.createStatement();
            creacion.execute("create database if not exists Libreria;");
            creacion.execute("use Libreria;");
            creacion.execute("create table if not exists Autores("
                    + "dniautor int(8) not null,"
                    + "nome varchar (60),"
                    + "nacionalidade varchar(30),"
                    + "primary key(dniautor)"
                    + ");");
            creacion.execute("create table if not exists Libros ("
                    + "idlibro int(3) unsigned zerofill auto_increment not null,"
                    + "titulo varchar(30) not null,"
                    + "prezo float not null,"
                    + "autor int(8),"
                    + "primary key(idlibro),"
                    + "unique key (titulo),"
                    + "index fk_autor(autor),"
                    + "constraint fk_autor "
                    + "foreign key(autor) references Autores(dniautor) on delete cascade on update cascade"
                    + ");");
            creacion.execute("create table if not exists Telefonos("
                    + "dni int(8) not null,"
                    + "ntel int(9),"
                    + "foreign key(dni) references Autores(dniautor) on delete cascade on update cascade,"
                    + "primary key(dni)"
                    + ");");
            
            System.out.println("Taboas creadas correctamente.");
            conect.close();
        }catch(SQLException sqle1){
            System.out.println("Error na creación das táboas: "+sqle1.getMessage());
        }
        
    }
    public void desconectar(){
        try{
        conect.close();
        }catch(SQLException sqle1){
            System.out.println("Error na creación das táboas: "+sqle1.getMessage());
        }
    }
}
