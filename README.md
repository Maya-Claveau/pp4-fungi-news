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

## **Code validation**

CSS code passes the validator without errors, however, there are some warnings, please see details in the screenshot. I looked into them, and don’t really know how to fix them at the moment, so I just left them there.

<details>
<summary>CSS</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527876/static/images/funginews%20img/testing/css/css_d3lklc.jpg">
<summary>CSS warnings</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527876/static/images/funginews%20img/testing/css/css_warnings_w5bhwy.jpg">
</details>


<details><summary>HTML</summary>
<summary>index.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527874/static/images/funginews%20img/testing/html/index_yvksha.jpg">
<summary>contact.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527874/static/images/funginews%20img/testing/html/contact_hzzg0l.jpg">
<summary>all_posts.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527874/static/images/funginews%20img/testing/html/blog_lortns.jpg">
<summary>signup.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527875/static/images/funginews%20img/testing/html/sign_up_kmyfyk.jpg">
<summary>login.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527875/static/images/funginews%20img/testing/html/login_p9h95q.jpg">
<summary>logout.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527874/static/images/funginews%20img/testing/html/log_out_chu8cg.jpg">
<summary>shared_posts.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527875/static/images/funginews%20img/testing/html/my_posts-_fixed_canjlu.jpg">
<summary>add_post.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527874/static/images/funginews%20img/testing/html/add_post_without_summernote_hywcxv.jpg">
<summary>update_post.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657532711/static/images/funginews%20img/testing/html/update_post_tgvpve.jpg">
<summary>delete_post.html</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657532826/static/images/funginews%20img/testing/html/delete_post_bsijrm.png">
</details>

<details><summary>Python</summary>
<summary>Blog - Admin.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527877/static/images/funginews%20img/testing/python/admin.py_vicyur.jpg">
<summary>Blog - apps.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527877/static/images/funginews%20img/testing/python/app.py_pltlt8.jpg">
<summary>Blog - forms.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527877/static/images/funginews%20img/testing/python/forms.py_dulqvh.jpg">
<summary>Blog - models.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527878/static/images/funginews%20img/testing/python/models.py_fvc5r0.jpg">
<summary>Blog - urls.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527878/static/images/funginews%20img/testing/python/urls.py-blog_yh1nnn.jpg">
<summary>Blog - views.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527878/static/images/funginews%20img/testing/python/views.py_uflxmz.jpg">
<summary>Funginews - asgi.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527877/static/images/funginews%20img/testing/python/asgi.py_mhmakf.jpg">
<summary>Funginews - settings.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527878/static/images/funginews%20img/testing/python/settings.py_pcpbpp.jpg">
<summary>Funginews - urls.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527878/static/images/funginews%20img/testing/python/urls.py-funginews_kmtpx7.jpg">
<summary>Funginews - wsgi.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527879/static/images/funginews%20img/testing/python/wsgi.py_fnwfqi.jpg">
<summary>Register - apps.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527877/static/images/funginews%20img/testing/python/apps.py_-_register_qqmtnc.jpg">
<summary>Register - forms.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527877/static/images/funginews%20img/testing/python/forms.py_-_register_ysh9ay.jpg">
<summary>Register - views.py</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527878/static/images/funginews%20img/testing/python/views.py_-_register_jkzaop.jpg">
</details>
