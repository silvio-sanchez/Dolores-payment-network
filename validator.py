# Dolores Payment Network - Cheque Validator
# Rule: Day Credits + Insurance >= Cheque Amount
# Daily settlement must finish at zero.

def can_create_cheque(day_credits, insurance, cheque_amount):
    available = day_credits + insurance
    if cheque_amount <= available:
        return True, f"APPROVED: Cheque ${cheque_amount} - Available ${available}"
    else:
        return False, f"REJECTED: Cheque ${cheque_amount} - Available only ${available}"

def check_daily_settlement(total_in, total_out):
    balance = total_in - total_out
    if balance == 0:
        return True, "SETTLEMENT OK: Day closed at zero"
    else:
        return False, f"SETTLEMENT ERROR: Balance is ${balance}, must be 0"

# Test - Example from Dolores
print(can_create_cheque(day_credits=100000, insurance=50000, cheque_amount=120000))
print(can_create_cheque(day_credits=100000, insurance=50000, cheque_amount=200000))
print(check_daily_settlement(total_in=500000, total_out=500000))
print(check_daily_settlement(total_in=500000, total_out=480000))
