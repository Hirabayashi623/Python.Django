from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cms.models import Book
from cms.forms import BookForm

def book_list(request):
    # 引数の中身をクライアントに見せる
    # return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id');
    return render(request
                  ,'cms/book_list.html'     # 使用するテンプレートを指定する（「※アプリ/templates/」以下のパスを記載）
                  ,{'books': books}         # テンプレートに渡すデータを指定
                  )
#     return render(request, 'cms/sample.html')


def book_edit(request, book_id=None):
#     return HttpResponse('書籍の編集')
    if book_id:
        # DBからpkを条件にレコードを取得する
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) # POSTされたrequestデータからフォームを作成
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:           ## GETのとき
        form = BookForm(instance=book)  # Bookインスタンスからフォームを作成

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))

def book_del(request, book_id):
    return HttpResponse('書籍の削除')