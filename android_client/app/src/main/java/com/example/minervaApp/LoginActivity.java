package com.example.minervaApp;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class LoginActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.minerva);

        Button loginButton = findViewById(R.id.login_button);

        ClickHandler handler = new ClickHandler(this);
        loginButton.setOnClickListener(handler);
    }
}

class ClickHandler implements Button.OnClickListener{
    private AppCompatActivity activity;
    private Connection con;

    public ClickHandler (AppCompatActivity activity) {
        this.activity = activity;
    }

    @Override
    public void onClick(View v) {
        TextView  url_entry = activity.findViewById(R.id.url_entry);
        TextView  username_entry = activity.findViewById(R.id.username_entry);
        TextView  password_entry = activity.findViewById(R.id.query_entry);

        connectionLogin(url_entry,username_entry,password_entry);
    }

    private void openQueryActivity (Student student) {
        Intent myIntent = new Intent(activity, QueryActivity.class);
        myIntent.putExtra("student", student);
        myIntent.putExtra("hostAddress", con.getHostAddress());
        activity.startActivity(myIntent);
    }

    private void connectionLogin (TextView url_entry, TextView username_entry, TextView password_entry) {

        con = new Connection(url_entry.getText().toString());
        con.login(username_entry.getText().toString(), password_entry.getText().toString(), new Connection.LoginCallback() {
            @Override
            public void onLogin(Student student) {
                openQueryActivity(student);
            }
        });
    }
}
