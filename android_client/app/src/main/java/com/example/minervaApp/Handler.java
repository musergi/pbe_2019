package com.example.minervaApp;

import android.os.Build;
import android.os.Message;

import androidx.annotation.RequiresApi;

public class Handler {
    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN)
    public void handleMessage(Message inputMessage, QueryActivity activity) {
        String response = (String) inputMessage.obj;
        TableRenderer.render(response, activity);
    }
}
