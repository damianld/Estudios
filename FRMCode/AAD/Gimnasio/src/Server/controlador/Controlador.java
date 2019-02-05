/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Server.controlador;

import org.neodatis.odb.ODBFactory;
import org.neodatis.odb.ODBServer;

/**
 *
 * @author a18franciscorm
 */
public class Controlador {
    public ODBServer encenderServer(){
        ODBServer server = ODBFactory.openServer(8000);
        server.addBase("ximnasios", "ximnasios.neo");
        server.startServer(true);
        return server;
    }
    
    public void pechar(ODBServer servidor){
        servidor.close();
    }
}
