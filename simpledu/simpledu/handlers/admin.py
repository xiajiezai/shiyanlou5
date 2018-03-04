from flask import Blueprint
admin = Blueprint('admin',__name__,url_prefix='/admin')

#because you defined prefix in line 2, here you don't have to use '/admin'
@admin.route('/')
def admin_index():
    return 'admin'
