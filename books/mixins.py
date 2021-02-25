#from books.models import Category
#
#
# class DisplayCategoryMixin:
#     cats = None
#
#     def get_cats(self):
#         return Category.objects.all()
#
#     def get_context_data(self,*args,**kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['cats'] = self.get_cats()
#         print("adding cats to the context")
#         return context

class FormMessageMixin(object):
    @property
    def form_valid_message(self):
        return NotImplemented

    form_invalid_message = 'Please correct the errors below.'

    def form_valid(self, form):
        messages.success(self.request, self.form_valid_message)
        return super(FormMessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.form_invalid_message)
        return super(FormMessageMixin, self).form_invalid(form)


class DocumentCreateView(FormMessageMixin, CreateView):
    model = Document
    fields = ('name', 'file')
    success_url = reverse_lazy('documents')
    form_valid_message = 'The document was successfully created!'