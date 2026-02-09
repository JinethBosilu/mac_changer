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
# MAC Changer

A small, command-line Python tool to change a network interface's MAC address. This README is written for other users who may want to run the program.

## Overview

`mac_changer.py` is a simple script that uses the system `ifconfig` command to take an interface down, set its hardware (MAC) address, then bring it back up. The script exposes a command-line interface so you can specify the target interface and new MAC address when you run it.

## Requirements

- A Unix-like OS where `ifconfig` is available (Linux, BSD). Many modern Linux distributions prefer `ip`; install `net-tools` if you need `ifconfig`.
- Python 3 (the script uses only standard-library modules).
- Root/administrator privileges to modify network interface settings.

## Usage

From the `mac_changer` directory, run:

```bash
sudo python3 mac_changer.py -i <interface> -m <new-mac>
```

Short options:
- `-i`, `--interface` : interface to modify (example: `eth0`, `wlan0`)
- `-m`, `--mac`       : new MAC address to apply (example: `00:11:22:33:44:55`)

Examples:

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
sudo python3 mac_changer.py --interface wlan0 --mac 12:34:56:78:9a:bc
python3 mac_changer.py --help
```

The script will print an error and exit if either option is missing.

## How it works

- The script uses `optparse` (standard library) to parse the command-line options.
- It runs `ifconfig <interface> down`, `ifconfig <interface> hw ether <new_mac>`, and `ifconfig <interface> up` using `subprocess.run`.

## Safety, permissions & legal

- You must have explicit permission to change network settings on a machine or network — do not use this on networks you do not control.
- Running this may disrupt network connectivity; make sure you have a way to restore connectivity.
- Run the script with `sudo` or as root. Without elevated privileges the commands will fail.

## Limitations & suggestions

- The script depends on `ifconfig`. On systems using `ip` (iproute2), adapt the commands or install `net-tools`.
- There is no MAC address format validation. Consider adding a simple regex check before applying the change.
- `optparse` is used for simplicity and works, but `argparse` offers a modern alternative with better help and validation.
- The script does not verify the change succeeded. You can verify using `ifconfig <interface>` or `ip link show <interface>` after running.

## Example verification

```bash
ifconfig eth0 | grep -i ether
# or
ip link show eth0
```

## Contributing / Publishing

- Remove any hard-coded or personal values before publishing. This repository contains no secrets by default.
- Add a `LICENSE` file if you plan to publish publicly.
- Add a `.gitignore` if you intend to keep local config or logs out of the repo.
