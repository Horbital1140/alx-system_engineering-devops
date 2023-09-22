# process kill me now

exec { 'pkill':
command => 'pkill killmenow',
provider => 'shell',
}

