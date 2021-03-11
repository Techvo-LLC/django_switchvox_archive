# Django Switchvox Archive
provides a solution to neatly display exported WAV/XML pairs of call recordings for users to download locally.

## What it does:
  1. Recurses through the media directory
  2. Collects the XML data for each WAV/XML pair
  3. Uploads data and relative filepath to the audio recording to MYSQL Database
  4. Displays the collected information in a table on index.php to with an available download link that will download the audio recording to the user's local machine. 

## How to use:
 The following will outline the requirements and setup process:

 ### Requirements
  This web app uses Python, Django, Mysql and will require a web server. Personally, I prefer NGINX, however you should be able to use whatever you wish. 

#### Installation
 - Python can be installed in various ways. Follow the instructions found at [python.org](https://www.python.org/) for help installing and setting up Python for your OS.
 - Once Python is installed, use pip to install the dependencies found in requirements.txt
 - - from the base directory run `pip install -r requirements.txt`

