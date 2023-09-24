#puppet class for maanging ssh config

include ssh_config
class ssh_config {
file { '/etc/ssh/ssh_config':
ensure 	=> present,
content => "Host *
                  identityFile ~/.ssh/school
	 	   PasswordAuthentication no"
replace => true
}
}
