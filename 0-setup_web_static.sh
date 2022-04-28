#!/usr/bin/env bash
# Sets up the web server and the necesary folders
sudo apt update
sudo apt install -y nginx

# Nginx redirection, header and 404 page
sudo sed -i '/^\tserver_name.*/a \\n\terror_page 404 \/custom-404.html;\n\tadd_header X-Served-By $HOSTNAME;\n\trewrite ^\/redirect_me/$ https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n' /etc/nginx/sites-available/default

# sudo sed -i '/^\tlocation \/ {.*}\n/a \\n\tlocation \/hbnb_static {\n\talias \/data\/web_static\/current\/\n}\n' /etc/nginx/sites-available/default

# Changing html response
echo "Hello World" | sudo tee /var/www/html/index.nginx-debian.html
printf "Ceci n'est pas une page" | sudo tee /var/www/html/custom-404.html

# Creating static folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Testing Nginx" | sudo tee /data/web_static/releases/test/index.html
# Creating symbolic link
sudo ln -f -s /data/web_static/releases/test/ /data/web_static/current
# Setting up privileges for folders
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo service nginx restart
