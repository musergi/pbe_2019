package com.example.minervaApp;

import android.os.Build;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.RequiresApi;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class QueryHandler implements Button.OnClickListener {

    private QueryActivity activity;

    public QueryHandler(QueryActivity activity) {
        this.activity = activity;
    }

    public interface QueryCallback {
        void onQueryResponse(String response);
    }

    @Override
    public void onClick(View v) {
        TextView queryEntry = activity.findViewById(R.id.query_entry);
        new Worker(queryEntry.getText().toString(), activity).start();
    }

    private class Worker extends Thread{

        private String query;
        private QueryCallback callback;

        public Worker (String query, QueryCallback callback){
            this.query = query;
            this.callback = callback;
        }

        @RequiresApi(api = Build.VERSION_CODES.O)
        public void run(){
            Map<String, String> queryParameters = new HashMap<String, String>();
            queryParameters.put("id", Integer.toString(activity.student.getId()));
            queryParameters.put("query", query);

            try {
                String queryResponse = Requester.get(activity.hostAddress + "/backend/java/query.php", queryParameters);
                callback.onQueryResponse(queryResponse);

            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }
}