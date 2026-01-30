#!/usr/bin/env python3
import sys
import argparse
from engine.volume import VolumeManager

def main():
    parser = argparse.ArgumentParser(
        prog="ghostd",
        description="GhostD : A Custom Container Runtime"
    )

    # Top-level commands (e.g., ghostd volume, ghostd pull)
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- VOLUME GROUP ---
    vol_parser = subparsers.add_parser("volume", help="Manage ghostd volumes")
    vol_subparsers = vol_parser.add_subparsers(dest="subcommand", help="Volume commands")
    
    # ghostd volume create <name>
    create_parser = vol_subparsers.add_parser("create", help="Create a new persistent volume")
    create_parser.add_argument("name", help="The unique name for the volume")

    # ghostd volume list
    vol_subparsers.add_parser("list", help="List all existing volumes")

    # ghostd volume inspect <name>
    inspect_parser = vol_subparsers.add_parser("inspect", help="Inspect a volume")
    inspect_parser.add_argument("name", help="The name of the ghostd volume to inspect")

    args = parser.parse_args()
    
    vm = VolumeManager()

    if args.command == "volume":
        if args.subcommand == "create":
            vm.create_volume(args.name)
        elif args.subcommand == "list":
            vm.list_volumes()
        elif args.subcommand == "inspect":
            vm.inspect_volume(args.name)
        else:
            vol_parser.print_help()

    elif args.command is None:
        parser.print_help()

if __name__ == "__main__":
    main()