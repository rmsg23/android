package com.example.root.myapplication;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.support.v4.app.FragmentActivity.*;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.app.Activity;
import android.widget.Spinner;
import android.widget.ArrayAdapter;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemSelectedListener;
import android.widget.Toast;
import android.view.View;
import android.util.Log;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.Console;
import java.io.DataOutputStream;
import java.io.DataInputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import android.view.View;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, AdapterView.OnItemSelectedListener{
    String ip;
    String puertoS;
    String response = "Español";
    EditText editTextIP;
    EditText editTextPuerto;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViewById(R.id.button).setOnClickListener(this);
        Spinner spinner = (Spinner) findViewById(R.id.spinner);
        editTextIP = (EditText) findViewById(R.id.editText);

        editTextPuerto = (EditText) findViewById(R.id.editText2);
        String[] valores = {"Español","Inglés", "Francés"};
        spinner.setAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, valores));
        spinner.setOnItemSelectedListener(this);
    }


    @Override
    public void onClick(View v) {
        System.out.println("Hola onClick");
        ip = editTextIP.getText().toString();
        puertoS = editTextPuerto.getText().toString();
        sendCommand("Idioma: " + response);
    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int position, long id) {
            //Toast.makeText(adapterView.getContext(), (String) adapterView.getItemAtPosition(position), Toast.LENGTH_SHORT).show();
            response = ""+adapterView.getSelectedItem().toString();
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }


    private void sendCommand(String command) {
        //System.out.println("senCommand");
        new SendCommandTask().execute(command);
    }

    class SendCommandTask extends AsyncTask<String, Void, Void> {
        //System.out.println("Hola SendCommandTask");
        @Override
        protected Void doInBackground(String... commands) {
            System.out.println("doInB");
            String command = commands[0];

            try {
                //TODO: make this configurable inside the app
                System.out.println("conectando...");
                //Socket socket = new Socket("192.168.1.74", 9999);
                System.out.println("terminando...");

                int puertoS2 = Integer.parseInt(puertoS);
                System.out.println(ip);
                System.out.println(""+puertoS2);
                Socket socket = new Socket(ip, puertoS2);
                PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);
                out.println(command);
                System.out.println("sucefull");
                //Log.d(TAG, "Successfully sent " + command);
            } catch (IOException ioe) {
                System.out.println("Error");
                //Log.d(TAG, "Unable to send command", ioe);
            }
            return null;
        }
    }
}
