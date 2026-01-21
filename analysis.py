
import pandas as pd
import numpy as np

DATA_PATH = "Data/"

# Enerolment
enrol_1 = pd.read_csv(DATA_PATH + "api_data_aadhar_enrolment_0_500000.csv")
enrol_2 = pd.read_csv(DATA_PATH + "api_data_aadhar_enrolment_500000_1000000.csv")
enrol_3 = pd.read_csv(DATA_PATH + "api_data_aadhar_enrolment_1000000_1006029.csv")

enrolment_df = pd.concat([enrol_1, enrol_2, enrol_3], ignore_index=True)

# Biometric
bio_1 = pd.read_csv(DATA_PATH + "api_data_aadhar_biometric_0_500000.csv")
bio_2 = pd.read_csv(DATA_PATH + "api_data_aadhar_biometric_500000_1000000.csv")
bio_3 = pd.read_csv(DATA_PATH + "api_data_aadhar_biometric_1000000_1500000.csv")
bio_4 = pd.read_csv(DATA_PATH + "api_data_aadhar_biometric_1500000_1861108.csv")

biometric_df = pd.concat([bio_1, bio_2, bio_3, bio_4], ignore_index=True)

# Demographic
demo_1 = pd.read_csv(DATA_PATH + "api_data_aadhar_demographic_0_500000.csv")
demo_2 = pd.read_csv(DATA_PATH + "api_data_aadhar_demographic_500000_1000000.csv")
demo_3 = pd.read_csv(DATA_PATH + "api_data_aadhar_demographic_1000000_1500000.csv")
demo_4 = pd.read_csv(DATA_PATH + "api_data_aadhar_demographic_1500000_2000000.csv")
demo_5 = pd.read_csv(DATA_PATH + "api_data_aadhar_demographic_2000000_2071700.csv")

demographic_df = pd.concat([demo_1, demo_2, demo_3, demo_4, demo_5], ignore_index=True)


print("Enrolment data shape:", enrolment_df.shape)
print("Biometric data shape:", biometric_df.shape)
print("Demographic data shape:", demographic_df.shape)

print("\nEnrolment sample:")
print(enrolment_df.head(3))

# Check missing values
print("\nMissing values check:")
print("\nEnrolment missing values:")
print(enrolment_df.isna().sum())
print("\nBiometric missing values:")
print(biometric_df.isna().sum())
print("\nDemographic missing values:")
print(demographic_df.isna().sum())

# Check duplicate rows
print("\nDuplicate rows check:")
print("Enrolment duplicates:", enrolment_df.duplicated().sum())
print("Biometric duplicates:", biometric_df.duplicated().sum())
print("Demographic duplicates:", demographic_df.duplicated().sum())

#Check for impossible / invalid values
print("\nNegative or invalid value check:")
print("Enrolment negative values:")
print((enrolment_df[["age_0_5", "age_5_17", "age_18_greater"]] < 0).sum())
print("Biometric negative values:")
print((biometric_df[["total"]] < 0).sum())
print("Demographic negative values:")
print((demographic_df[["total"]] < 0).sum())

# Check date validity
print("\nInvalid date check:")
print("Invalid enrolment dates:", enrolment_df["date"].isna().sum())
print("Invalid biometric dates:", biometric_df["date"].isna().sum())
print("Invalid demographic dates:", demographic_df["date"].isna().sum())

# %%
