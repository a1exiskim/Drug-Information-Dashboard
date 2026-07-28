# Drug-Information-Dashboard

A Python application that retrieves drug information from the OpenFDA API and displays relevant information in a dashboard.

## Project Goal

This project is being built to learn:
- REST APIs
- JSON data handling
- Data extraction and transformation
- Database integration
- Data visualization

## Project Progress

### API Integration (Extract)
- [x] Install and configure `requests` library
- [x] Connect Python application to OpenFDA API
- [x] Send API requests using drug name as input
- [x] Understand OpenFDA API endpoints and query parameters
- [ ] Handle API response status codes
- [x] Retrieve and inspect raw JSON responses
- [ ] Save raw API responses for future processing

### Data Transformation (Transform)
- [x] Explore OpenFDA JSON structure
- [x] Identify relevant drug information fields
- [ ] Extract important fields:
  - [x] Drug name
  - [x] Generic name
  - [x] Manufacturer
  - [ ] Purpose
  - [ ] Active ingredients
  - [ ] Warnings
- [ ] Handle missing or incomplete data
- [ ] Clean and format extracted information
- [ ] Create reusable data transformation functions

### Data Storage (Load)
- [ ] Design a data storage structure
- [ ] Store cleaned drug information
- [ ] Create database tables for drug information
- [ ] Insert transformed API data into database
- [ ] Query stored drug information

### Dashboard Development
- [ ] Design dashboard layout
- [ ] Create user input for drug searches
- [ ] Connect dashboard to API pipeline
- [ ] Display cleaned drug information
- [ ] Add error messages for invalid searches
- [ ] Improve dashboard usability and formatting

### Future Enhancements
- [ ] Track drug search history
- [ ] Add analytics on searched drugs
- [ ] Add drug comparison functionality
- [ ] Add scheduled data updates
