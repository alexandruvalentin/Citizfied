# Citizfied

This is the presentation website for a City Review Application. Citizfied uses HTML/CSS/JS/Python/Flask/MongoDB and is an educational project that serves as the Milestone Project 3 for the **Full-Stack Software Development** program powered by **Code Institute**.

## Demo 

[Live Website](https://citizfied.herokuapp.com/)

![Am I Responsive](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/amiresponsive.jpg)

## UX

### __Business Goals__

  To build an application that:
-   offers people the chance to rate and review any city in any country in the world based on their own experience.
-   allows the visitors to read reviews of places they would like to visit.
-	stands as an online places-to-visit guide based on its users reviews.

### __Customer Goals__

-	Learn about places they would like to visit from reviews uploaded by other human beings.
-	Create their own account which they can use to submit reviews to any city they have visited.
-	Manage their submitted reviews via an account panel.
-   Look up reviews using a search engine.

### __Scope__

* __Functional requirements:__

    -  Option to easily navigate through the pages and content;
    -  Option to search the web for desired meals/recipes;
    -  Option to view social media accounts;
    -  Option to submit queries/recipes via contact form;

* __Content requirements:__

    -	Compelling content that communicates the purpose of the website;
    -	Content flexibility for easier scanning;
    -	Mixed media content for easy understanding of concepts presented;
    -	Various CTAs;

### __User Stories__

1.	"As a first-time visitor, I want to navigate through your website quickly and efficiently."
2.	"As a first-time visitor, I want to easily understand the purpose of your website."
3.	“As a first-time visitor, I want to be able to register to your website in order to make use of all its features.”
4.	"As a user, I want to be able to submit, edit and/or delete content to your website."
5.	“As a user, I want to look up other user’s reviews using a search engine.”
6.	"As a frequent visitor, I want to be able to access your website across a range of devices."

### __Structure__

The website is designed to be intuitive and learnable

1.	Interaction design:
-	The interface responds to the user actions as expected. The scroll/swipe functional behaviour is standard and the buttons respond instantly when actioned;
-	Subtle visual feedback will be added throughout the page in order to increase the user's interaction experience;
2.	Information architecture:
-	The content is organised in order of importance, from top to bottom and left to right
-	The information is structured in nested lists.

### __Skeleton__

* Wireframes

  * [Mobile View](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/mobile-wireframe.jpg)
  * [Tablet View - Home Page](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/tablet-home.jpg)
  * [Tablet View - Write A Review](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/tablet-writeareview.jpg)
  * [Tablet View - Profile Page](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/tablet-profile.jpg)
  * [Desktop View - Home Page](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/desktop-home.jpg)
  * [Desktop View - Write A Review](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/desktop-writeareview.jpg)
  * [Desktop View - Profile Page](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/desktop-profile.jpg)
 

### __Design Choices__

* Colors
  
![Colors](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/coolors-palette.png)

* Typography
  
* One general font was used for this project, with a ```serif``` fallback. A second font was used to create the website's logo.
  * [Otomanopee One](https://fonts.google.com/specimen/Otomanopee+One).
  * [Mukta](https://fonts.google.com/specimen/Mukta?query=mukta)

* Media
  
  * Images used throughout the project are relevant to the purpose of the website.
  * All images have been resized and compressed in order to boost the UX flow.

* Iconography
  * Icons have been used throughout the website in order to boost the UX efficiency.

### __Features__

### __Database__

The MongoDB database used for this project is document-based as a relational database is not needed.

![DB Schema](https://github.com/alexandruvalentin/Citizfied/blob/main/readme-images/db-schema.png)

### __Technologies Used__

- Workspace
  * [Visual Studio Code](https://code.visualstudio.com/) as Integrated Development Environment

- Languages
  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS)
  * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- Frameworks & Libraries
  * [Font Awesome](https://fontawesome.com/) icons were used to improve aesthetics and [UX](#ux)
  * [Google Fonts](https://fonts.google.com/) was used as the main font source
  * [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) was used for its responsiveness and styling classes
  * [Flask](https://flask.palletsprojects.com/en/2.0.x/) was used as a back-end framework
  * Python modules:
    * [pymongo](https://pymongo.readthedocs.io/en/stable/) and [flask-pymongo](https://flask-pymongo.readthedocs.io/en/latest/) were used to connect the app to a MongoDB databse

- Version Control
  * [Github](https://github.com/) for hosting the repository.

- Wireframes
    * [Balsamiq](https://balsamiq.com/) was used to create the wireframes

- Media
    * [Coolors](https://coolors.co/) was used to create the color palette
    * [Compress JPEG](https://compressjpeg.com/) was used to compress images size
    * [dbdiagram.io](https://dbdiagram.io/home) was used to create the database diagram

### __Testing__

 - ### Click [here] for the full testing process.

### __Deployment__

- ### Forking the GitHub Repository
  By forking the GitHub Repository you make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository by using the following steps:
  1. Log in to GitHub and locate the [Citizfied Repository](https://github.com/alexandruvalentin/Citizfied);
  2. At the top right of the Repository just above the "Settings" Button on the menu, locate and click the "**Fork**" Button;
  3. You should now have a copy of the original repository in your GitHub account;

- ### Local Machine
  1. Log in to GitHub and locate the [Citizfied Repository](https://github.com/alexandruvalentin/Citizfied)
  2. At the top of the Repository just above the list of files, locate and click the "**Code**" dropdown;
  3. To clone the repository using HTTPS, under "**Clone**", make sure "**HTTPS**" is selected and copy the link;
  4. Open Git Bash;
  5. Change the current working directory to the location desired for the directory creation;
  6. Type ```git clone```, and then paste in the URL from the clipboard(Step 3);
      ```bash
      git clone https://github.com/alexandruvalentin/Citizfied.git
      ```
  7. Press Enter. Your local clone will be created.
      ```bash
      $ git clone https://github.com/alexandruvalentin/Citizfied.git
      Cloning into 'Citizfied'...
      remote: Enumerating objects: 408, done.
      remote: Counting objects: 100% (408/408), done.
      remote: Compressing objects: 100% (258/258), done.
      remote: Total 408 (delta 156), reused 368 (delta 116), pack-reused 0
      Receiving objects: 100% (408/408), 24.92 MiB | 15.71 MiB/s, done.
      Resolving deltas: 100% (156/156), done.
      ```
      > Click [Here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.
  8. Create account:
      - [MongoDB](https://www.mongodb.com/) account, project, cluster and database;
  9.  Create the `env.py` file and include the following code (note that the values should be replaced with your own credentials)
      ```python
      import os

      # App IP and PORT
      os.environ.setdefault("IP", "0.0.0.0")
      os.environ.setdefault("PORT", "5000")
      # Generate a secret key, use https://randomkeygen.com/
      os.environ.setdefault("SECRET_KEY", "<secret_key>")
      # Mongo DB credentials
      os.environ.setdefault("MONGO_URI", "<mongo_uri>")
      os.environ.setdefault("MONGO_DBNAME", "<db_name>")
      # Admin panel user and password
      os.environ.setdefault("ADMIN_USERNAME", "<username>")
      os.environ.setdefault("ADMIN_PASSWORD", "<password>")
      # AWS Keys
      os.environ.setdefault('AWS_ACCESS_KEY_ID', '<access_key>')
      os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<secret_key>')
      os.environ.setdefault('S3_BUCKET_NAME', '<bucket_name>')
      # Email credentials. See mail_settings in app.py for more email settings
      os.environ.setdefault("SENDGRID_API_KEY", "<api_key>")
      os.environ.setdefault("MAIL_DEFAULT_SENDER", "<sender_email>")
      # Recaptcha keys. Go to https://www.google.com/recaptcha/admin/create and create a new site
      os.environ.setdefault("RC_SITE_KEY", "<recaptcha_site_key>")
      os.environ.setdefault("RC_SECRET_KEY", "<recaptcha_secret_key>")
      ```
      > Make sure you add this file to **.gitignore** file so it will not be published.
  10. Install required `python` packages by running the following command into terminal:
      ```bash
      pip3 install -r requirements.txt
      ```
  11. Run app by typing the following into terminal:
      ```bash
      python3 app.py
      ```
  12. Browse app by accessing [0.0.0.0:5000](http://0.0.0.0:5000) into a browser. At this point, if configured right, the app will automatically build the database.

- ### Heroku
  1. Make sure the `requirements.txt` and `Procfile` files are created. If not, type the followings into the terminal:
      ```bash
      pip3 freeze --local > requirements.txt
      ```
      and
      ```bash
      echo web: python app.py > Procfile
      ```
  2. Commit and push changes to forked repository.
  3. Create a [Heroku](https://heroku.com) account and click **New** on top right of the dashboard to **Create a new app**.
  4. Within the newly created app go to **Settings** tab and press **Reveal Config Vars**. Here you can add the variables initially stored into local `env.py` file: IP, SECRET_KEY, MONGO_URI, MONGO_DBNAME, ADMIN_USERNAME, ADMIN_PASSWORD, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME, SENDGRID_API_KEY, MAIL_DEFAULT_SENDER, RC_SITE_KEY, RC_SECRET_KEY.
  5. Go to **Deploy** tab and under the **Deployment method** click on the **Github** icon.
  6. Right under this section, type the `dev.pi` and search for the forked repository into your GitHub account. Select the right repository and click **Connect**.
  7. Under the **Automatic deploys** section, click **Enable Automatic Deploys**. The deployment will be now automatic with every github `push` command.
  8. Under the **Manual deploy** section, click **Deploy Branch** for initial deploy.
  9. You can now browse the deployed app by clicking **Open app** button on top right of the dashboard.

### __Credits__

- ### Media & Content
  - [FREE SVG](https://freesvg.org/) for the footer SVG
  - [Fabrizio Bianchi](http://fabrizio.io/) for creating [Coolors](https://coolors.co/) which was used to create the color palette
  - [Johan Dufour](https://github.com/lutangar) for the [JSON file](https://github.com/lutangar/cities.json/blob/master/cities.json) that was used to import countries and cities from
  - [CMDW](https://codepen.io/cmdw) for creating the [content divider](https://codepen.io/cmdw/pen/vQqzyB) used in the hero section
  - [Niche](https://www.niche.com/) as a source of inspiration
- ### Code
  - [CSS TRICKS](https://css-tricks.com/) as a general resource.
  - [Stack Overflow](https://stackoverflow.com/) as a general resource.
  - [W3Schools](https://www.w3schools.com/) as a general resource.

### __Acknowledgements__