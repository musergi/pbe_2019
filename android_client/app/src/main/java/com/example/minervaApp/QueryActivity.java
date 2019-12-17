package com.example.minervaApp;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TableLayout;
import android.widget.TextView;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class QueryActivity extends AppCompatActivity implements QueryHandler.QueryCallback {
    public Student student;
    public String hostAddress;
    private Handler handler;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_query);

        setActivity();

        handler = new Handler(Looper.getMainLooper()) {
            @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN)
            @Override
            public void handleMessage(Message inputMessage) {
                String response = (String) inputMessage.obj;
                TableRenderer.render(response, QueryActivity.this);
            }
        };

        Button searchButton = findViewById(R.id.search_button);
        Button logOutButton = findViewById(R.id.log_out);

        logOutButton.setOnClickListener(new LogoutHandler(this));
        searchButton.setOnClickListener(new QueryHandler(this));
    }

    @Override
    public void onQueryResponse(String response) {
        Message message = handler.obtainMessage(0, response);
        message.sendToTarget();
    }

    private void setActivity () {
        student = (Student) getIntent().getSerializableExtra("student");
        hostAddress = getIntent().getStringExtra("hostAddress");

        TextView name = findViewById(R.id.greeting_text_view);
        name.setText("Welcome " +student.getName());
    }


}
