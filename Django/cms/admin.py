from django.contrib import admin
from cms.models import Book, Impression

# admin.site.register(Book)
# admin.site.register(Impression)

class BookAdmin(admin.ModelAdmin):
    ## 一覧に表示したい項目を定義する
    list_display = ('id', 'name', 'publisher', 'page')
    ## 修正リンクでクリックできる項目を定義する
    list_display_links=('id', 'name')


admin.site.register(Book, BookAdmin)
admin.site.register(Impression)