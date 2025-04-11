import sqlite3


def print_all_entries(db_path="school_info.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Check if the 'info' table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='info';")
    if not c.fetchone():
        print("No data found — 'info' table doesn't exist.")
        conn.close()
        return

    c.execute("SELECT id, topic, url, substr(content, 1, 150) || '...' FROM info")
    rows = c.fetchall()

    if not rows:
        print("No entries found in the database.")
    else:
        for row in rows:
            print(f"[{row[0]}] {row[1]} | URL: {row[2]}\n{row[3]}\n{'-' * 60}")

    conn.close()


# Run the viewer
if __name__ == "__main__":
    print_all_entries()
