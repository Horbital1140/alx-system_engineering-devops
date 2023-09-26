# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
  ",
  notify => Service['nginx'],
  require => Package['nginx'],
}

# Create the HTML files
file { '/var/www/html/index.html':
  content => "Hello World!\n",
  require => Package['nginx'],
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

# Ensure Nginx listens on port 80
file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  require => Package['nginx'],
  notify => Service['nginx'],
}

# Remove the default Nginx default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'absent',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

