# bird-configwatcher

`bird-configwatcher` applies changed configs to the BIRD internet relay daemon without restarting the BIRD process.
The bird config files at `/opt/bird/bird.conf` and `/opt/bird/bird6.conf` will be observed for changes.
When changes are detected, the new config will be validated and subsequently applied when the validation was successful.

The following prometheus metrics are exposed on port `8000`:

- bird4_config_state
- bird6_config_state

with the possible values of `valid` or `invalid`.
