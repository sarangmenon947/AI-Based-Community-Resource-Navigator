Below is a beginner-friendly README.md you can copy directly into your project.
It avoids emojis/icons and explains both what the app does and how the code works at a high level.

AI Community Resource Navigator

The AI Community Resource Navigator is a beginner-friendly Python desktop application that helps users find local community resources based on their needs. Users describe their situation in plain English, and the application analyzes the text to recommend relevant services such as healthcare, housing, food assistance, legal aid, education, employment support, and mental health services.

This project uses Tkinter for the graphical interface and simple text-matching logic to simulate an AI-powered recommendation system.

Features

Simple desktop user interface built with Tkinter

Natural language input (users describe their situation in their own words)

Smart matching using keywords, context analysis, and text similarity

Categorized community resources:

Healthcare

Housing

Food

Legal

Employment

Education

Mental Health

Ranked results with confidence scores

Example prompts to help users get started

Fully offline and beginner-friendly

Screens Overview

The application includes:

A text box where users describe what kind of help they need

Example buttons to quickly fill in common requests

A results area that displays recommended resources with details such as:

Description

Contact information

Address

Eligibility requirements

Match confidence

Requirements

Python 3.8 or higher

No external libraries required (everything used is part of the Python standard library)

Used standard libraries include:

tkinter

ttk

scrolledtext

re

difflib

datetime

typing

Installation

Make sure Python is installed on your system
You can check by running:

python --version


Clone or download this repository

Navigate to the project folder:

cd ai-community-resource-navigator

How to Run the Application

Run the Python file from your terminal or command prompt:

python main.py


(Replace main.py with the filename if you named it differently.)

A window titled AI Community Resource Navigator will open.

How It Works (Beginner Explanation)
1. User Input

The user types a description such as:

“I need help paying rent”

“I am struggling with depression”

“Looking for free dental care”

2. Text Analysis

The program:

Converts the text to lowercase

Breaks it into words

Compares the words to keywords stored in each resource

Checks context (for example, housing-related words or mental health terms)

Uses text similarity to compare the user input with resource descriptions

Assigns a confidence score to each match

3. Ranking Results

Resources with higher confidence scores are shown first. Only relevant matches are displayed.

Project Structure
.
├── main.py              # Main application file
├── README.md            # Project documentation


All resource data is stored directly inside the Python file as dictionaries for simplicity.

Customizing the Resources

You can easily add or modify resources by editing the self.resources dictionary in the code.

Each resource includes:

name

type

description

contact

address

eligibility

keywords

Example:

{
    "name": "Community Health Center",
    "type": "Primary Care",
    "description": "Sliding scale fees based on income.",
    "contact": "555-0101",
    "address": "123 Health St",
    "eligibility": "All income levels accepted",
    "keywords": ["doctor", "medical", "health"]
}

Intended Use

This project is intended for:

Learning basic GUI development with Tkinter

Understanding simple natural language processing concepts

Demonstrating how software can support community services

Educational or prototype purposes

It is not a replacement for professional advice or emergency services.

Future Improvements

Possible enhancements include:

Loading resources from a JSON file or database

Adding real location-based search

Improving AI matching logic

Exporting results to a file

Adding accessibility features

Adding multi-language support

License

This project is open for educational and personal use.
You are free to modify and expand it as needed.
