# Puppet script that sets up your web servers for the deployment of web_static.

exec { 'setup':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu:ubuntu /data && sudo sed -i \'53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}\' /etc/nginx/sites-available/default && sudo service nginx restart',
  provider => shell,
}