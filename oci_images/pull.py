#!/usr/bin/env python3
import requests
import argparse
import sys
import platform

def get_docker_token(repo):
    auth_url = f"https://auth.docker.io/token?service=registry.docker.io&scope=repository:{repo}:pull"
    response = requests.get(auth_url)
    return response.json().get('token') if response.status_code == 200 else None

def get_manifest(repo, tag, token):
    url = f"https://registry-1.docker.io/v2/{repo}/manifests/{tag}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.docker.distribution.manifest.v2+json, application/vnd.docker.distribution.manifest.list.v2+json"
    }
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def main():
    parser = argparse.ArgumentParser(prog="foo")
    subparsers = parser.add_subparsers(dest="command")
    pull_parser = subparsers.add_parser("pull")
    pull_parser.add_argument("image")
    pull_parser.add_argument("--tag", default="latest")
    
    args = parser.parse_args()
    if not args.command == "pull":
        parser.print_help()
        return

    repo = f"library/{args.image}" if "/" not in args.image else args.image
    token = get_docker_token(repo)
    manifest_data = get_manifest(repo, args.tag, token)

    if not manifest_data:
        print("[!] Image not found.")
        sys.exit(1)

    if "manifests" in manifest_data:
        print("[*] Multi-arch image detected. Finding linux/amd64...")
        target_digest = None
        for m in manifest_data['manifests']:
            if m['platform']['architecture'] == 'amd64' and m['platform']['os'] == 'linux':
                target_digest = m['digest']
                break
        
        if not target_digest:
            print("[!] Could not find a compatible linux/amd64 manifest.")
            sys.exit(1)
            
        manifest_data = get_manifest(repo, target_digest, token)

    config_digest = manifest_data['config']['digest']
    print(f"[+] Successfully retrieved manifest for {repo}")
    print(f"    Config Digest: {config_digest}")
    print(f"    Layers to pull: {len(manifest_data['layers'])}")

if __name__ == "__main__":
    main()
