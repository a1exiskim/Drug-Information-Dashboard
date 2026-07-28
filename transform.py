def clean_drug_data(drug):
    drug_name = drug['openfda']['brand_name']
    generic_name = drug['openfda']['generic_name']
    manufacturer_name = drug['openfda']['manufacturer_name']

    cleaned_drug = {
        'drug_name': drug_name,
        'generic_name': generic_name,
        'manufacturer': manufacturer_name 
    }

    return cleaned_drug