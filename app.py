import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cab_agency"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


# Admin page
@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('home.html')


@app.route('/get_cabs')
def get_cabs():
    return render_template('cabs/cabs.html', cabs=mongo.db.cabs.find())


# Add a cab
@app.route('/add_cab')
def add_cab():
    return render_template('cabs/addcab.html', types=mongo.db.types.find(),
                           brands=mongo.db.brands.find(),
                           models=mongo.db.models.find(),
                           bookings=mongo.db.bookings.find())


# Insert a Cab
@app.route('/insert_cab', methods=['POST'])
def insert_cab():
    cabs = mongo.db.cabs
    # get the form and convert to a dictionary
    cabs.insert_one(request.form.to_dict())
    # get the form fields with data in them
    return redirect(url_for('get_cabs'))


# Edit a Cab selection
# pre-populated based on the information returned in the task.
@app.route('/edit_cab/<cab_id>')
def edit_cab(cab_id):
    a_cab = mongo.db.cabs.find_one({"_id": ObjectId(cab_id)})
    # prepolulated based on the collection
    # returned in the types, brands and models cursor
    all_types = mongo.db.types.find()
    all_brands = mongo.db.brands.find()
    all_models = mongo.db.models.find()
    return render_template('cabs/editcab.html', cab=a_cab,
                           types=all_types, brands=all_brands,
                           models=all_models)


# update Cab entry
@app.route('/update_cab/<cab_id>', methods=['POST'])
def update_cab(cab_id):
    # access the database collection
    cabs = mongo.db.cabs
    # call the update function, specify an id
    cabs.update({'_id': ObjectId(cab_id)},
    {
        'vehicle_type': request.form.get('vehicle_type'),
        'brand_name': request.form.get('brand_name'),
        'model_name': request.form.get('model_name'),
        'cab_location': request.form.get('cab_location'),
        'email': request.form.get('email'),
        'tel_nr': request.form.get('tel_nr'),
        'cab_picture': request.form.get('cab_picture')
    })
    return redirect(url_for('get_cabs'))
    # specify the form fields to match the keys on the task collection


# delete a Cab entry
@app.route('/delete_cab/<cab_id>')
def delete_cab(cab_id):
    mongo.db.cabs.remove({'_id': ObjectId(cab_id)})
    return redirect(url_for('get_cabs'))


# find a cab by using a search field
@app.route('/get_one/<cab_id>', methods=['GET'])
def get_one(cab_id):
    cab = mongo.db.cabs
    cab = mongo.db.cabs.find_one({'_id': ObjectId(cab_id)})
    return render_template('cabs/findcab.html', cab=cab)


# get booked cabs
@app.route('/get_bookings')
def get_bookings():
    return render_template('bookings/bookings.html',
                           bookings=mongo.db.bookings.find())


# add booking
@app.route('/add_booking')
def add_booking():
    return render_template('bookings/addbooking.html', types=mongo.db.types.find(),
                           brands=mongo.db.brands.find(),
                           models=mongo.db.models.find(),
                           bookings=mongo.db.bookings.find())


# Book a Cab
@app.route('/insert_booking', methods=['POST'])
def insert_booking():
    bookings = mongo.db.bookings
    # get the form and convert to a dictionary
    bookings.insert_one(request.form.to_dict())
    return redirect(url_for('get_bookings'))


# <---- Manage vehicle Types, Brands & Models ---->

# Gets the vehicle Types
@app.route('/get_types')
def get_types():
    return render_template('types/types.html',
                           types=mongo.db.types.find())


# edits a vehicle Type
@app.route('/edit_type/<type_id>')
def edit_type(type_id):
    return render_template('types/edittype.html',
                           type=mongo.db.types.find_one(
                            {'_id': ObjectId(type_id)}))


# updates vehicle Type
@app.route('/update_type/<type_id>', methods=['POST'])
def update_type(type_id):
    mongo.db.types.update(
        {'_id': ObjectId(type_id)},
        {'vehicle_type': request.form.get('vehicle_type')})
    return redirect(url_for('get_types'))
# ------ End of Vehicle Type----------

# ------ Vehicle Brand----------


# Gets the Brand Name
@app.route('/get_brand')
def get_brand():
    return render_template('brands/brands.html',
                           brands=mongo.db.brands.find())


# edits a Brand Name
@app.route('/edit_brand/<brand_id>')
def edit_brand(brand_id):
    return render_template('brands/editbrand.html',
                           brand=mongo.db.brands.find_one(
                            {'_id': ObjectId(brand_id)}))


