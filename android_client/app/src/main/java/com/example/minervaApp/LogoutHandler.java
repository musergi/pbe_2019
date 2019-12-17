package com.example.minervaApp;

import android.content.Intent;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class LogoutHandler implements Button.OnClickListener {
    private AppCompatActivity activity;

    public LogoutHandler (AppCompatActivity activity) {
        this.activity = activity;
    }

    @Override
    public void onClick(View v) {
        Intent myIntent = new Intent(activity, LoginActivity.class);
        activity.startActivity(myIntent);
    }
}