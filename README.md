# Django Switchvox Archive
provides a solution to neatly display exported WAV/XML pairs of call recordings for users to download locally.

## What it does:
  1. Recurses through the recordings directory
  2. Collects the XML data for each WAV/XML pair
  3. Uploads data and relative filepath to the audio recording to MYSQL Database
  4. Displays the collected information in a table on index.php to with an available download link that will download the audio recording to the user's local machine. 

## How to use:
 The following will outline the requirements and setup process:

 ### Requirements
  This web app uses Python, Django, Mysql and will require a web server. Personally, I prefer NGINX, however you should be able to use whatever you wish. 

#### Installation
##### Python:
   Follow the instructions found at [python.org](https://www.python.org/) for help installing and setting up Python for your OS.
##### Python Dependencies:
   from this project's base directory run `pip install -r requirements.txt`
##### MYSQL
 - If you do not already have MYSQL installed use the following links to get started based on your OS:
    [MYSQL for Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)
    [MYSQL for macOS](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/osx-installation.html)
    [MYSQL for Linux](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)
