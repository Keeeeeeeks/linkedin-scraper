# A Linkedin Scraper

## Background

ATS (Applicant Tracking Systems) have made job application reviews easy for employers, but deceptively difficult for job applicants. For a number of applicants who are either inexperienced with drafting resumes, don't believe in embellishing experience, or are making lateral moves across job functions and companies, ATSes can swiftly end a job applicant's journey before they're able to speak with a human about their experiences.

[ATSes pre-filter applications based on keywords.](https://www.themuse.com/advice/beat-the-robots-how-to-get-your-resume-past-the-system-into-human-hands) While this may make sense on paper, the issue is that great potential hires may not know that there are pre-screens and internal scores that affect their job hunt. As they continue to apply, with limited to no feedback on why their application was rejected, they may find decreased success with job applications and lose motivation, which then feeds into decreased interview performance, and decreased chances of receiving an offer.

## Purpose

This script is designed to help job applicants put their best foot forward. The script does this by asking the user what their desired role is, searching jobs with similar titles, compiling job descriptions into a data set, and generating a word cloud that weighs concepts and terms based on frequency across job descriptions. From that, applicants can adjust their resumes to make sure that they mention relevant experiences in a way that maximizes their chance of progressing to the next round.

## Process

Given a job title (user input), the script will:
1. Search LinkedIn for the role
2. Take 9 pages worth of job descriptions
3. Add them to a .txt file
4. Use the job descriptions as data for a Word Cloud
5. Shape the word cloud in the form of a goose (it can be any b&w image)

## Feedback

Please submit an issue or PR if you notice anything wrong!
