inputs_by_model_dict = {
    "general": ["birthday", "retirement_age_yrs", "retirement_age_mos"],
    "savings": [
        "base_savings",
        "base_saved_per_mo",
        "base_savings_per_yr_increase",
        "savings_lower_limit",
        "base_monthly_bills",
    ],
    "payments": [
        "pmt_name",
        "pmt_start_age_yrs",
        "pmt_start_age_mos",
        "pmt_length_yrs",
        "down_pmt",
        "monthly_pmt",
    ],
    "retirement": [
        "base_retirement",
        "base_retirement_per_mo",
        "base_retirement_per_yr_increase",
        "retirement_extra_expenses",
    ],
    "rates": [
        "base_rf_interest_per_yr",
        "base_mkt_interest_per_yr",
        "rf_interest_change_mos",
        "base_inflation_per_yr",
    ],
}


def model_to_dict(active_inputs, model):
    """Convert a Django model instance to a dictionary"""
    model_dict = {}
    for field in active_inputs._meta.fields:
        if field.name in inputs_by_model_dict[model]:
            field_name = field.name
            field_value = getattr(active_inputs, field_name)
            model_dict[field_name] = field_value
    return model_dict


def ensure_active_inputs(active_inputs):
    """Functtion to ensure inputs are acceptable"""
    assert active_inputs, "There are no active scenarios for this user"
    assert len(active_inputs) == 1, "There are too many active scenarios for this user"
