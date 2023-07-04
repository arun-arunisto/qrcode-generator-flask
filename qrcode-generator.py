import pyqrcode

url = "https://www.nic.in/diw2023-reg/"

create = pyqrcode.create(url)
create.png("register.png", scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
create.show()