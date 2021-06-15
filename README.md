# bird-configwatcher

`bird-configwatcher` applies changed configs to the BIRD internet relay daemon without restarting the BIRD process.
The bird config files at `/opt/bird/bird.conf` and `/opt/bird/bird6.conf` will be observed for changes.
When changes are detected, the new config will be validated and subsequently applied when the validation was successful.

Prometheus metrics about the Python runtime and the config validity are exposed on the port specified by the environment variable `METRICS_PORT` (default: `8000`):

Full example of all metrics:

```text
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 31.0
python_gc_objects_collected_total{generation="1"} 348.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 37.0
python_gc_collections_total{generation="1"} 3.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="9",patchlevel="2",version="3.9.2"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.75661056e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 1.9931136e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.62376327661e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.13
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 7.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP bird4_config_state Bird IPv4 Config State
# TYPE bird4_config_state gauge
bird4_config_state{bird4_config_state="valid"} 1.0
bird4_config_state{bird4_config_state="invalid"} 0.0
# HELP bird6_config_state Bird IPv6 Config State
# TYPE bird6_config_state gauge
bird6_config_state{bird6_config_state="valid"} 1.0
bird6_config_state{bird6_config_state="invalid"} 0.0
```
