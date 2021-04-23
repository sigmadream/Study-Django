# CRM-Web

## Tip!, Jupyter를 사용해서 Query를 확인하는 방법

```
import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

import django
django.setup()
```

## tailwindcss

CDN 사용

```
<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
```

tailwindcss기반 CSS 예제

* [Tailblocks](https://github.com/mertJF/tailblocks)

## FBV to CBV

```python
# def landing_page(request):
#     return render(request, "landing.html")

class LandingPageView(TemplateView):
    template_name = "landing.html"


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {"leads": leads}
#     return render(request, "leads/lead_list.html", context)

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {"lead": lead}
#     return render(request, "leads/lead_detail.html", context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.get(id=pk)
    context_object_name = "lead"


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {"form": form}
#     return render(request, "leads/lead_create.html", context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {"form": form, "lead": lead}
#     return render(request, "leads/lead_update.html", context)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


# 
# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
```
