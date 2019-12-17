package com.example.minervaApp;

import android.os.Build;

import androidx.annotation.RequiresApi;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Requester {

	@RequiresApi(api = Build.VERSION_CODES.O)
	public static String get(String requestedUrl, Map<String, String> parameters) throws IOException {
		URL url = new URL(requestedUrl + "?" + parseParams(parameters));
		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
		connection.setRequestMethod("GET");
		
		return readResponse(connection);
	}
	
	@RequiresApi(api = Build.VERSION_CODES.O)
	public static String post(String requestedUrl, Map<String, String> parameters) throws IOException {
		URL url = new URL(requestedUrl);
		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
		connection.setRequestMethod("POST");
		
		connection.setDoOutput(true);
		OutputStream outputStream = connection.getOutputStream();
		outputStream.write(parseParams(parameters).getBytes());
		outputStream.flush();
		outputStream.close();
		
		return readResponse(connection);
	}
	
	private static String readResponse(HttpURLConnection connection) throws IOException {
		int responseCode = connection.getResponseCode();
		StringBuffer buffer = new StringBuffer();
		if (responseCode == HttpURLConnection.HTTP_OK) {
			BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
			String line;
			while ((line = reader.readLine()) != null) {
				buffer.append(line);
				buffer.append('\n');
			}
			reader.close();
		} else {
			throw new IOException("Connection refused");
		}
		return buffer.toString();
	}
	
	@RequiresApi(api = Build.VERSION_CODES.O)
	private static String parseParams(Map<String, String> parameters) throws IOException {
		List<String> parameterStrings = new LinkedList<String>();
		for (Map.Entry<String, String> parameter: parameters.entrySet()) {
			String name = URLEncoder.encode(parameter.getKey(), "UTF-8");
			String value = URLEncoder.encode(parameter.getValue(), "UTF-8");
			parameterStrings.add(name + "=" + value);
		}
		return String.join("&", parameterStrings);
	}
}
