# Tkinter Excel Data Entry Form

A Python desktop application that collects personal and educational information through a graphical user interface and saves the submitted records in an Excel workbook.

## Features

- Collects first name, last name, title, age, and nationality.
- Collects degree, grade, and passing year.
- Uses Tkinter labels, entry fields, comboboxes, and spinboxes.
- Validates required text fields and title/degree selections.
- Requires acceptance of the terms and conditions before submission.
- Creates an Excel workbook with column headings if one does not exist.
- Appends each submitted record to the existing workbook.
- Displays success, error, and warning message boxes.

## Technologies

- Python
- Tkinter and ttk
- OpenPyXL
- OS module
- Excel file handling

## Installation

Install the required dependency:

```bash
pip install openpyxl
```

Tkinter is included with most standard Python installations.

## Run the Application

1. Save the program as `data_entry_form.py`.
2. Make sure the directory `D:\Python\Project` exists, or update the file path in the code.
3. Run:

   ```bash
   python data_entry_form.py
   ```

## Excel Data

The application saves records to `data.xlsx` with these columns:

| Personal Information | Education Information |
|---|---|
| First Name | Degree |
| Last Name | Grade |
| Title | Passing Year |
| Age | |
| Nationality | |

The first row contains the column headings. Each valid submission is added as a new row.

## How It Works

1. The user enters personal and educational information.
2. The user accepts the terms and conditions.
3. The application checks that the required fields are filled in.
4. The data is appended to the Excel workbook.
5. A success message appears after the save operation completes.


## Learning Outcomes

This project demonstrates GUI development, event-driven programming, widget configuration, form validation, and Excel spreadsheet operations in Python.
