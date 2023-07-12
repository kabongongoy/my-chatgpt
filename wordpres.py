import os

# Update the system
os.system('sudo yum update -y')

# Install Apache web server
os.system('sudo yum install httpd -y')
os.system('sudo systemctl start httpd')
os.system('sudo systemctl enable httpd')

# Install MySQL database server
os.system('sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2')
os.system('sudo yum install -y mariadb-server')
os.system('sudo systemctl start mariadb')
os.system('sudo systemctl enable mariadb')

# Secure MySQL installation
os.system('sudo mysql_secure_installation')

# Install PHP
os.system('sudo yum install -y php php-mysql')

# Start Apache web server
os.system('sudo systemctl restart httpd')

# Download and extract WordPress
os.system('sudo yum install -y wget')
os.system('sudo wget https://wordpress.org/latest.tar.gz')
os.system('sudo tar -xzf latest.tar.gz')

# Move WordPress files to web server root directory
os.system('sudo cp -R wordpress/* /var/www/html/')
os.system('sudo chown -R apache:apache /var/www/html/')
os.system('sudo chmod -R 755 /var/www/html/')

# Create WordPress database
os.system('sudo mysql -e "CREATE DATABASE wordpress;"')
os.system('sudo mysql -e "CREATE USER \'wordpressuser\'@\'localhost\' IDENTIFIED BY \'Password123\';"')
os.system('sudo mysql -e "GRANT ALL PRIVILEGES ON wordpress.* TO \'wordpressuser\'@\'localhost\';"')
os.system('sudo mysql -e "FLUSH PRIVILEGES;"')

# Clean up
os.system('sudo rm latest.tar.gz')
os.system('sudo rm -rf wordpress')

print('WordPress installation completed.')


# Save this script in a file called `wordpress_installer.py` and execute it using the following command:
# ```
# python wordpress_installer.py
# ```

# This script will update the system, install Apache, MySQL, and PHP, download and extract WordPress, move the WordPress files to the web server root directory, create a MySQL database for WordPress, and clean up the downloaded files.

# Make sure to replace `Password123` with a secure password for the WordPress database user.

# Note: This script assumes that you are using an Amazon Linux 2 EC2 instance. If you are using a different version of Linux, some commands may need to be modified.