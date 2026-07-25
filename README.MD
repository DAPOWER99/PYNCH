# Pynch 📖

> A high-performance dictionary GUI tool built for instant local lookups and clean desktop integration.

---

## Overview

**Pynch** is a lightweight desktop application designed for fast word definitions and linguistic exploration. It uses a clean separation between the database preparation phase and the graphical runtime interface.

---

## Architecture & Scripts

* **`index.py` (Indexer)**: Run this script to parse and index the raw dictionary data into a high-speed format. You only need to run this if an indexed dictionary database is missing or needs to be rebuilt (run this first if you dont have a preindexed version).
* **`main.py` (Runtime GUI)**: The core application script that launches the graphical user interface for everyday lookups.

---

## Tech Stack & Environment

* **Language**: Python
* **Runtime**: Ghost Python (Portable v3.14) compatible
* **Interface**: Custom GUI Framework

---

## Quick Start

Clone the repository and jump into the directory:

```bash
git clone [https://github.com/DAPOWER99/Pynch.git](https://github.com/DAPOWER99/Pynch.git)
cd Pynch
