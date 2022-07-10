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

<details><summary>Desktop Landing Page</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657485555/static/images/funginews%20img/6md6c2_gw5ep4.gif">