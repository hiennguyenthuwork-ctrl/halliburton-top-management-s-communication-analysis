# -*- coding: utf-8 -*-

import pandas as pd

# Load the Sample of Earnings Calls for the S&P500 from 2015 to 2021 with financials
Sample_EC = pd.read_csv("https://www.dropbox.com/scl/fi/2p7ahxroqj9pwf98ni5an/Sample_Calls.csv?rlkey=zfieicvz891u4e3z0aroeg0u7&dl=1")
GVKEYs= Sample_EC.groupby('GVKEY')['file_name'].count()[(Sample_EC.groupby('GVKEY')['file_name'].count()>15)].index.to_list()

if numeric_id is not None:
    gvkeys_list = list(GVKEYs) # Convert to list to ensure proper indexing
    index = numeric_id % len(gvkeys_list)
    assigned_gvkey = gvkeys_list[index]
    print(f"Assigned GVKEY for student {student_id}: {assigned_gvkey}")
else:
    print("Cannot assign GVKEY due to invalid Student ID format.")


Sample_EC=Sample_EC[Sample_EC.GVKEY == assigned_gvkey]

print("The company assigned to you is: %s"%Sample_EC.co_conm.iloc[0])

# # Load the Sample's Presentation texts
# Sample_Presentations = pd.read_feather("https://www.dropbox.com/scl/fi/uceh2xva5g4apbmt92cgt/Sample_Calls_Presentations.feather?rlkey=ln4nzsa4nenqyvm0pg2cur9sp&dl=1")
# Sample_Presentations = Sample_Presentations[Sample_Presentations.file_name.isin(Sample_EC.file_name)]
# Load the Q&A session textual data for the sample
Sample_QAs = pd.read_feather("https://www.dropbox.com/scl/fi/iq4111nlmsykp2tzxk9xg/Sample_Calls_QA.feather?rlkey=xabjqmwhesx05jivrlfzkgj6m&dl=1")
Sample_QAs = Sample_QAs[Sample_QAs.file_name.isin(Sample_EC.file_name)]

# The Main DF:
Sample_EC.head(10)

## Note: column "file_name" is to be used for the merging

# ## Columns:
#     # Identifiers
#     "GVKEY": "A unique company identifier used by Compustat.",
#     "date_rdq": "The reporting date of the quarterly earnings or a related key event date.",
#     "co_conm": "The company’s name in CRSP.",

#     # Earnings Call Columns
#     "file_name": "The identifier or filename of the earnings call transcript.",
#     "CAR-11-Carhart": "Cumulative Abnormal Return over an event window using the Carhart 4-factor model.",
#     "CAR-11-ff3": "Cumulative Abnormal Return over an event window using the Fama-French 3-factor model.",
#     "CAR01-Carhart": "Cumulative Abnormal Return (alternative window) using the Carhart 4-factor model.",
#     "CAR01-ff3": "Cumulative Abnormal Return (alternative window) using the Fama-French 3-factor model.",
#     "IV": "Implied volatility (often from options) reflecting expected future stock price volatility.",
#     "hvol": "Historical volatility of the stock, based on past price movements.",
#     "IV_l1d": "Implied volatility lagged by one day.",
#     "IV_l2d": "Implied volatility lagged by two days.",
#     "IV_f1d": "Implied volatility forecasted or measured one day forward.",

#     # I/B/E/S Columns
#     "NUMEST": "The number of analyst estimates contributing to the consensus.",
#     "NUMUP": "The number of analysts who have revised their EPS estimates upward.",
#     "NUMDOWN": "The number of analysts who have revised their EPS estimates downward.",
#     "MEDEST": "The median of analyst EPS estimates.",
#     "MEANEST": "The mean of analyst EPS estimates.",
#     "ACTUAL": "The I/B/E/S standardized actual EPS figure, often adjusted for comparability.",
#     "surp": "The earnings surprise, typically ACTUAL minus MEANEST.",
#     "SurpDec": "A scaled or decimalized version of the earnings surprise.",

#     # Compustat Columns
#     "atq": "Total Assets (Quarterly)",
#     "actq": "Current Assets (Quarterly)",
#     "cheq": "Cash and Cash Equivalents (Quarterly)",
#     "rectq": "Accounts Receivable (Quarterly)",
#     "invtq": "Inventory (Quarterly)",
#     "ltq": "Total Liabilities (Quarterly)",
#     "lctq": "Current Liabilities (Quarterly)",
#     "apq": "Accounts Payable (Quarterly)",
#     "ceqq": "Total Equity (Quarterly)",
#     "seqq": "Common Equity (Quarterly)",

