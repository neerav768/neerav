import pandas as pd

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"


def money(value: float) -> str:
    return f"₹{value:,.2f} Lakhs"


def banner(text: str) -> str:
    return f"{BOLD}{CYAN}{text}{RESET}"


# Define Schedule III compliant Balance Sheet structure
balance_sheet = {
    "Head": [
        "Shareholders' Funds", "Shareholders' Funds",
        "Non-Current Liabilities", "Non-Current Liabilities",
        "Current Liabilities", "Current Liabilities", "Current Liabilities",
        "Non-Current Assets", "Non-Current Assets", "Non-Current Assets",
        "Current Assets", "Current Assets", "Current Assets", "Current Assets"
    ],
    "Particulars": [
        "1. Share Capital", "2. Reserves and Surplus",
        "3. Long-term Borrowings", "4. Deferred Tax Liabilities (Net)",
        "5. Short-term Borrowings", "6. Trade Payables", "7. Other Current Liabilities",
        "1. Property, Plant and Equipment", "2. Non-current Investments", "3. Long-term Loans & Advances",
        "4. Current Investments", "5. Inventories", "6. Trade Receivables", "7. Cash & Cash Equivalents"
    ],
    "Amount (in ₹ Lakhs)": [
        500.00, 1200.00,
        450.00, 50.00,
        150.00, 280.00, 70.00,
        1800.00, 300.00, 100.00,
        150.00, 200.00, 120.00, 30.00
    ]
}

df = pd.DataFrame(balance_sheet)

liabilities = df.iloc[0:7].copy()
assets = df.iloc[7:14].copy()

total_liabilities = liabilities["Amount (in ₹ Lakhs)"].sum()
total_assets = assets["Amount (in ₹ Lakhs)"].sum()
variance = total_assets - total_liabilities

print("=" * 92)
print(banner("    BALANCE SHEET DASHBOARD"))
print("=" * 92)
print(df.to_string(
    index=False,
    formatters={"Amount (in ₹ Lakhs)": lambda x: f"₹{x:,.2f}"},
    justify="center",
    col_space=24,
))
print("-" * 92)
print(f"{BOLD}{'Total Equity & Liabilities':<28}{RESET}: {GREEN}{money(total_liabilities)}{RESET}")
print(f"{BOLD}{'Total Assets':<28}{RESET}: {GREEN}{money(total_assets)}{RESET}")
print(f"{BOLD}{'Balance Check':<28}{RESET}: {GREEN if abs(variance) < 0.01 else YELLOW}{money(variance)}{RESET}")

if abs(variance) < 0.01:
    print(f"{BOLD}{'Status':<28}{RESET}: {GREEN}✅ Balanced{RESET}")
else:
    print(f"{BOLD}{'Status':<28}{RESET}: {RED}⚠️ Needs attention{RESET}")

print("=" * 92)
print(f"{BOLD}{CYAN}Summary:{RESET} This company shows a strong asset base with equity and liabilities aligned within {money(abs(variance))}.")
print("=" * 92)

indian_companies = [
    {"Ticker": "RELIANCE.NS", "Company": "Reliance Industries", "Sector": "Energy"},
    {"Ticker": "TCS.NS", "Company": "Tata Consultancy Services", "Sector": "IT Services"},
    {"Ticker": "INFY.NS", "Company": "Infosys", "Sector": "IT Services"},
    {"Ticker": "HDFCBANK.NS", "Company": "HDFC Bank", "Sector": "Banking"},
    {"Ticker": "ICICIBANK.NS", "Company": "ICICI Bank", "Sector": "Banking"},
    {"Ticker": "SBIN.NS", "Company": "State Bank of India", "Sector": "Banking"},
    {"Ticker": "ITC.NS", "Company": "ITC Ltd", "Sector": "FMCG"},
    {"Ticker": "TATAMOTORS.NS", "Company": "Tata Motors", "Sector": "Automotive"},
    {"Ticker": "SUNPHARMA.NS", "Company": "Sun Pharmaceutical", "Sector": "Pharma"},
    {"Ticker": "LT.NS", "Company": "Larsen & Toubro", "Sector": "Infrastructure"},
    {"Ticker": "BHARTIARTL.NS", "Company": "Bharti Airtel", "Sector": "Telecom"},
    {"Ticker": "AXISBANK.NS", "Company": "Axis Bank", "Sector": "Banking"},
    {"Ticker": "KOTAKBANK.NS", "Company": "Kotak Mahindra Bank", "Sector": "Banking"},
    {"Ticker": "NTPC.NS", "Company": "NTPC", "Sector": "Power"},
    {"Ticker": "ASIANPAINT.NS", "Company": "Asian Paints", "Sector": "Consumer Durables"},
]

popular_stocks = pd.DataFrame(indian_companies)
print("\n" + "=" * 92)
print(banner("    INDIAN STOCKS / COMPANY WATCHLIST"))
print("=" * 92)
print(popular_stocks.to_string(index=False, justify="center", col_space=22))
print("=" * 92)