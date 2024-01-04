# Kids Videos Flask Project

## Project Description

The goal of this project is to create a safe, localized browsing environment for children to enjoy age-appropriate YouTube videos. With the consideration that full access to a platform like YouTube isn't always suitable for young viewers, this project provides a solution by allowing selected YouTube videos to be displayed on a local network.

Our application showcases a collection of YouTube videos embedded on a webpage, approved and uploaded internally by parents. This offers children a narrow selection of parent-approved content to browse and watch, protected from inappropriate or unwanted material. The platform is designed to operate on restricted computers that have strict internet access; only whitelisted sites are accessible, blocking all other Internet pages. This ensures a safe space for young minds to explore and learn through quality, pre-screened video content.

## Components & Functionality

The project is structured in Python using the Flask web framework and SQLite as a database. End to end, the project employs HTML/CSS for frontend presentation, JavaScript/jQuery to bring dynamic functionality to pages, and Python/SQLite for backend logic and data storage.

1. **SQLite Database (`kidsvideos.db`)**: All video details (including title, category, YouTube link, upload date, channel, and youtubeID) are stored and managed in this database.
    
2. **Python Scripts**:
    
    - **`databaseHelper.py`**: Serves as the application's backbone. It contains the Flask routes that handle requests and render templates.
        
    - **`add_video.py`**: A utility script used to add new videos to the database. It fetches video information from YouTube using the YouTube Data API v3 and inserts this data into the SQLite database.
        
3. **HTML Templates**: Stored under the templates directory, these files control the layout and structure of the website.
    
    - `index.html` - Main homepage displaying the latest videos and category/channel filters.
    - `video.html` - Displays individual YouTube videos in an embedded player, including video title and category.
    - `category.html` & `channel.html` - Lists the videos associated with a specific category or channel.
    - `database.html` - Presents an extensive table view of all video data from the database.
    - `navbar.html` - A reusable navbar component used across multiple pages.
4. **JavaScript/jQuery** (`scripts.js`): Fetches video, channel, and category data to be dynamically displayed on webpages.
    
5. **CSS Files** (`styles.css`): Dictates the appearance and styling across all webpages.
    

## Working Mechanism

This project largely revolves around the connection and collaboration between its several components. On the front-end, HTML templates are used to create the structure of the website, with CSS providing style and aesthetics. JavaScript/jQuery are involved to inject dynamic functionality into the pages.

Python runs the back-end logic through Flask, serving differing functionalities via different routes. For instance, the Flask routes manipulate, add to, or fetch data from the SQLite database, those data are then rendered in the corresponding pages to be viewed in the browser.

A crucial functionality worth mentioning is the manipultion of videos in the kidsvideos.db database. There are several scripts that are designed to take parameters with the execution of the script to read, delete, modify, and add to the database.

The Python and JS scripts ensure that proper and recommended videos based on their categories or channels (collected in the database) are displayed appropriately for each user.

Interaction between these modules presents a streamlined and safe video viewing platform for kids, with the control of content selection in their parents' hands.

## Summary

In essence, this project has created a safe and localized alternative to children browsing YouTube freely by rendering parent-approved YouTube videos on a local network. Its operation on computers with whitelisted site access offers an added layer of protection against inappropriate content. The control is back to where it should be, in the parents' hands, granting them peace of mind in the digital age.


## More Information

How to have running session in background with screens:

1. screen -S kidsyoutube
2. run python
3. ctr + a, d
4. Close Terminal

## TODO:

 - Add Search Functionality
 - Move iOS Shortcut functionality into Python scripts for add/delete
    - Create selection list for when deleting that will be based on a wildcard search
 - Create setup instructions for setting up project and iOS shortcuts