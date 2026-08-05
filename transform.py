def clean_drug_data(drug):
    default = 'No information available'

    try:
        drug_name = drug['openfda']['brand_name']
    except KeyError:
        raise KeyError('Drug name missing from OpenFDA response')

    generic_name = drug['openfda'].get('generic_name', [default])
    manufacturer_name = drug['openfda'].get('manufacturer_name', [default])
    warnings = drug.get('warnings', [default])
    dosage_and_administration = drug.get('dosage_and_administration', [default])
    drug_purpose = drug.get('purpose', [default])
    active_ingredient = drug.get('active_ingredient', [default])

    cleaned_drug = {
        'drug_name': drug_name,
        'generic_name': generic_name,
        'manufacturer': manufacturer_name,
        'warnings': warnings,
        'purpose': drug_purpose,
        'dosage_and_administration': dosage_and_administration, 
        'active_ingredient': active_ingredient
    }

    return cleaned_drug