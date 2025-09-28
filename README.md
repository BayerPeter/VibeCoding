# Complaint Assistance System

A system for managing pharmaceutical product complaints and generating investigation reports.

## Prerequisites

1. Python 3.8 or higher
2. pip (Python package installer)

## Installation & Setup

1. Clone or download this repository
2. Make sure Python is added to your system's PATH
3. Double-click `run_server.bat` or run it from the command line

The batch file will:
- Check Python installation
- Create necessary directories
- Install required packages
- Initialize the database
- Start the server

## Using the System

Once the server is running, you can access the system at http://localhost:8080

### Main Features

1. **Submit Complaints**
   - Go to http://localhost:8080/complaints/create
   - Fill in the complaint description
   - Optionally attach images
   - Submit to get automatic analysis

2. **View Complaints**
   - Go to http://localhost:8080/complaints
   - See all submitted complaints
   - Access detailed reports

3. **Investigation Reports**
   - Go to http://localhost:8080/reports
   - View all investigation reports
   - Track CAPA actions

### API Documentation

- Available at http://localhost:8080/docs
- Shows all API endpoints and schemas

## System Features

- Automatic complaint analysis
- Report generation
- Image attachment support
- Complaint history tracking
- CAPA management
- Mock data support when RAG service is unavailable

## Troubleshooting

1. If the server doesn't start:
   - Ensure Python is installed and in PATH
   - Check if port 8080 is available
   - Look for error messages in the console

2. If you can't access the web interface:
   - Verify the server is running
   - Try accessing http://localhost:8080/docs first
   - Check your firewall settings

## Directory Structure

- `/app` - Main application code
  - `/templates` - HTML templates
  - `/static` - Static files
  - `/services` - Service modules
- `/uploads` - Uploaded files
- `/instance` - Instance-specific files
