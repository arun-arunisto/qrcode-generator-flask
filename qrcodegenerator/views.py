from flask import Blueprint, flash, render_template, send_from_directory, redirect, url_for
from .forms import LinkInput
import pyqrcode as qr
import os

def link_purifier(url):
    if url.startswith("https://") or url.startswith("http://"):
        if url.find("www.") != -1:
            start = url.find("www.")
            end = url[start:].find("/")
            if end == -1:
                return url[start:]
            return url[start:][:end]
        elif url.find("://") != -1:
            start = url.find("://") + 3
            end = url[start:].find("/")
            if end == -1:
                return url[start:]
            return url[start:][:end]

qr_bp = Blueprint("qrgenerate", __name__,
                  template_folder="templates",
                  static_folder="static",
                  static_url_path="/qrcodegenerator/static")

@qr_bp.route("/", methods=["GET", "POST"])
def home():
    form = LinkInput()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        try:
            link = form.link.data
            #print(link_purifier(link).replace(".", "-"))
            create = qr.create(link)
            filename = link_purifier(link).replace(".", "_")+".png"
            folder_path = os.path.join(qr_bp.static_folder, "images")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            filepath = os.path.join(folder_path, filename)
            create.png(filepath, scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
            return render_template("index.html", data=[{"link":link_purifier(link),
                                                        "filename":filename}])
        except Exception as e:
            print(e)
            return render_template("index.html", form=form)
    return render_template("index.html", form=form)

@qr_bp.route("/download/<filename>/", methods=["GET", "POST"])
def download(filename):
    try:
        folder_path = os.path.join(qr_bp.static_folder, "images")
        print(folder_path)
        return send_from_directory(folder_path, path=filename, as_attachment=True)
    except Exception as e:
        print(e)
        return redirect(url_for('qrgenerate.home'))
