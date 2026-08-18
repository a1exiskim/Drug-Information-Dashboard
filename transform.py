def clean_drug_data(drug):
    default = 'No information available'

    try:
        drug_name = drug['openfda']['brand_name'] # nothing can be displayed without drug name
    except KeyError:
            raise KeyError('Brand name missing from OpenFDA response')
    if drug_name:
        drug_name = drug_name[0] # removing list structure 
    else:
        raise KeyError('Brand name missing from OpenFDA response')
    
    generic_name = drug['openfda'].get('generic_name')
    if generic_name:
        generic_name = generic_name[0]
    else:
        generic_name = default 

    manufacturer_name = drug['openfda'].get('manufacturer_name')
    if manufacturer_name:
        manufacturer_name = manufacturer_name[0]
    else:
        manufacturer_name = default

    warnings = drug.get('warnings', [default])
    if warnings == []:
        warnings = [default] 
    warnings = warnings[0]
    
    dosage_and_administration = drug.get('dosage_and_administration', [default])
    if dosage_and_administration == []:
        dosage_and_administration = [default]
    dosage_and_administration = dosage_and_administration[0]

    drug_purpose = drug.get('purpose', [default])
    if drug_purpose == []:
        drug_purpose = [default]
    drug_purpose = drug_purpose[0]

    active_ingredient = drug.get('active_ingredient', [default])
    if active_ingredient == []:
        active_ingredient = [default]
    active_ingredient = active_ingredient[0]

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