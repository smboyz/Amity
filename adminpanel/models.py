from django.db import models
# from django.utils import timezone

class GlobalSettings(models.Model):
    SiteName = models.CharField(max_length=100)
    SiteContact = models.CharField(max_length=100)
    SiteEmail = models.EmailField()
    SiteAddress = models.CharField(max_length=500)
    Sitedescription = models.CharField(max_length=500)
    Sitelicence = models.CharField(max_length=300)
    Sitetwitterlink = models.CharField(max_length=300)
    Sitefacebooklink = models.CharField(max_length=300)
    Sitelinkdinlink = models.CharField(max_length=300)
    Siteinstagram = models.CharField(max_length=300)
    Siteyoutubelink = models.CharField(max_length=300)
    logo = models.ImageField(upload_to="Global/",max_length=200, null=True, default=None)
    back_image = models.ImageField(upload_to="Global/",null=True)
    brochure = models.FileField(upload_to="brochure/",null=True)
    brochure_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.SiteName

class ContactUS(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
# class Page_Type(models.Model):
#     name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    

class Navigation(models.Model):
    PAGE_TYPE = (
        ('Home', 'Home'),('Vision','Vision'),('Mission','Mission'),('Home/About', 'Home/About'),
        ('Documents', 'Documents'),('About Company','About Company'),('Registration/Approval','Registration/Approval'),
        ('About', 'About'),('Our Message','Our Message'),('Our Commitment','Our Commitment'),('Pop','Pop'),
        ('Contact', 'Contact'),('Organizational Chart','Organizational Chart'),('Demand Letter','Demand Letter'),
        ('Job Seeker', 'Job Seeker'),('Recruiting Procedure','Recruiting Procedure'),('Recruiting Documents','Recruiting Documents'),
        ('Gallery', 'Gallery'),('Slider','Slider'),('Service','Service'),('Amity/Service','Amity/Service'),
        ('Newspaper Vacancy', 'Newspaper Vacancy'),('Our Service','Our Service'),('Requirement','Requirement'),
        ('Group','Group'),('Normal','Normal'),('Talent','Talent'),('UNSKILLED','UNSKILLED'),('THE PROFESSIONALS','THE PROFESSIONALS'),
        ('SEMI-SKILLED','SEMI-SKILLED'),('SKILLED','SKILLED'),('HIGHLYSKILLED','HIGHLYSKILLED'),('TESTIMONIAL','TESTIMONIAL'),('COUNTRIES','COUNTRIES'),
        ('Home1','Home1'),('Job','Job'),('Job1','Job1'),('Job2','Job2'),('Job3','Job3'),('News','News'),('Gall','Gall'),('Recruitment','Recruitment'),
        ('Home2','Home2'),('Home3','Home3'),('Home4','Home4'),('Home5','Home5'),('Home6','Home6'),('UNSKILLED LABOUR','UNSKILLED LABOUR'),('SEMI-SKILLED STAFF','SEMI-SKILLED STAFF'),
    )

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )
    name = models.CharField(max_length=100, null=False)
    caption = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=50)
    position = models.IntegerField()
    page_type = models.CharField(choices=PAGE_TYPE, null=True, blank=True, max_length=50)
    title = models.CharField(max_length=200)
    short_desc = models.TextField(null=True)
    desc = models.TextField(null=True)
    bannerimage = models.ImageField(upload_to="about/",null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    icon_image = models.TextField(null=True)
    slider_image = models.ImageField(upload_to="about/", null=True)
    Parent = models.ForeignKey('self', related_name="childs", on_delete=models.CASCADE, null=True, blank=True)
    brochure = models.FileField(upload_to="brochure/",null=True)

    def __str__(self):
        return self.name

