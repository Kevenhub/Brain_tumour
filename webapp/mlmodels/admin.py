from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path
import subprocess, sys, os
from .models import MLModelTask

admin.site.site_header = "Brain Tumor Detection Admin Portal"
admin.site.site_title = "Brain Tumor Detection Admin Portal"
admin.site.index_title = "Welcome to the Brain Tumor Detection Admin"


def run_script(script_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  
    # ^ goes from webapp/mlmodels/admin.py → webapp/mlmodels → webapp → Brain_tumour_Final
    backend_dir = os.path.join(base_dir, "backend")  
    script_path = os.path.join(backend_dir, script_name)

    if not os.path.exists(script_path):
        return f"❌ Script not found: {script_path}"

    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    return result.stdout + result.stderr


class MLModelAdmin(admin.ModelAdmin):
    change_list_template = "admin/mlmodels_dashboard.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("load-data/", self.admin_site.admin_view(self.load_data)),
            path("build-model/", self.admin_site.admin_view(self.build_model)),
            path("train-model/", self.admin_site.admin_view(self.train_model)),
        ]
        return custom_urls + urls

    def load_data(self, request):
        messages.info(request, "⏳ Loading data… please wait.")
        output = run_script("aload_data.py")
        messages.success(request, f"✅ Load Data completed:\n{output[:200]}...")
        return HttpResponseRedirect("../")

    def build_model(self, request):
        messages.info(request, "⏳ Building model… please wait.")
        output = run_script("build_model.py")
        messages.success(request, f"✅ Build Model completed:\n{output[:200]}...")
        return HttpResponseRedirect("../")

    def train_model(self, request):
        messages.info(request, "⏳ Training model… this may take some time.")
        output = run_script("ctrain_model.py")
        messages.success(request, f"✅ Training completed:\n{output[:200]}...")
        return HttpResponseRedirect("../")


admin.site.register(MLModelTask, MLModelAdmin)
