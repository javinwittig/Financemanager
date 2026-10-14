# Finance Manager

A command-line finance manager written in Python for managing your personal finances.

## Features

- **Account creation:** On first use you can create a username and password. They are stored locally in a JSON file (`daten.json`) that is created automatically.
- **Add custom transactions:** Add income or expenses with a date, amount, category and custom description.
- **Transaction date range:** View all transactions within a custom date range, together with a summary of total income, total expenses and savings.
- **Automatic saving:** All transactions are saved to `finance_data.csv`, which is also created automatically.

## Requirements


None. No Python installation needed, everything is bundled in the download.

## How to install

1. Go to the [latest release](https://github.com/javinwittig/Financemanager/releases/tag/v1.0.1).
2. Download the file for your operating system.
3. Put it in its own folder, because the program creates `daten.json` and `finance_data.csv` next to it.
4. Run it:


Just download it and run it

## How to install

https://github.com/javinwittig/Financemanager/releases/tag/v1.0.1


| OS | File | How to run |
|---|---|---|
| Windows | `financemanager-windows.exe` | Double-click. If SmartScreen warns you, click "More info" → "Run anyway". |
| macOS | `financemanager-macos.tar.gz` | Extract, then open Terminal in that folder and run `./financemanager`. On the first start macOS may block the unsigned app: right-click → Open. |
| Linux | `financemanager-linux.tar.gz` | Extract, then run `./financemanager` in a terminal. |

The first start can take a few seconds, please wait

## Usage

1. Answer `No` on the first start and create your account (or `Yes` if you already have one) and log in.
2. Choose from the menu:
   1. Add a new transaction
   2. View transactions within a date range and summary
   3. Exit

## Note

The password is stored in plain text in `daten.json`. This is a learning project, so please do not use a password you use elsewhere.

