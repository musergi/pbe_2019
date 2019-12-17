package com.example.minervaApp;

import android.annotation.SuppressLint;
import android.os.Build;
import android.view.Gravity;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import androidx.annotation.RequiresApi;

import java.util.Arrays;
import java.util.List;

import static com.example.minervaApp.R.drawable.table_body;


public class TableRenderer {

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN)

    public static void render (String response, QueryActivity activity){
        TableLayout table = activity.findViewById(R.id.table);
        List<String> data = Arrays.asList(response.split("\n"));

        // Remove previous content
        table.removeAllViews();

        //Create the table
        for (String row: data) {
            TableRow tableRow = new TableRow(activity);
            List<String> columns = Arrays.asList(row.split(","));
            for (String column: columns) {
                TextView textView = new TextView(activity);
                setStyle(textView, activity);
                textView.setText(column);
                tableRow.addView(textView);
            }
            table.addView(tableRow);
        }
    }

    @SuppressLint("NewApi")
    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN)
    public static void setStyle(TextView textView, QueryActivity activity){
        textView.setTextSize(18);
        textView.setGravity(Gravity.CENTER);
        textView.setBackground(activity.getDrawable(table_body));
        textView.setPadding(16, 2, 16, 2);
    }
}
