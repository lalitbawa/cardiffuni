from flask import Blueprint, render_template, request,flash
from flask_login import current_user
from .models import Note
from . import db


views = Blueprint('views', __name__)

@views.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) <1:
            flash('Message cannot be blank', category='error')
        else:
            new_note = Note(data = note , user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Message sent successfully',category='success')
    return render_template('home.html', user = current_user)

@views.route('/resume')
def resume():
    return render_template('resume.html', user = current_user)