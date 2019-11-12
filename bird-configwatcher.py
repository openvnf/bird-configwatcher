
from lib import bird_control
from inotify_simple import INotify, flags
from prometheus_client import start_http_server, Enum


def main():
    start_http_server(8000)
    bird_config_folder = '/opt/bird'
    birdc_ip4_config = f'{bird_config_folder}/bird.conf'
    birdc_ip6_config = f'{bird_config_folder}/bird6.conf'

    birdc_ip4_socket_path = '/var/bla';
    birdc_ip6_socket_path = '/var/bla';

    bird4_prometheus = Enum('bird4_config_state', 'Bird IPv4 Config State', states=['valid', 'invalid'])
    bird6_prometheus = Enum('bird6_config_state', 'Bird IPv6 Config State', states=['valid', 'invalid'])

    birdc_ip4 = bird_control.BirdControl(birdc_ip4_socket_path);
    birdc_ip6 = bird_control.BirdControl(birdc_ip6_socket_path);
    inotify = INotify()
    watch_flags = flags.CREATE | flags.MODIFY
    wd = inotify.add_watch(bird_config_folder, watch_flags)

    for event in inotify.read():
        full_path_event = f'{bird_config_folder}/{event.name}'
        if full_path_event == birdc_ip4_config:
            valid_config = birdc_ip4.reconfigure_check(birdc_ip4_config)
            if valid_config :
                birdc_ip4.reconfigure(birdc_ip4_config)
                bird4_prometheus.state('valid')
            else :
                bird4_prometheus.state('invalid')
                print('BAD IPv4 Config')
        elif full_path_event == birdc_ip6_config:
            valid_config = birdc_ip6.reconfigure_check(birdc_ip6_config)
            if valid_config :
                birdc_ip6.reconfigure(birdc_ip6_config)
                bird6_prometheus.state('valid')
            else :
                bird6_prometheus.state('invalid')
                print('BAD IPv6 Config')
        else:
            print('unknown file added, or changed')

main()