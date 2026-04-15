import subprocess, argparse, collections, sys
from datetime import datetime, timedelta

def run_git(cmd):
    try: return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8').splitlines()
    except (subprocess.CalledProcessError, FileNotFoundError): return None

def generate_pulse(days=1):
    since = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
    raw = run_git(['git', 'log', f'--since={since}', '--pretty=format:%h|%an|%s', '--no-merges'])
    
    if raw is None: return "Error: Git environment failure."
    if not raw: return "No activity found."

    authors = collections.defaultdict(list)
    for s, a, m in (line.split('|', 2) for line in raw):
        authors[a].append(f"  - [{s}] {m}")

    report = [f"--- Git Pulse: {len(raw)} Commits ---"]
    for user, lines in authors.items():
        report.extend([f"\nUser: {user}", *lines])
    return "\n".join(report)

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Git activity summary')
    p.add_argument('--days', type=int, default=1)
    print(generate_pulse(p.parse_args().days))