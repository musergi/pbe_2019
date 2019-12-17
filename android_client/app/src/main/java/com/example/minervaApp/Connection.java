package com.example.minervaApp;

import android.os.Build;

import androidx.annotation.RequiresApi;

import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Connection {
	private static final String LOGIN_PATH = "/backend/java/login.php";
	
	private String hostAddress;
	
	public Connection(String url) {
		hostAddress = "http://" + url;
	}
	
	public void login(String username, String password, LoginCallback callback) {
		Worker worker = new Worker(username, password, callback);
		worker.start();
	}

	public String getHostAddress() {
		return hostAddress;
	}
	
	public interface LoginCallback {
		void onLogin(Student student);
	}
	
	private class Worker extends Thread {
		String username;
		String password;
		LoginCallback callback;
		
		public Worker(String username, String password, LoginCallback callback) {
			this.username = username;
			this.password = password;
			this.callback = callback;
		}
		
		@RequiresApi(api = Build.VERSION_CODES.O)
		public void run() {
			Map<String, String> loginParameters = new HashMap<String, String>();
			loginParameters.put("username", username);
			loginParameters.put("password", password);
			String[] login_response;

			try {
				login_response = Requester.post(hostAddress + LOGIN_PATH, loginParameters).split("\n");
				List<String> labels = Arrays.asList(login_response[0].split(","));
				List<String> values = Arrays.asList(login_response[1].split(","));

				int id = Integer.parseInt(values.get(labels.indexOf("id")));
				String name = values.get(labels.indexOf("name"));
				String surname = values.get(labels.indexOf("surname"));

				Student student = new Student(id, name, surname);

				callback.onLogin(student);

			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
