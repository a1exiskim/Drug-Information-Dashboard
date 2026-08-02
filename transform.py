def clean_drug_data(drug):
    drug_name = drug['openfda']['brand_name']
    generic_name = drug['openfda']['generic_name']
    manufacturer_name = drug['openfda']['manufacturer_name']
    warnings = drug['warnings']
    dosage_and_administration = drug['dosage_and_administration']
    drug_purpose = drug['purpose']
    active_ingredients = drug['active_ingredient']

    cleaned_drug = {
        'drug_name': drug_name,
        'generic_name': generic_name,
        'manufacturer': manufacturer_name,
        'warnings': warnings,
        'purpose': drug_purpose,
        'dosage_and_administration': dosage_and_administration, 
        'active_ingredients': active_ingredients
    }

    return cleaned_drug