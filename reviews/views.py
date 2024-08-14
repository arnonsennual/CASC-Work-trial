from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse
from reviews.models import ReviewForm,Course,Review,University

# Create your views here.

#List of the University
def index(request):
    university_list = University.objects.all()
    print(university_list)

    return render(request, 'index.html', {'university_list': university_list})

#University Details
def university(request, university_id):
    university = get_object_or_404(University, id = university_id)
    university_name = (university.name)
    print(university_name)
    reviews = Review.objects.filter(university_id = university.id)
    return render(request,  'university_page.html', {'university_name': university_name, 'reviews':reviews})


def submit_review(request, link_id):
    # Get the ReviewForm instance
    link = get_object_or_404(ReviewForm, id=link_id)

    # Check if the form has already been used
    if link.is_used:
        # Return a custom message or render a template with the message
        return HttpResponse("You have already submitted the form. Please contact admin if you need to edit or resubmit.")

    # Proceed with form processing
    reviewer_study_at = link.reviewer.study_at
    university_id = link.reviewer.study_at.id
    course = link.reviewer.course
    print(course)
    
    
    if request.method == 'POST':
        
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        # Print form data (for debugging purposes)
        #course = get_object_or_404(Course, id=course)
        university_id = get_object_or_404(University , id= university_id)

        #Create Actul review data
        new_review = Review(
            course_id = course,
            star=float(rating),
            desc=comment,
            is_show=True,
            university_id = university_id
        )
        new_review.save()


        #Update URL is_used
        link.is_used = True
        link.save()

        # Redirect to a success page or another view
        return redirect('index') 

    else:
        return render(request, 'review.html', {'course': course, 'university': reviewer_study_at, 'link_id': link_id})