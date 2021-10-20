# Exploring Spotify Songs from 1921-2020

## Link to Visualization

[https://share.streamlit.io/samarthgowda/assignment-2-samarthgowda/main/main.py](https://share.streamlit.io/samarthgowda/assignment-2-samarthgowda/main/main.py)

## Project Description & Goals

This project was looking to understand how music has changed over time. The dataset that was chosen for this project came from [Kaggle](https://www.kaggle.com/ektanegi/spotifydata-19212020) and it was information for over 169k songs collected from the Spotify Web API. The question this application is aiming to answer is **What aspects of music have changed over the last century (from 1921-2020)?** The goals of this project are to understand the answer to this question and to create visualizations that help future users of this application find their own answers to this question.

## Design Decisions Rationale

**Section 1: Understanding how different aspects of songs have changed over time**

For this visualization, I wanted to allow the user to select the particular song attribute that they were interested in exploring and allow them to view how that attribute has changed over time. At first, I thought about grouping the years into decades and creating a bar plot of sorts or using a scatterplot with a data point for each song. However, I realized that a simple line plot with the release year on the x-axis and the selected attribute on the y-axis would provide sufficient information. In order to do this line plot, I grouped all of the songs for each year and took the average of each of the attribute values for that particular year. Even though, this will not give a full picture of that attribute for that year, it is a more sufficient way of viewing the trends over the last century for a given attribute.

**Section 2: Understanding the distribution of aspects of songs for a given release year range**

Building off the previous visualization, I knew that I wanted users to be able to see particular year ranges and what the distribution of an attribute is like for a particular year range. The previous visualization showed the average value for that attribute from 1921-2020. However, for users that wanted to see the distribution of `energy` from `2000` to `2020`, they are unable to do so. I decided to use a histogram as it allows the user to easily see this distribution for the selected year range, and they can see how these variables are also changing over time while doing so. This allows them to get as granular as possible. Another solution for this that I had thought of included using tables or a density plot, but for most users, a histogram was easy to understand and interpret.

## Development Process Overview

This application was developed individually (I did not have any team members). Most of the time for it was spent finding a dataset that would answer this question. I knew that there were lots of datasets on music and songs, but once I stumbled across this Spotify dataset, I knew that it made a lot of sense for answering my question. I spent around 10 hours on this project. This was split across multiple days. Most of the time was spent on finding the dataset, figuring out what visualizations to create, and hwo to get them to work in streamlit. The actual data cleaning, manipulating, and visualizations did not take as long since I had prior experience with pandas and data visualization libraries such as matplotlib.