#     "capxy": "Capital Expenditures (Note: 'capxy' is annual by default, quarterly approximations derived from segments)",
#     "dpq": "Depreciation and Amortization (Quarterly)",
#     "saleq": "Revenue (Quarterly)",
#     "cogsq": "Cost of Goods Sold (Quarterly)",
#     "oiadpq": "Operating Income (Quarterly)",
#     "niq": "Net Income (Quarterly)",
#     "epspxq": "Basic Earnings Per Share (Quarterly)",
#     "epspiq": "Diluted Earnings Per Share (Quarterly)",
#     "dlttq": "Long-Term Debt (Quarterly)",
#     "dlcq": "Debt in Current Liabilities (Quarterly)",
#     "prccq": "Price Close - Fiscal Quarter",
#     "cshoq": "Common Shares Outstanding (Quarterly)",
#     "dvpq": "Dividends Paid (Quarterly)",
#     "xintq": "Interest Expense (Quarterly)"

Sample_QAs.head()
qa_df = Sample_QAs

# Q&A DataFrame: Sample_QAs
# -------------------------
# This DataFrame stores the Q&A section of earnings call transcripts.
#
# Columns
# -------
# - QA:
#     String flag indicating whether the row is a question or an answer.
#     "q" = analyst question
#     "a" = management answer
#
# - speaker_name:
#     Name of the person speaking (either the analyst or the management representative).
#
# - file_name:
#     Identifier of the source earnings call transcript in the main DataFrame
#     (e.g., the original transcript file name).
#
# - QA_text:
#     Full text of the question or answer.
#
# - QA_number:
#     Integer indicating the sequence number of the Q&A pair in the transcript.
#     Starts at 1 for the first question, 2 for the second, etc.
#     The counter increments only for new questions ("q");
#     all corresponding answers ("a") share the same QA_number as their question.

"""# Step 3: Do your own codings
Good luck with the assignment!
"""

print("Số lượng speaker names duy nhất:", qa_df['speaker_name'].nunique())
print("\nDanh sách speakers:")
print(qa_df['speaker_name'].value_counts())

from itertools import combinations

# 1. Lấy danh sách các tên duy nhất
unique_names = qa_df['speaker_name'].unique()

# 2. Tạo danh sách các cặp tên để so sánh
name_pairs = list(combinations(unique_names, 2))

print(f"{'Tên thứ nhất':<30} | {'Tên thứ hai':<30} | {'Chung file?'}")
print("-" * 80)

for n1, n2 in name_pairs:
    # Chỉ kiểm tra nếu hai tên có ít nhất một từ giống nhau (thường là họ)
    set1 = set(n1.split())
    set2 = set(n2.split())

    if len(set1.intersection(set2)) > 0:  # Nếu có ít nhất 1 từ trùng nhau
        # Lấy tập hợp các file_name của từng người
        files_n1 = set(Sample_QAs[Sample_QAs['speaker_name'] == n1]['file_name'])
        files_n2 = set(Sample_QAs[Sample_QAs['speaker_name'] == n2]['file_name'])

        # Tìm các file xuất hiện chung
        shared = files_n1.intersection(files_n2)

        status = f"CHUNG {len(shared)} file" if len(shared) > 0 else "KHÔNG chung file (Có thể gộp)"
        print(f"{n1:<30} | {n2:<30} | {status}")

# 1. Làm sạch định dạng gốc trước
qa_df['speaker_name'] = qa_df['speaker_name'].str.strip().str.lower()

# 2. Định nghĩa lại Dictionary (đảm bảo các key cũng là chữ thường và không cách thừa)
clean_map = {
    'jud bailey': 'judson edwin bailey',
    'jeff miller': 'jeffrey allen miller',
    'dave lesar': 'david j. lesar',
    'james west': 'james carlyle west',
    'jim wicklund': 'james knowlton wicklund',
    'james wicklund': 'james knowlton wicklund',
    'angie sedita': 'angeline marie sedita',
    'angeline m. sedita': 'angeline marie sedita',
    'sean meakim': 'sean christopher meakim',
    'dan boyd': 'daniel jon boyd',
    'david anderson': 'john david anderson',
    'scott gruber': 'scott andrew gruber',
    'bill herbert': 'william andrew herbert',
    'timna tanners': 'timna beth tanners',
    'kurt hallead': 'kurt kevin hallead',
    'ole slorer': 'ole henry slorer',
    'chase mulvehill': 'brandon chase mulvehill'
}

# 3. Thực hiện thay thế
qa_df['speaker_clean'] = qa_df['speaker_name'].replace(clean_map)

# 4. Kiểm tra kết quả thực tế
print("--- SO SÁNH TRƯỚC VÀ SAU ---")
print(f"Số lượng unique ban đầu: {qa_df['speaker_name'].nunique()}")
print(f"Số lượng unique sau khi clean: {qa_df['speaker_clean'].nunique()}")

# Xem thử top 10 người sau khi clean
print("\nTop speakers sau khi làm sạch:")
print(qa_df['speaker_clean'].value_counts().head(10))

# 3. XÓA cột cũ và đổi tên cột mới
qa_df = qa_df.drop('speaker_name', axis=1)
qa_df = qa_df.rename(columns={'speaker_clean': 'speaker_name'})