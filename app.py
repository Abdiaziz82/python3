from flask import Flask,request,current_app,make_response, jsonify, render_template
# Create Flask app instance
app = Flask(__name__) 

# Simulate request context for testing
# because request object becomes available
# only when a request is made
with app.test_request_context('/test'):
    print(request.method)  # Print HTTP method
    print(request.path)    # Print request path
    print(current_app.name)  # Print app name

@app.route('/my_request')  # Route to display request info
def requet_page():
    request_url = request.url  # Get full URL
    request_method = request.method  # Get HTTP method
    remote_address = request.remote_addr  # Get client IP
    user_agent = request.headers.get("User-Agent")  # Get user agent
    cookie = request.headers.get('Cookie')  # Get cookies
    accept = request.headers.get('Accept')  # Get accept header
    host = request.headers.get('Host')  # Get host header

    return f"""
    <h1>Request url :  {request_url}</h1>
    <h1>Request method  :  {request_method}</h1>
    <h1>Request ip_address:  {remote_address}</h1>
    <h1>Request agent:  {user_agent}</h1>
    <h1>Request cookie:  {cookie}</h1>
    <h1>Request accept:  {accept}</h1>
    <h1>Request host:  {host}</h1>
    
"""
@app.before_request   # Runs before every request
def allow_client_by_ip():
    allowed_ips = ['127.0.0.1' ,'127.0.0.2']  # IP whitelist
    request_ip = request.remote_addr  # Get client IP
    if request_ip not in allowed_ips:
        return jsonify("access denied") ,403  # Block unauthorized IPs
    else:
        print (f"welcome : {request_ip}")  # Log allowed IP
    

@app.route('/test_response')  # Route for custom response
def test_response():
    response = make_response("This is the response")  # Create response object
    response.status_code = 201  # Set status code
    response.headers['X-Powered-By'] = "Flask"  # Add custom headers
    response.headers['Content-Type'] = 'text/html'
    response.headers['Server'] = 'WSGI'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Cookie'] = ["userId: 22222"]
    return response
    
@app.after_request  # Runs after every request
def after(response):
    print("after req")  # Log after request
    return response
  
    
@app.route('/')  # Home route
def home():
    return render_template('index.html')  # Render HTML template

# @app.route('/my_request')  # Route to display request info
# def requet_page():
#     request_url = request.url  # Get full URL
#     request_method = request.method  # Get HTTP method
#     remote_address = request.remote_addr  # Get client IP
#     user_agent = request.headers.get("User-Agent")  # Get user agent
#     cookie = request.headers.get('Cookie')  # Get cookies
#     accept = request.headers.get('Accept')  # Get accept header
#     host = request.headers.get('Host')  # Get host header

#     return f"""
#     <h1>Request url :  {request_url}</h1>
#     <h1>Request method  :  {request_method}</h1>
#     <h1>Request ip_address:  {remote_address}</h1>
#     <h1>Request agent:  {user_agent}</h1>
#     <h1>Request cookie:  {cookie}</h1>
#     <h1>Request accept:  {accept}</h1>
#     <h1>Request host:  {host}</h1>
    
# """

@app.route('/about')  # Static about route
def about_page():
    return "this is the about page"

@app.route('/about/home')  # Nested about route
def about_home():
    return "this is the about on home page"

@app.route('/<string:name>')  # Dynamic string parameter
def user_profile(name):
    return f"Welcome {name}"

@app.route('/courses/<int:course_id>')  # Dynamic integer parameter
def course_details(course_id):
    return f"welcome to the course {course_id}"

if __name__ == "__main__":  # Run only if script executed directly
    app.run(port = 5002, debug = True)  # Start server on port 5002 with debug mode