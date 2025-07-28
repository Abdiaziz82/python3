from flask import Blueprint,session ,jsonify,make_response ,request

user_session = Blueprint('user_session' ,__name__)

@user_session.route('/set_student/<string:name>/<string:role>')
def set_student(name,role):
    session.permanent = True  # Make the session permanent
    session['student_name'] = session.get('student_name',name)
    session['student_role'] = session.get('student_role',role)

    response = make_response(jsonify({
        "message" :f"session set for {name} with role {role}",
        "where created" :{
            "session" : {
                "student_name" : session['student_name'],
                "student_role" : session['student_role'],
            },
            "cookie" :"preference=darktheme"
        }
    }))
    response.set_cookie('preference', 'darktheme')
    return response

@user_session.route('/get_student')
def get_student():
    student_name = session.get('student_name',"name")
    student_role = session.get('student_role')
    preference = request.cookies.get('preference' )
    
    response = make_response(jsonify({
        'from session' :{
            'student_name' :student_name,
            'student_role' :student_role,  
        },
        'from cookies':{
            'preference':preference
        },
        "all_cookies":dict(request.cookies)
        
            }))
    return response                