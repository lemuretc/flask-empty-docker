from flask_appbuilder import IndexView


class MyIndexView(IndexView):
    index_template = 'kr-index.html'
