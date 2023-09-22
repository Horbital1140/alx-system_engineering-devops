#file created in /tmp


file { 'school' :
path => '/tmp/school',
mode => '0744',
owner => 'www-data',
group => 'www-data',
ensure => 'present',
content => 'I love Puppet'
}
