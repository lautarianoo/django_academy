from django.db.models import Q

from courses.models import Course, Category

def rec_course(user):
    rec_query_course = []
    if user.last_query:
        queries = user.last_query.split(' ').reverse()[:4]
        for query in queries:
            course_on_title = Course.objects.filter(title__icontains=query).distinct()[:8]
            course_on_describe = Course.objects.filter(description__icontains=query).distinct()[:8]

            for course_title, course_describe in zip(course_on_title, course_on_describe):
                rec_query_course.append(course_title)
                rec_query_course.append(course_describe)
    return rec_query_course