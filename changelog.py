# changelog.py
import datetime
import sys

def update_changelog(version, entries):
    today = datetime.date.today().strftime("%B %d, %Y")
    header = f"\n## v{version} – {today}\n"
    lines = [f"- {entry}" for entry in entries]
    block = header + "\n" + "\n".join(lines) + "\n"

    with open("CHANGELOG.md", "r+") as f:
        content = f.read()
        f.seek(0)
        f.write(content.strip() + block)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python changelog.py <version> <entry1> [<entry2> ...]")
        sys.exit(1)
    
    ver = sys.argv[1]
    update_changelog(ver, sys.argv[2:])
    print(f"✅ CHANGELOG updated to v{ver}")
