# Django Switchvox Archive
provides a solution to neatly display exported WAV/XML pairs of call recordings for users to download locally.

## What it does:
  1. Recurses through the recordings directory
  2. Collects the XML data for each WAV/XML pair
  3. Uploads data and relative filepath to the audio recording to MySQL Database
  4. Displays the collected information in a table on index.php to with an available download link that will download the audio recording to the user's local machine. 

## How to use:
 The following will outline the requirements and setup process:

 ### Requirements
  This web app uses Python, Django, Mysql and will require a web server. Personally, I prefer NGINX, however you should be able to use whatever you wish. 

#### Installation
##### Python:
   Follow the instructions found at [python.org](https://www.python.org/) for help installing and setting up Python for your OS.
 - Dependencies:\
    from this project's base directory run `pip install -r requirements.txt`
##### MySQL
 - If you do not already have MySQL installed use the following links to get started based on your OS:\
    [MySQL for Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)\
    [MySQL for macOS](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/osx-installation.html)\
    [MySQL for Linux](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)
 - Create your database:\
   `mysql -u [user] -p`\
   `CREATE DATABASE [db name]`\
   `\q`
##### Environment variables
  The project uses environment variables to collect sensitive information. If you are unsure how to set environment variables for your OS, take a look at [Twilio's helpful tips](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) or run a simple search on your favorite [search engine](https://duckduckgo.com/?q=set+environment+variables&t=h_&ia=web)\
   \
  The following are a list of environment variables that will need to exist:
  - Database information should be set using the following variables
   - archiver_db
   - archiver_host
   - archiver_user
   - archiver_password
   - archiver_port
