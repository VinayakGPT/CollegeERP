from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from dbms.views import CustomLoginView
from dbms.views import (
    home,
    student_view,
    certificate_view,
    feedback_view,
    library_management_view,
    website_management_view,
    department_list, department_create,
    news_notice_list, news_notice_create,
    faculty_list, faculty_create,
    image_gallery_list, image_gallery_create,
    video_gallery_list, video_gallery_create,
    library_inventory_list, library_member_list,
    grievance_list,
    feedback_list,
    show_marks,
    show_students,
    show_admissions,
    show_courses,
    show_fees,
    show_grievances,
    show_feedback,
    show_enquiries,
    show_inventory,
    show_members,
    show_fines,
    show_issued_books,
    show_certificates,
    show_applications,
    show_news_notices,
    show_departments,
    show_sliders,
    show_tickers,
    show_gallery,
    show_videos,
    show_faculty,
    about, contact,
    course_list,
    admin_dashboard, faculty_dashboard, student_dashboard,
    s_student_view, s_library_management_view,s_show_marks,
    s_feedback_view, f_student_view, f_library_management_view,
    f_feedback_view, s_issued_books_view, s_show_feedback,
    f_show_feedback, s_show_courses, f_show_courses,f_show_marks,show_assignment,add_marks,update_marks,delete_marks
    
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),  # Root page is now the login page
    path('home/', home, name='home'),  # Ensure there's a route for the home page
    path('certificate/', certificate_view, name='certificate'),
    path('feedback/', feedback_view, name='feedback'),
    path('student/', student_view, name='student'),
    path('library/', library_management_view, name='library'),
    path('management/', website_management_view, name='management'),
    path('departments/', department_list, name='department_list'),
    path('departments/create/', department_create, name='department_create'),
    path('news-notices/', news_notice_list, name='news_notice_list'),
    path('news-notices/create/', news_notice_create, name='news_notice_create'),
    path('faculty/', faculty_list, name='faculty_list'),
    path('faculty/create/', faculty_create, name='faculty_create'),
    path('image-gallery/', image_gallery_list, name='image_gallery_list'),
    path('image-gallery/create/', image_gallery_create, name='image_gallery_create'),
    path('video-gallery/', video_gallery_list, name='video_gallery_list'),
    path('video-gallery/create/', video_gallery_create, name='video_gallery_create'),
    path('library/inventory/', library_inventory_list, name='library_inventory_list'),
    path('library/members/', library_member_list, name='library_member_list'),
    path('grievances/', grievance_list, name='grievance_list'),
    path('show-students/', show_students, name='show_students'),
    path('show-admissions/', show_admissions, name='show_admissions'),
    path('show-courses/', show_courses, name='show_courses'),
    path('show-fees/', show_fees, name='show_fees'),
    path('show-marks/', show_marks, name='show_marks'),
    path('show-grievances/', show_grievances, name='show_grievances'),
    path('show-feedback/', show_feedback, name='show_feedback'),
    path('show-enquiries/', show_enquiries, name='show_enquiries'),
    path('show-inventory/', show_inventory, name='show_inventory'),
    path('show-members/', show_members, name='show_members'),
    path('show-fines/', show_fines, name='show_fines'),
    path('show-issued-books/', show_issued_books, name='show_issued_books'),
    path('show-certificates/', show_certificates, name='show_certificates'),
    path('show-applications/', show_applications, name='show_applications'),
    path('show-news-notices/', show_news_notices, name='show_news_notices'),
    path('show-departments/', show_departments, name='show_departments'),
    path('show-sliders/', show_sliders, name='show_sliders'),
    path('show-tickers/', show_tickers, name='show_tickers'),
    path('show-gallery/', show_gallery, name='show_gallery'),
    path('show_videos/', show_videos, name='show_videos'),
    path('show-faculty/', show_faculty, name='show_faculty'),
    path('show_assignment/', show_assignment, name='show_assignment'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('faculty_dashboard/', faculty_dashboard, name='faculty_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('s_student/', s_student_view, name='s_student'),
    path('s_library/', s_library_management_view, name='s_library'),
    path('s_feedback/', s_feedback_view, name='s_feedback'),
    path('s_show_marks/', s_show_marks, name='s_show_marks'),
    path("s_issued_books_view/",s_issued_books_view,name = "s_issued_books_view"),
    path('s_show_courses/', s_show_courses, name='s_show_courses'),
    path("s_show_feedback/", s_show_feedback, name="s_show_feedback"),
    path('f_student/', f_student_view, name='f_student'),
    path('f_library/', f_library_management_view, name='f_library'),
    path('f_feedback/', f_feedback_view, name='f_feedback'),
    path('show_assignments/', website_management_view, name='show_assignments'),
    path('f_show_feedback/', f_show_feedback, name='f_show_feedback'),
    path('f_show_courses/', f_show_courses, name='f_show_courses'),
    path('f_show_marks/', f_show_marks, name='f_show_marks'),
    path('course_list/', course_list, name='course_list'),
    path('add_marks/',add_marks,name="add_marks"),
    path('update_marks/',update_marks,name = "update_marks"),
    path('delete_marks/',delete_marks,name = "delete_marks"),
    
]