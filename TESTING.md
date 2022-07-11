# **Testing**

## **Code Validation**
[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS code

<details>
<summary>CSS</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527876/static/images/funginews%20img/testing/css/css_d3lklc.jpg">
<summary>CSS warnings</summary>
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527876/static/images/funginews%20img/testing/css/css_warnings_w5bhwy.jpg">
</details>
CSS code passes the validator without errors, however, there are some warnings, please see details in the screenshot. I looked into them, and don’t really know how to fix them at the moment, so I just left them there.


[Nu Html checker](https://validator.nu/) for validate HTML code
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


[Pep8](http://pep8online.com/) for validate python code
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

- add post page: I had to remove the summernotewidget on the content field, because although it was working fine, but it does error during the code validation, so I decided to remove it after all.

this is with summernotewidget
<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527874/static/images/funginews%20img/testing/html/add_post_with_summernote_pyoc76.jpg">



this is without summernotewidget

<img src="https://res.cloudinary.com/mayathebee/image/upload/v1657527874/static/images/funginews%20img/testing/html/add_post_without_summernote_hywcxv.jpg">

### **Unfixed bugs:**
Post.object – put it under unfixed bugs Pylint is pythons error message, and unfortunately python can’t see what Django is doing, so as an example, objects are there, python just can’t see that Django is handling the objects.
