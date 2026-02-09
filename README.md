# MAC Changer

A minimal Python script to change a network interface's MAC address using system `ifconfig` commands.

## What this does

- Runs `ifconfig <interface> down`, sets the hardware (MAC) address, then brings the interface back up.
- Uses hard-coded `interface` and `new_mac` variables at the top of the script.

## Requirements

- Unix-like OS with `ifconfig` available (Linux/BSD). Note: many modern Linux distributions use `ip` instead of `ifconfig`.
- Python 3
- Root privileges (the script calls network commands that require administrative access).

## Files

- `mac_changer.py` — the script to change the MAC address.

## Usage

1. Open `mac_changer.py` and set the `interface` and `new_mac` variables to the desired values.

2. Run with root privileges:

```bash
sudo python3 mac_changer.py
```

Example (from repository root):

```bash
cd mac_changer
sudo python3 mac_changer.py
```

## Safety & Legal

- Only run this on systems and networks you own or where you have explicit permission.
- Changing MAC addresses can disrupt network access and violate network policies.
- The script uses `shell=True` with `subprocess.run`; review and modify if you need stricter command handling.

## Notes

- If your system uses `ip` instead of `ifconfig`, adapt the script commands or install the `net-tools` package.
- Consider enhancing the script to accept command-line arguments and validate MAC address format before applying.

## Before pushing to GitHub

- Remove or review any sensitive values. Hard-coded MAC addresses or interface names are not secrets but review for appropriateness.
- Optionally add a `.gitignore` if you plan to add local config files.

## License

Use as you wish; include a license file if you plan to publish publicly.
