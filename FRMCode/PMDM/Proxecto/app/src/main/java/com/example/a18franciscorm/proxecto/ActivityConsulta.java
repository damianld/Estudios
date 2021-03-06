package com.example.a18franciscorm.proxecto;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class ActivityConsulta extends AppCompatActivity {
    AutoCompleteTextView entrada;
    ListView lista;
    SQLiteDatabase sqldb;
    ArrayList<String> listaX= new ArrayList();
    ArrayList<Alimento> alimentos= new ArrayList();
    int eliminador;
    AdaptadorPersonalizadp pers;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_consulta);
        //setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        entrada=(AutoCompleteTextView)findViewById(R.id.entrada);
        lista=(ListView)findViewById(R.id.lista);
        ClaseDB cdb= new ClaseDB(ActivityConsulta.this,"BDAlimentos",null,1);
        sqldb=cdb.getReadableDatabase();
        Cursor c= sqldb.rawQuery("Select nombre from Alimentos;",null);
        if (c.moveToFirst()) {
            do {
                listaX.add(c.getString(0).replace('_',' '));
            }while (c.moveToNext());
        }
        else
            Toast.makeText(this, "Non se recuperou nada", Toast.LENGTH_LONG).show();
        final ArrayAdapter adaptador= new ArrayAdapter(this,android.R.layout.simple_list_item_1,listaX);
        entrada.setAdapter(adaptador);
        entrada.setThreshold(1);
        entrada.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Cursor b = sqldb.rawQuery("Select * from Alimentos where nombre ='"+parent.getItemAtPosition(position).toString().replace(' ','_')+"';",null);
                b.moveToFirst();
                Alimento a = new Alimento(Integer.parseInt(b.getString(0)),b.getString(1),b.getString(2),b.getString(3),b.getString(4),b.getString(5));
                alimentos.add(a);
                entrada.setText("");
            }
        });
        pers=new AdaptadorPersonalizadp(this,alimentos);
        lista.setAdapter(pers);
        lista.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Toast.makeText(ActivityConsulta.this,"Seleccion:"+alimentos.get(position).getNome().replace(' ','_'),Toast.LENGTH_SHORT).show();
            }
        });
        lista.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
                eliminador=position;
                return false;
            }
        });
        registerForContextMenu(lista);
    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        MenuInflater me =getMenuInflater();
        me.inflate(R.menu.menu,menu);
        super.onCreateContextMenu(menu, v, menuInfo);
    }

    @Override
    public boolean onContextItemSelected(MenuItem item) {
        switch(item.getItemId()){
            case R.id.eliminar:
                alimentos.remove(eliminador);
                pers=new AdaptadorPersonalizadp(ActivityConsulta.this,alimentos);
                lista.setAdapter(pers);
        }
        return super.onContextItemSelected(item);
    }
}
