# some more data 

APP_TITLE = "TaxCalc"
VERSION = "1.0.0"

STANDARD_DEDUCTION = 75000
#this slab data i took from the govt which i could see 
OLD_REGIME_SLABS = [
    {"limit": 250000, "rate": 0.00},
    {"limit": 500000, "rate": 0.05},
    {"limit": 1000000, "rate": 0.20},
    {"limit": float("inf"), "rate": 0.30},
]

NEW_REGIME_SLABS = [
    {"limit": 400000, "rate": 0.00},
    {"limit": 800000, "rate": 0.05},
    {"limit": 1200000, "rate": 0.10},
    {"limit": 1600000, "rate": 0.15},
    {"limit": 2000000, "rate": 0.20},
    {"limit": float("inf"), "rate": 0.30},
]

HEALTH_EDUCATION_CESS_RATE = 0.04
