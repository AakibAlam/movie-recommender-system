# Movie Recommendation System

## Overview

This Movie Recommender System allows users to discover movies similar to a particular movie or find movies based on genre. It employs a content-based recommender system, utilizing TF-IDF vectorization for movie details and cosine similarity to calculate similarity scores. The system is implemented as a web application using Flask and stores movie details in a MongoDB database.

## Workflow

1. **Web Scraping with Selenium:**

   - Configures a headless Chrome browser using Selenium and initiates with configured options.
   - Navigates to each friend's Codeforces profile and fetches their recent correct submissions.

2. **Data Extraction:**

   - Extracts information about submissions made by friends yesterday.
   - Uses Jinja2 templates to format the HTML content of the email body dynamically.

3. **Email Sending:**

   - Uses the Sendgrid API to send emails.

## Preview of Email

<img src="https://github.com/AakibAlam/codeforces-submission-scraping/blob/main/preview.png" align="center" width="100%"/>
