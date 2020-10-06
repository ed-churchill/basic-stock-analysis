import quandl
from last_trading_date import last_trading_date
import time

t0 = time.time()
# List of companies on the Frankfurt Stock Exchange
companies = ("1COV_X",
             "2HR_X",
             "AAD_X",
             "AB1_X",
             "ADS_X",
             "ADV_X",
             "AFX_X",
             "AIR_X",
             "AIXA_X",
             "ALV_X",
             "ANN_X",
             "AOX_X",
             "ARL_X",
             "B5A_X",
             "BAF_X",
             "BAS_X",
             "BAYN_X",
             "BBZA_X",
             "BC8_X",
             "BDT_X",
             "BEI_X",
             "BIO3_X",
             "BMW_X",
             "BNR_X",
             "BOSS_X",
             "BYW6_X",
             "CBK_X",
             "CEV_X",
             "CLS1_X",
             "COK_X",
             "COM_X",
             "CON_X",
             "COP_X",
             "CWC_X",
             "DAI_X",
             "DB1_X",
             "DBAN_X",
             "DBK_X",
             "DEQ_X",
             "DEX_X",
             "DEZ_X",
             "DIC_X",
             "DLG_X",
             "DPW_X",
             "DRI_X",
             "DRW3_X",
             "DTE_X",
             "DUE_X",
             "DWNI_X",
             "EOAN_X",
             "EON_X",
             "EVD_X",
             "EVK_X",
             "EVT_X",
             "FIE_X",
             "FME_X",
             "FNTN_X",
             "FPE3_X",
             "FRA_X",
             "FRE_X",
             "G1A_X",
             "GBF_X",
             "GFJ_X",
             "GFK_X",
             "GIL_X",
             "GLJ_X",
             "GMM_X",
             "GSC1_X",
             "GWI1_X",
             "GXI_X",
             "HAB_X",
             "HAW_X",
             "HBH3_X",
             "HDD_X",
             "HEI_X",
             "HEN3_X",
             "HHFA_X",
             "HNR1_X",
             "HOT_X",
             "IFX_X",
             "INH_X",
             "JEN_X",
             "JUN3_X",
             "KBC_X",
             "KCO_X",
             "KD8_X",
             "KGX_X",
             "KRN_X",
             "KU2_X",
             "KWS_X",
             "LEG_X",
             "LEO_X",
             "LHA_X",
             "LIN_X",
             "LPK_X",
             "LXS_X",
             "MAN_X",
             "MEO_X",
             "MLP_X",
             "MOR_X",
             "MRK_X",
             "MTX_X",
             "MUV2_X",
             "NDA_X",
             "NDX1_X",
             "NEM_X",
             "NOEJ_X",
             "O1BC_X",
             "O2C_X",
             "O2D_X",
             "OSR_X",
             "P1Z_X",
             "PFV_X",
             "PMOX_X",
             "PSAN_X",
             "PSM_X",
             "PUM_X",
             "QIA_X",
             "QSC_X",
             "RAA_X",
             "RHK_X",
             "RHM_X",
             "RRTL_X",
             "RWE_X",
             "S92_X",
             "SAP_X",
             "SAX_X",
             "SAZ_X",
             "SBS_X",
             "SDF_X",
             "SFQ_X",
             "SGL_X",
             "SIE_X",
             "SIX2_X",
             "SKB_X",
             "SKYD_X",
             "SLT_X",
             "SOW_X",
             "SPR_X",
             "SRT3_X",
             "SW1_X",
             "SY1_X",
             "SZG_X",
             "SZU_X",
             "TEG_X",
             "TIM_X",
             "TKA_X",
             "TLX_X",
             "TTI_X",
             "TTK_X",
             "TUI1_X",
             "UTDI_X",
             "VIB3_X",
             "VNA_X",
             "VOS_X",
             "VOW3_X",
             "VT9_X",
             "WAC_X",
             "WCH_X",
             "WDI_X",
             "WIN_X",
             "ZIL2_X",
             "ZO1_X"
             )

# API Key for quandl. To run this program, save your API key in a file named 'my_api_key.txt' and place the file in the
# same directory as this one.
with open('my_api_key.txt') as file_object:
    my_api_key = file_object.read().strip()

# String storing the date of the last business day in the form YYYY-MM-DD
last_business_date = last_trading_date()

# Dictionaries that will contain open and close prices for each company
open_prices = {}
close_prices = {}

# Dictionary that will contain the percentage change between open and close price for each company
percentage_changes = {}

# For loop to get relevant data for each company and store it in the relevant dictionary
for company in companies:

    # Dataframe containing the opening price and closing price for the company
    open_close_data = quandl.get(["FSE/" + company + ".1", "FSE/" + company + ".4"],
                                 authtoken=my_api_key,
                                 start_date=last_business_date)

    # Ignores any empty dataframes
    if open_close_data.empty:
        continue

    # Adds the company name as a key and the open/close price as the value to the relevant dictionary
    open_prices[company] = open_close_data.iloc[0, 0]
    close_prices[company] = (open_close_data.iloc[0, 1])

# Calculate the percentage change between open and close price for each company
for key in open_prices:
    percentage_change = (close_prices[key] - open_prices[key]) / open_prices[key]
    percentage_changes[key] = percentage_change

# Variables storing the name and perecentage increase of the company with the largest percentage increase
largest_increase_company = max(percentage_changes, key=percentage_changes.get)
largest_increase = percentage_changes[largest_increase_company]

# Variables storing the name and perecentage increase of the company with the smallest percentage increase
smallest_increase_company = min(percentage_changes, key=percentage_changes.get)
smallest_increase = percentage_changes[smallest_increase_company]

# Print the best and worst performing companies for the last business day, with the relavant perecentage changes.
print("The best performing company on " + last_business_date + "was "
      + largest_increase_company + " with a " + str(round(largest_increase, 3)) + "% change in their share price.")
print("The worst performing company on " + last_business_date + "was "
      + smallest_increase_company + " with a " + str(round(smallest_increase, 3)) + "% change in their share price.")

t1 = time.time()
print(str(t1 - t0))
