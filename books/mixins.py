from books.models import Category


class DisplayCategoryMixin:
    cats = None

    def get_cats(self):
        return Category.objects.all()

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['cats'] = self.get_cats()
        print("adding cats to the context")
        return context