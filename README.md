# AI Community Resource Navigator

## Overview

The **AI Community Resource Navigator** is a beginner-friendly Python desktop application that helps users find local community resources based on their needs. Users describe their situation in plain English, and the application analyzes the text to recommend relevant services such as healthcare, housing, food assistance, legal aid, education, employment support, and mental health services.

This project uses **Tkinter** for the graphical interface and simple text-matching logic to simulate an AI-powered recommendation system.

---

## Features

- Desktop graphical user interface built with Tkinter  
- Natural language input (users describe their situation in their own words)  
- Keyword, context, and text similarity analysis  
- Categorized community resources:
  - Healthcare
  - Housing
  - Food
  - Legal
  - Employment
  - Education
  - Mental Health
- Ranked results with confidence scores  
- Example prompts for beginners  
- Fully offline and easy to understand  

---

## Application Layout

The application includes:

- A text input area where users describe their needs  
- Example buttons to quickly insert common requests  
- A results panel displaying recommended resources with:
  - Description
  - Contact information
  - Address
  - Eligibility requirements
  - Match confidence percentage  

---

## Requirements

### System Requirements

- Python 3.8 or higher

### Python Libraries Used

All libraries are part of the Python standard library:

- tkinter
- ttk
- scrolledtext
- re
- difflib
- datetime
- typing

No third-party packages are required.

## How the Application Works
### Step 1: User Input

The user types a description of their situation, for example:

I need help paying rent

Looking for free dental care

My child needs tutoring

I am struggling with depression

### Step 2: Text Analysis

The application processes the input by:

Converting the text to lowercase

Breaking the text into words

Matching words against predefined keywords

Checking context based on categories (housing, food, mental health, etc.)

Comparing text similarity with resource descriptions

Calculating a confidence score

### Step 3: Resource Ranking

Resources are ranked by confidence score

The most relevant matches are displayed first

Only results above a relevance threshold are shown
