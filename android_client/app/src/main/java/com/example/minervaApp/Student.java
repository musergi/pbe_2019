package com.example.minervaApp;

import java.io.Serializable;

public class Student implements Serializable {
    private int id;
    private String name;
    private String surname;

    public Student(int id, String name, String surname) {
        this.id = id;
        this.name = name;
        this.surname = surname;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getSurname(){ return surname; }

    public String toString() {
        return name + "(" + id + ")";
    }
}
