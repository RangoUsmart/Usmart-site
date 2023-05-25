from django.shortcuts import  render, redirect,  get_object_or_404
from .models import MainUserExp, MainUserInfo, MainUserSkill
from django.views.generic.base import View
from .forms import PostForm

# def rezume(request):
#     return render(request, "cv.html")
class RezumeView(View):  
    def get(self, request):
        maininfo = MainUserInfo.objects.all()
        mainexp = MainUserExp.objects.all()
        mainskill =  MainUserSkill.objects.all()
        activeskill = mainskill.filter(skill_status ='a')
        passskill = mainskill.filter(skill_status ='b')
        planskill = mainskill.filter(skill_status ='c')
        return render(request, 'cv.html', {'maininfo': maininfo, 
                                            'mainexp': mainexp, 
                                            'mainskill': mainskill[0:5],
                                            'passskill': passskill,
                                            'planskill': planskill,
                                            'activeskill': activeskill,
                                            
                                        })

def cv_edit(request):
    post = get_object_or_404(MainUserInfo)
    # print(post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.date = timezone.now()
            post.save()
            return redirect(RezumeView.as_view())
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
        
# class Rezume(View):
    
    
    
   
#     def foringetfo(self, request):       
#         maininfo = get_object_or_404(MainUserInfo)
#         return render(request, 'cv.html', {'maininfo': maininfo, 
#                                        })
        
#     def forskill(self, request):     
#         mainskill =  MainUserSkill.objects.all()          
#         return render(request, 'cv.html', {
#                                             'mainskill': mainskill, 
#                                        })
        
#     def forexp(self, request):   
#         mainexp = get_object_or_404( MainUserExp)  
                  
#         return render(request, 'cv.html', {
#                                             'mainexp': mainexp, 
#                                        })