# updates Brand
@app.route('/update_brand/<brand_id>', methods=['POST'])
def update_brand(brand_id):
    mongo.db.brands.update(
        {'_id': ObjectId(brand_id)},
        {'brand_name': request.form.get('brand_name')})
    return redirect(url_for('get_brand'))

# ------ End of Vehicle Brand----------


# ------ Vehicle Model----------

# Get the Model
@app.route('/get_model')
def get_model():
    return render_template('models/models.html',
                           models=mongo.db.models.find())


# edit the Model
@app.route('/edit_model/<model_id>')
def edit_model(model_id):
    return render_template('models/editmodel.html',
                           model=mongo.db.models.find_one(
                            {'_id': ObjectId(model_id)}))


# updates Model
@app.route('/update_model/<model_id>', methods=['POST'])
def update_model(model_id):
    mongo.db.models.update(
        {'_id': ObjectId(model_id)},
        {'model_name': request.form.get('model_name')})
    return redirect(url_for('get_model'))

# ------ End of Vehicle Brand----------


# ------ Delete functions--------

#  delete Types
@app.route('/delete_type/<type_id>')
def delete_type(type_id):
    mongo.db.types.remove({'_id': ObjectId(type_id)})
    return redirect(url_for('get_types'))


#  delete Brands
@app.route('/delete_brand/<brand_id>')
def delete_brand(brand_id):
    mongo.db.brands.remove({'_id': ObjectId(brand_id)})
    return redirect(url_for('get_brand'))


#  delete Models
@app.route('/delete_model/<model_id>')
def delete_model(model_id):
    mongo.db.models.remove({'_id': ObjectId(model_id)})
    return redirect(url_for('get_model'))

# ------ End Delete---------


# <----- Add functions --------->
# add Types
@app.route('/insert_type', methods=['POST'])
def insert_type():
    types = mongo.db.types
    types_doc = {'vehicle_type': request.form.get('vehicle_type')}
    types.insert_one(types_doc)
    return redirect(url_for('get_types'))


# render a view and add a new type
@app.route('/new_type')
def new_type():
    return render_template('types/addtype.html')


# add Brands
@app.route('/insert_brand', methods=['POST'])
def insert_brand():
    brands = mongo.db.brands
    brands_doc = {'brand_name': request.form.get('brand_name')}
    brands.insert_one(brands_doc)
    return redirect(url_for('get_brand'))


# render a view and add a new brand
@app.route('/new_brand')
def new_brand():
    return render_template('brands/addbrand.html')


# add Model
@app.route('/insert_model', methods=['POST'])
def insert_model():
    models = mongo.db.models
    models_doc = {'model_name': request.form.get('model_name')}
    models.insert_one(models_doc)
    return redirect(url_for('get_model'))


# render a view and add a new brand
@app.route('/new_model')
def new_model():
    return render_template('models/addmodel.html')


# Admin page
@app.route('/admin_page')
def admin_page():
    return render_template('admin.html')


# Admin page
@app.route('/admin_tasks')
def admin_tasks():
    return render_template('indexadmin.html')


# -- Search Routes ----
# Search form
"""
@app.route('/search_cab/', defaults={'vehicle_type': None})
@app.route('/search_cab/<vehicle_type>')
def search_cab(vehicle_type):
    cabs = mongo.db.cabs
    if vehicle_type is None:
        vehicle_type = request.form.get('vehicleType')
    cab = cabs.find_one({
        'vehicleType': vehicle_type
    })
    return render_template('searchresults.html', cab=cab)
# -------------------------------------------------------------->
"""


# -- Search Routes ----

# Search Cab
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    cabs = list(mongo.db.cabs.find({"$text": {"$search": query}}))
    return render_template("searchresults.html", cabs=cabs)


# Search Cab Bookings
@app.route("/search_booking", methods=["GET", "POST"])
def search_booking():
    query = request.form.get("query")
    bookings = list(mongo.db.bookings.find({"$text": {"$search": query}}))
    return render_template("bookings.html", bookings=bookings)


# ------ Login section for new drivers to add a Cab -----------

# register a user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
                {'username': request.form.get('username').lower()})

        if existing_user:
            flash('username already in DB')
            return redirect(url_for('register'))

        register = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for("profile", username=session["user"]))

    return render_template("admin/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                            request.form.get("username")))
                return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("admin/login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("admin/profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# ----- end login section ---------------/

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)
