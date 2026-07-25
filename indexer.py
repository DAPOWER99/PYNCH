import shelve
import sys

def build_index(input_path, db_name):
    print("Starting high-speed index... Please wait.")
    # 'writeback=False' is crucial for memory efficiency
    db = shelve.open(db_name, writeback=False)
    
    count = 0
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        while True:
            pos = f.tell()
            line = f.readline()
            if not line: break
            
            # FAST PARSING: Check for word key without loading full JSON
            # This is significantly faster than json.loads()
            if '"word":"' in line:
                try:
                    word = line.split('"word":"')[1].split('"')[0].lower()
                    if word not in db:
                        db[word] = pos
                except:
                    pass
            
            count += 1
            if count % 50000 == 0:
                sys.stdout.write(f"\rProcessed {count} lines...")
                sys.stdout.flush()

    db.close()
    print("\nIndexing finished successfully.")

if __name__ == "__main__":
import shelve
import sys

def build_index(input_path, db_name):
    print("Starting high-speed index... Please wait.")
    # 'writeback=False' is crucial for memory efficiency
    db = shelve.open(db_name, writeback=False)
    
    count = 0
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        while True:
            pos = f.tell()
            line = f.readline()
            if not line: break
            
            # FAST PARSING: Check for word key without loading full JSON
            # This is significantly faster than json.loads()
            if '"word":"' in line:
                try:
                    word = line.split('"word":"')[1].split('"')[0].lower()
                    if word not in db:
                        db[word] = pos
                except:
                    pass
            
            count += 1
            if count % 50000 == 0:
                sys.stdout.write(f"\rProcessed {count} lines...")
                sys.stdout.flush()

    db.close()
    print("\nIndexing finished successfully.")

if __name__ == "__main__":
    build_index('dictionary/kaikki.org-dictionary-English-words.jsonl', 'pynch_db')