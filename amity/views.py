from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from adminpanel.models import ContactUS, GlobalSettings, Navigation
from django.contrib import messages
from django.core.paginator import Paginator

def Main(request):
    return render(request, "amity_global/index.html")
                  
def Base(request):
    pop = True
    pop = Navigation.objects.filter(status='Publish', page_type='Pop')
    glob = GlobalSettings.objects.all()
    sli = Navigation.objects.filter(status='Publish', page_type='Home')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    abo = Navigation.objects.filter(status='Publish', page_type='Home/About')
    ser = Navigation.objects.filter(status='Publish', page_type='Amity/Service')
    our = Navigation.objects.filter(status='Publish', page_type='Our Service')
    req = Navigation.objects.filter(status='Publish', page_type='Requirement')
    ten = Navigation.objects.filter(status='Publish', page_type='Talent')
    pool = Navigation.objects.filter(status='Publish', page_type='UNSKILLED LABOUR')
    pool1 = Navigation.objects.filter(status='Publish', page_type='THE PROFESSIONALS')
    pool2 = Navigation.objects.filter(status='Publish', page_type='SEMI-SKILLED STAFF')
    cont = Navigation.objects.filter(status='Publish', page_type='COUNTRIES')
    test = Navigation.objects.filter(status='Publish', page_type='TESTIMONIAL')
    title = Navigation.objects.filter(status='Publish', page_type='Home1')
    ser1 = Navigation.objects.filter(status='Publish', page_type='Home2')
    ser2 = Navigation.objects.filter(status='Publish', page_type='Home3')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    test1 = Navigation.objects.filter(status='Publish', page_type='Home5')
    con1 = Navigation.objects.filter(status='Publish', page_type='Home6')
    bro = Navigation.objects.filter(status='Publish', page_type='Normal')


    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
    
    
    return render(request, "amity_global/home.html", {'main':main,'glob':glob,'sli':sli,'ven':ven,'pop':pop,'pool':pool,'pool1':pool1,
                                                    'pop':pop,'ten':ten,'pool2':pool2,'abo':abo,'ser':ser,'our':our,'req':req,
                                                    'test':test,'cont':cont,'title':title,'ser1':ser1,'ser2':ser2,
                                                    'ven1':ven1,'test1':test1,'con1':con1,'bro':bro})
def redirect_to_url(request, name):
    if name == '17':
       return redirect('about')
    elif name == '18':
        return redirect('legaldoc')
    elif name == '19':
        return redirect('massage_cha')
    elif name == '20':
        return redirect('commitment')
    elif name == '21':
        return redirect('vision')
    elif name == '22':
        return redirect('mission')
    elif name == '23':
        return redirect('org_chart')
    elif name == '24':
        return redirect('demand')
    elif name == '25':
        return redirect('recru_procedure')
    elif name == '26':
        return redirect('recu_documents')
    elif name == '163':
        return redirect('unskilled')
    elif name == '164':
        return redirect('semiskilled')
    elif name == '165':
        return redirect('skilled')
    # elif name == '166':
    #     return redirect('highskilled')
    elif name == '200':
        return redirect('Newspaperpub')
    elif name == '47':
        return redirect('gallery')
    elif name == '124':
        return redirect('contact')
    else:
        return HttpResponse("Id not Matched")

def about(request):
    glob = GlobalSettings.objects.all()
    abo = Navigation.objects.filter(status='Publish', page_type='About Company')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/about/about.html", {'main':main,'glob':glob, 'abo':abo,'ven':ven,'ven1':ven1})

def legaldoc(request):
    glob = GlobalSettings.objects.all()
    leg = Navigation.objects.filter(status='Publish', page_type='Registration/Approval')
    page = Navigation.objects.filter(status='Publish', page_type='Normal')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    legal = Navigation.objects.filter(status='Publish', page_type="Registration/Approval")
    paginator = Paginator(legal, 6)  # Show 6 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "amity_global/about/legaldoc.html", {'main':main,'glob':glob,'leg':leg,'page':page,'page_obj':page_obj,'ven':ven,'ven1':ven1})

def massage_cha(request):
    glob = GlobalSettings.objects.all()
    mass = Navigation.objects.filter(status='Publish', page_type='Our Message')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/about/massage_cha.html", {'main':main,'glob':glob,'mass':mass,'ven':ven,'ven1':ven1})

def commitment(request):
    glob = GlobalSettings.objects.all()
    com = Navigation.objects.filter(status='Publish', page_type='Our Commitment')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/about/commitment.html", {'main':main,'glob':glob,'com':com,'ven':ven,'ven1':ven1})

def vision(request):
    glob = GlobalSettings.objects.all()
    vis = Navigation.objects.filter(status='Publish', page_type='Vision')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/about/vision.html", {'main':main,'glob':glob,'vis':vis,'ven':ven,'ven1':ven1})

def mission(request):
    glob = GlobalSettings.objects.all()
    mis = Navigation.objects.filter(status='Publish', page_type='Mission')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/about/mission.html", {'main':main,'glob':glob,'mis':mis,'ven':ven,'ven1':ven1})

def org_chart(request):
    glob = GlobalSettings.objects.all()
    org = Navigation.objects.filter(status='Publish', page_type='Organizational Chart')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/about/org_chart.html", {'main':main,'glob':glob,'org':org,'ven':ven,'ven1':ven1})

def demand(request):
    glob = GlobalSettings.objects.all()
    dem = Navigation.objects.filter(status='Publish', page_type='Demand Letter')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/document/demand.html", {'main':main,'glob':glob,'dem':dem,'ven':ven,'ven1':ven1})

def recru_procedure(request):
    glob = GlobalSettings.objects.all()
    recru = Navigation.objects.filter(status='Publish', page_type='Recruitment')
    proce = Navigation.objects.filter(status='Publish', page_type='Recruiting Procedure')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/document/recru_procedure.html", {'main':main,'glob':glob,'recru':recru,'proce':proce,'ven':ven,'ven1':ven1})

def recu_documents(request):
    glob = GlobalSettings.objects.all()
    rec = Navigation.objects.filter(status='Publish', page_type='Recruiting Documents')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/document/recu_documents.html", {'main':main,'glob':glob,'rec':rec,'ven':ven,'ven1':ven1})

def Newspaperpub(request):
    glob = GlobalSettings.objects.all()
    new = Navigation.objects.filter(status='Publish', page_type='Newspaper Vacancy')
    new1 = Navigation.objects.filter(status='Publish', page_type='News')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    news = Navigation.objects.filter(status='Publish', page_type="Newspaper Vacancy")
    news = news.order_by('-id')  # Order by the primary key in descending order
    paginator = Paginator(news, 6)  # Show 6 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "amity_global/Newspaperpub.html", {'main':main,'glob':glob,'new':new,'new1':new1,'page_obj':page_obj,'ven':ven,'ven1':ven1})

def gallery(request):
    glob = GlobalSettings.objects.all()
    gall = Navigation.objects.filter(status='Publish', page_type='Gallery')
    gall1 = Navigation.objects.filter(status='Publish', page_type='Gall')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    gallery = Navigation.objects.filter(status='Publish', page_type="Gallery")
    gallery = gallery.order_by('-id')  # Order by the primary key in descending order
    paginator = Paginator(gallery, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "amity_global/gallery.html", {'main':main,'glob':glob, 'gall':gall,'gall1':gall1,
                                                         'page_obj':page_obj,'ven':ven,'ven1':ven1})

def contact(request):
    glob = GlobalSettings.objects.all()
    conn = Navigation.objects.filter(status='Publish', page_type='Contact')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
    
    if request.method=="POST":
        message=request.POST.get('message')
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')

        if len(name)<2 or len(email)<3 or len(subject)<4 or len(message)<2:
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            con=ContactUS(name=name,email=email,subject=subject,message=message)
            con.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request, "amity_global/contact.html", {'main':main,'glob':glob,'conn':conn,'ven':ven,'ven1':ven1})  

def country(request,id):
    glob = GlobalSettings.objects.all()
    cont = Navigation.objects.filter(status='Publish', id=id)
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
    
    return render(request, "amity_global/contry.html", {'main':main,'glob':glob,'cont':cont,'ven':ven,'ven1':ven1})

def service(request):
    glob = GlobalSettings.objects.all()
    ser = Navigation.objects.filter(status='Publish', page_type='Service')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/service.html", {'main':main,'glob':glob,'ser':ser,'ven':ven,'ven1':ven1})

def unskilled(request):
    glob = GlobalSettings.objects.all()
    un =Navigation.objects.filter(status='Publish', page_type='UNSKILLED')
    page =Navigation.objects.filter(status='Publish', page_type='Job')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/Job_Category/unskilled.html", {'main':main,'glob':glob,'un':un,'page':page,'ven':ven,'ven1':ven1})

def skilled(request):
    glob = GlobalSettings.objects.all()
    skill =Navigation.objects.filter(status='Publish', page_type='SKILLED')
    page =Navigation.objects.filter(status='Publish', page_type='Job2')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/Job_Category/skilled.html", {'main':main,'glob':glob,'skill':skill,'page':page,'ven':ven,'ven1':ven1})

def semiskilled(request):
    glob = GlobalSettings.objects.all()
    sem =Navigation.objects.filter(status='Publish', page_type='SEMI-SKILLE')
    page =Navigation.objects.filter(status='Publish', page_type='Job1')
    ven = Navigation.objects.filter(status='Publish', page_type='Home')
    ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "amity_global/Job_Category/semi-skilled.html", {'main':main,'glob':glob,'sem':sem,'page':page,'ven':ven,'ven1':ven1})

# def highskilled(request):
#     glob = GlobalSettings.objects.all()
#     high =Navigation.objects.filter(status='Publish', page_type='HIGHLYSKILLED')
#     page =Navigation.objects.filter(status='Publish', page_type='Job3')
#     ven = Navigation.objects.filter(status='Publish', page_type='Home')
#     ven1 = Navigation.objects.filter(status='Publish', page_type='Home4')
#     main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

#     return render(request, "amity_global/job_Category/highly-skilled.html", {'main':main,'glob':glob,'high':high,'page':page,'ven':ven,'ven1':ven1})



