
from lib import bird_control
from inotify_simple import INotify, flags
from prometheus_client import start_http_server, Enum
import hashlib

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def main():
    print('Starting prometheus exporter')
    start_http_server(8000)
    bird_config_folder = '/opt/bird'
    birdc_ip4_config = f'{bird_config_folder}/bird.conf'
    birdc_ip6_config = f'{bird_config_folder}/bird6.conf'

    birdc_ip4_socket_path = '/var/run/bird/bird.ctl'
    birdc_ip6_socket_path = '/var/run/bird/bird6.ctl'

    bird4_prometheus = Enum('bird4_config_state', 'Bird IPv4 Config State', states=['valid', 'invalid'])
    bird6_prometheus = Enum('bird6_config_state', 'Bird IPv6 Config State', states=['valid', 'invalid'])

    birdc_ip4 = bird_control.BirdControl(birdc_ip4_socket_path)
    birdc_ip6 = bird_control.BirdControl(birdc_ip6_socket_path)

    bird_ip4_config_hash = sha256sum(birdc_ip4_config)
    bird_ip6_config_hash = sha256sum(birdc_ip6_config)

    inotify = INotify()
    watch_flags = flags.CREATE | flags.MODIFY
    inotify.add_watch(bird_config_folder, watch_flags)
    print(f'watching config directory {bird_config_folder}')
    while True:
        for event in inotify.read():
            print('got inotify event, checking what has changed')
            new_bird_ip4_config_hash = sha256sum(birdc_ip4_config)
            new_bird_ip6_config_hash = sha256sum(birdc_ip6_config)

            if new_bird_ip4_config_hash != bird_ip4_config_hash:
                print('IPv4 config change')
                bird_ip4_config_hash = new_bird_ip4_config_hash
                valid_config = birdc_ip4.reconfigure_check(birdc_ip4_config)
                if valid_config :
                    birdc_ip4.reconfigure(birdc_ip4_config)
                    bird4_prometheus.state('valid')
                    print('valid IPv4 Config')
                else :
                    bird4_prometheus.state('invalid')
                    print('BAD IPv4 Config')
            if new_bird_ip6_config_hash != bird_ip6_config_hash:
                print('IPv6 config change')
                bird_ip6_config_hash = new_bird_ip6_config_hash
                valid_config = birdc_ip6.reconfigure_check(birdc_ip6_config)
                if valid_config :
                    birdc_ip6.reconfigure(birdc_ip6_config)
                    bird6_prometheus.state('valid')
                    print('valid IPv6 Config')
                else :
                    bird6_prometheus.state('invalid')
                    print('BAD IPv6 Config')

main()