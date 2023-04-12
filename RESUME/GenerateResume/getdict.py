from .models import *


def getAllDict(u_id=100):
    user1=userinfo.objects.get(uid=u_id)
    skill=skills.objects.filter(uid=u_id),
    languge = languages.objects.filter(uid=u_id),
    project = projects.objects.filter(uid=u_id),
    spec = specializations.objects.filter(uid=u_id),
    works = workexp.objects.filter(uid=u_id).values_list('workname')

   
    datas = {'Name':user1.name,'phone':user1.phone,'mail':user1.mail,'address':user1.address,'about':user1.about,'skills':[s.skillname for sk in skill for s in sk],
             'language':[l.langname for lan in languge for l in lan],'projects':[p.proj for proj in project for p in proj],
             'spec':[s.specname for sp in spec for s in sp]
             }
    return datas
    

