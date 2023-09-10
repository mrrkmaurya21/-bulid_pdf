#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Import necessary modules from ReportLab
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time as part of the filename
formatted_date = current_datetime.strftime("%Y/%m/%d")
formatted_time = current_datetime.strftime("%H:%M:%S")

# Define some sample data
Time = formatted_time
Name = "Mr. Maurya"
Position = "Buy/Sell"
Status = "Completed/Rejected"

"""
# Initialize your data (sample values)
LTP = []
Quantity = []
for i in range(1, 10):
    LTP.append(2 * i)
    Quantity.append(30 + i)
# Create a list of lists to represent the table data
data = [
    ["Time", "Name", "Position", "Quantity", "LTP", "Status"],
    [Time, Paragraph(f"{Name}", getSampleStyleSheet()['Normal']), Position, Quantity[0], LTP[0], Status],
    ["", "", "", Quantity[1], LTP[1], ""],
    ["", "", "", Quantity[2], LTP[2], ""],
]
"""
# Define the range for generating rows
row_range = 50  # Change this number to generate the desired number of rows
# Initialize your data (sample values)
LTP = []
Quantity = []
for i in range(1, row_range + 1):  # Add +1 to the range to generate the specified number of rows
    LTP.append(2 * i)
    Quantity.append(30 + i)
# Create a list of lists to represent the table data
data = [
    ["Sr.No.","Time", "Name", "Position", "Quantity", "LTP", "Status"],
]
# Generate rows based on the range
for i in range(row_range):
    data.append([i+1,Time, Name, "", Quantity[i], LTP[i], Status])
    
    
# Count the number of rows (excluding the header row)
Counts = len(data) - 1  # Subtract 1 to exclude the header row

# Define styles for the table
style = [
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header row font style
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Bottom padding for header row
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Data row background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines for all cells
]

# Create a PDF document
formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
output_pdf = f"trading_{formatted_datetime}.pdf"
doc = SimpleDocTemplate(output_pdf, pagesize=letter)

# Define a custom PageTemplate for the header
def header_template(canvas, doc):
    logo_image = Image("images.jpeg", width=100, height=50)  # Adjust the image path, width, and height
    logo_image.drawOn(canvas, 40, 720)  # Adjust the position as needed

# Add the header template to each page
doc.build([Paragraph("")] * 2, onFirstPage=header_template, onLaterPages=header_template)

# Create a title or header paragraph
title_text = f"Trading Report"
styles = getSampleStyleSheet()
title_style = styles["Title"]
title = Paragraph(title_text, title_style)

# Create a story to hold the document elements
story = [title, Spacer(1, 24)]  # Add title and some space

# Define a ParagraphStyle for the header information
header_style = ParagraphStyle(
    name='HeaderStyle',
    alignment=0,  # Left alignment
    parent=getSampleStyleSheet()['Normal']
)

# Create a list of Paragraphs for the header information
header_text = [
    Paragraph(f"Name : <b> {Name}</b>", header_style),  # Left-aligned text
    Spacer(1, 6),  # Create a small spacer for alignment
    Paragraph(f"Total P&L :   287356", getSampleStyleSheet()['Normal']),  # Left-aligned text
    Spacer(1, 6),  # Create a small spacer for alignment
    Paragraph(f"Invoice Date :   {formatted_date}  {formatted_time}", getSampleStyleSheet()['Normal']),  # Left-aligned text
    Spacer(1, 6),  # Create a small spacer for alignment
    Paragraph(f"Email-Id :   xyz@gmail.com", getSampleStyleSheet()['Normal']),  # Left-aligned text
    Spacer(1, 6),  # Create a small spacer for alignment
    Paragraph(f"Counts :   {Counts}", getSampleStyleSheet()['Normal']),  # Left-aligned text
]

# Extend the story with header_text and add space
story.extend(header_text)
story.append(Spacer(1, 12))  # Add space

# Create the table and apply the defined style
table = Table(data)
table.setStyle(TableStyle(style))

# Add the table to the story
story.append(table)

# Build the PDF document
doc.build(story)

# Print a message indicating the saved PDF file
print(f"Table saved as {output_pdf}")


# In[ ]:




