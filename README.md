# Label Maker
Easy-to-use script to generate *.xlsx files from genbank/txt for Brady label printers

## Installation
Make sure you have Python ver. 3.2+ installed on your machine as well as the following libraries:
- [Biopython](https://pypi.org/project/biopython/)
- [Pandas](https://pypi.org/project/pandas/) 

## Usage
### Parameters
Name | Type | Required | Example | Help 
-----|------|----------|---------|-----
-src | string | True | "input/example.gb" | Input file (txt, gb, gbk)
-out | string | True | "output/example.xlsx | Output file (xlsx file extension required)
-c | string | True | "CedKB" | Initials of the creator

### Example
Nomenclature example:
> pME_Cp_0_1_001_psbH_5'Hom__C   

Example runs:

> python label_maker.py -src input/example.txt -out output/example.xlsx -c CedKB

> python label_maker.py -src "input/90 documents from pME_Cp_0_3.gb" -out "output/labels_21022022.xlsx" -c "CedKB"

### Tested
This script was tested on Windows 10 with:
- Python ver. 3.6.7
- Biopython ver. 1.79
- Pandas ver. 0.24.2

