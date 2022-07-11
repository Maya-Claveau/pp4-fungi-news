# Welcome to **[Fungi News](https://funginews.herokuapp.com/)**

<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657461423/static/images/mockup_tvfbue.jpg" width="800">

Curious to see what I have built? [Here](https://funginews.herokuapp.com/) is deployed link.

## **Purpose of the site**
<p>This site is a blog style news site, aimed to let users keep up with the fast changing digital world within the NFT realm.</p>

 Site owner’s main objectives are:
- to inform users about what’s happening in NFT world
- to educate users about what is NFT, what can you do with it
- to increase users’  interests and curiosity about NFT and blockchain technology in general
- to provide a platform for users to share posts, comments and interact with each other
- to create a community with people that has common interests in this technology

Site user’s main objectives are:
- to keep up with the NFT trendy news
- to meet other like minded people
- to interact and discuss with other people on this topic
- to learn from each other about this technology
- to share posts, ideas, opinions with people who understand you
- to show your passion to other people who don’t know a lot about it and want to learn

------

## **Why This**

<p>NFT is fairly new technology, the very first NFT was created back in 2014, then minted on the blockchain, it was sold for $4. Fast forward 8 years later today, NFT art is sold at millions of dollars, there are more and more people showing interest in this new technology. Big tech companies are building virtual universes even, who knows what else can be built with this.</p>

<p>I decided to build this project, because I personally believe this is our future, and I would like more people to be aware of this, get interested and try to understand it. For those who have the same interests as me, I hope this site can be a place to share and exchange information, knowledge and opinions about NFT and blockchain in general, so we get to know it better together.</p>

------

## **Project planning**
<br>

### **User Stories**
The tasks users can perform depends on their role. On this site, there are admin, first time user and returned users, tasks that they have the authorization to perform are shown in below table, as well as their associated User Stories from [Github](https://github.com/Maya-Claveau/pp4-fungi-news/projects/1).


<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657478028/static/images/user_stories_with_tasks_xmsacw.jpg" width="800">

#### **Logic**
I decided that any new post added by the user need approval, reasons being:
- I have no one to moderate the post, that is the reason any posts coming from user needs to be approved by admin first
- To prevent spam, and/or post that is unrelated to nft
- To make sure the language is appropriate
- To reach the max storage in database in short time period filled with trash data
- A bot can post massive amount of trash post which will cause the website been taken down
- Last but not least, because of this nature, in the admin panel under post, the drop down menu only has the delete option, without “approval selected posts”, because naturally you would have to go through the content before approving the post.

<br>

### **Database Structure**

Below is the Database structure that this project is based on. There are User, Post and Comment tables, you can also see their relationships between each table.

<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657479550/static/images/database_structure_au8tqz.jpg" width="800">

<br>

### **WireFrames**

<details><summary>Desktop Wireframes</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480163/static/images/funginews%20img/desktop-home-page_p8qztm.jpg" width="800">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480163/static/images/funginews%20img/desktop-home-page-pt2_cwdbgn.jpg" width="800">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480163/static/images/funginews%20img/desktop-signup-form_b0mpnc.jpg" width="800">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480163/static/images/funginews%20img/desktop-login-form_tn1jr5.jpg" width="800">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480163/static/images/funginews%20img/desktop-home-page-footer_hg331a.jpg" width="800">
</details>

<details><summary>Mobile Wireframes</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480164/static/images/funginews%20img/mob-home-page_pt5hkv.jpg" width="400">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480164/static/images/funginews%20img/mob-hope-page-menu_c55ruj.jpg" width="400">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480164/static/images/funginews%20img/mob-signup_wnjuix.jpg" width="400">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480163/static/images/funginews%20img/mob-signup-form_qbp5en.jpg" width="400">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480164/static/images/funginews%20img/mob-login_dpi4ak.jpg" width="400">
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657480164/static/images/funginews%20img/mob-home-page-footer_gmwbcv.jpg" width="400">
</details>

<br>

### **Font and color**

#### **Font**
I chose Inter because it looked nice and clean, Most importantly, it is easy to read. <details><summary>See here</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657481182/static/images/funginews%20img/font_vhodoz.jpg"></details>

#### **Color**
I chose this colour palette, because it looks simple and classy.
<details><summary>Color palette</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657481510/static/images/funginews%20img/color_palettes_2_nbg3jf.jpg"></details>

------

## **Installations**

Below are the installations we need before writing any code
<br>

Install the server to use when deploy on Heroku
  ```sh
  pip3 install django gunicorn
  ```

Supporting libraries:
  * Postgresql and psycopg2
  ```sh
  pip3 install dj_database_url psycopg2
  ```
  * to run Cloudinary
  ```sh
  pip3 install dj3-cloudinary-storage
  ```
  Creat file list:
  * create requirement.txt
  ```sh
  pip3 freeze --local > requirements.txt
  ```
  * create new django project
  ```sh
  django-admin startproject funginews .
  ```
  * create blog app
  ```sh
  python3 manage.py startapp blog
  ```

## **23 Days Later**

After 23 days of tears and sweat, I can finally present a functional blog site.

By clicking [Fungi News](https://funginews.herokuapp.com/) first thing you will see is the landing page. Here you can see the navbar on the top which has links for Contact us, Blog, Signup or Login.

If you scroll down you will see the articles section with the latest posts, along with info like title, author, a short snippet of the post, date and time when the post was created as well as a number of likes on that particular post.

If you are logged in, you will see two buttons, add post and my post, this will take you to the respective page. If you are not logged in you will just see the footer with social links icons of Twitter, Telegram, Reddit, Instagram, and Facebook. At the very bottom of the page is my Github repo link where you can see all the code and this file to read through how I created this project.

Desktop
<details><summary>Not logged in user</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657529651/static/images/funginews%20img/first_time_user_exiqpj.gif">
</details>

<details><summary>Logged in user</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657529153/static/images/funginews%20img/logged_in_plhf3g.gif">
</details>

<br>

Mobile
<details><summary>Not logged in user
</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657530701/static/images/funginews%20img/new_user-mob_sttoph.gif">
</details>

<details><summary>Logged in User
</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657530701/static/images/funginews%20img/logged_in_mobile_wvp8ii.gif">
</details>

The project evolved by itself during the development stage, and I am made changes since the wireframes were done, and added features that I didn’t think about initially. Overall, I am quite happy about how it turned out.

------

## **Testing**

Testing was conducted continuously throughout the development of this project. Google dev tools were used mainly, to ensure things run smoothly and as expected. More details, please refer to [TESTING.md](TESTING.md) file.

### **Code Validation**
Details on code validation can also be found in the [TESTING.md](TESTING.md) file.

## **Tech Stack**
### **Language**

This project is a Full-Stack site based on business logic used to control a centrally-owned dataset. With the authentication it provide role-based access to the data.

Main programming languages used are:

- **python**
- **Django**
- **HTML**
- **CSS**
- **Javascript**
- **postgresql**
- **psycopg2**

### **Tools**
- [Github](https://github.com/) for store and version control of the code

- [Gitpod](https://gitpod.io/workspaces) for editing code

- [Heroku](https://heroku.com/) for deployment

- [Lucidchart](https://www.lucidchart.com/pages/) for creating database relationship

- [Cloudinary](https://cloudinary.com) for store the images and css files used in this project

- [Lightshot](https://app.prntscr.com/en/index.html) for creating screenshots

- [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/) for generating table of content for README.md file

- [techsini.com](https://techsini.com/multi-mockup/index.php) for generating the mock up

- [Freepik](https://www.freepik.com/) for downloading the nft images

- [Figma](https://www.figma.com/) for making the logo

- [Bootstrap](https://getbootstrap.com/) was used to speed up the design the style and responsiveness of the website


### **Difficulties I manage to overcome**
Below are example of list of things I struggled with, there are many more that were not documented.
- Alert Message doesn’t appear when signup or login
- Like button icon doesn’t appear (font awesome problem)
- Login btn doesn’t work on Login page
- Deployed version: add post button not showing (turns out i wan’t logged in)
- Sticky footer issue
- Display author name when a new post is added: solution add “author” in admin.py file on the list_display field
-  Update and delete wasn’t working: post.slug, and sccess_url = ‘/’
- Display all posts shared by one user: logic – query from the db to specific use.id, ie: select all from posts table in db, then user id
- ContactForm: Contact Form is not working. IntegrityError at /contact/
IntegrityError at /contact NOT NULL constraint failed
- Display message on success submit contact form: https://stackoverflow.com/questions/42848646/show-django-messages-inside-form-invalid-of-formview
- Display a message and share post button when logged in user havn’t share anything yet
- Excerpt issue: remove the summernotewidget solved it

## **Credits**

- Code Institute's [I think therefor I blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)

- Tutor support from Code Institute for helping me out when I got stuck. Special shout out to Ger, who helped me to solve multiple problems that was driving me nuts.

- Fellow students on slack also helped me a lot, is such a amazing community to learn and grow together

- [Stackoverflow](https://stackoverflow.com/) for researching massive amount of things

- Youtube videos for watching people building things with the features I needed, especially the google login part

- Google in general, I can't remember the list of things and webiste I searched

<br>

## **Acknowledgments**
My mentor Mr. ADEGBENGA ADEYE for his continuous structured feedback and support. My project won't be the same without his valuable advice.

Tutor support at Code Institute. They are always there when I need help, I am really grateful for that.

Fellow students on the Slack community for their help and support, this amazing community constantly inspires me and it feels nice to learn and grow with them together.

Most importantly, I would like to thank my husband, my friends Elina and David, who supported me every step in my coding journey, and my son who was a brave boy even when he was sick and I couldn't give him much attention as I should during the last two days of the development of this project.


THANK YOU ALL!!!



Disclaimer: I am aware of this readme is not up to standard, there are tons of things I would like to talk about, and have the notes and screenshots. Unfortunately, I m running out of time and had to do it this way. It is also possible that I missed some credit to the source of my code. Please accept my apology.



