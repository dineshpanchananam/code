d = """01-01-1990	70201	Trust Indenture	legal_entity_updated_again.pdf	73018	3		2019-02-22 16:37:20	23237	75	AsofDateDateofReporting	As of Date (Date of Reporting)	1		0	2555402	156878	2019-02-22 16:43:25	Signature Fields	datetime	72.515625	130.5	57.6119842529297	12.75	1	3053150	legal_entity_updated_again.pdf	application/pdf
Name1	70201	Trust Indenture	legal_entity_updated_again.pdf	73018	3		2019-02-22 16:37:20	23237	148	LegalEntityName	Legal Entity Name	0		1	2555402	156882	2019-02-22 16:43:25	Entity Legal Info	text	72.515625	115.86328125	63.0703125	12.75	1	3053150	legal_entity_updated_again.pdf	application/pdf
LName	71054	Trust Deed/Agreement	legal_entity_changed_again.pdf	73022	4		2019-02-22 16:45:41	2996	1	LegalName	Legal Name	0		0	2555406	156886	2019-02-22 16:48:43	Entity Legal Info	text	72.515625	71.94140625	97.3828125	12.75	1	3053166	legal_entity_changed_again.pdf	application/pdf
01-01-1980	71054	Trust Deed/Agreement	legal_entity_changed_again.pdf	73022	4		2019-02-22 16:45:41	2996	75	AsofDateDateofReporting	As of Date (Date of Reporting)	1		0	2555406	156890	2019-02-22 16:48:43	Signature Fields	datetime	72.515625	101.21484375	57.5999908447266	12.75	1	3053166	legal_entity_changed_again.pdf	application/pdf
Name2\t71054	Trust Deed/Agreement	legal_entity_changed_again.pdf	73022	4		2019-02-22 16:45:41	2996	148	LegalEntityName	Legal Entity Name	0		1	2555406	156894	2019-02-22 16:48:43	Entity Legal Info	text	72.515625	71.94140625	97.3828125	12.75	1	3053166	legal_entity_changed_again.pdf	application/pdf
Name3	71838	FATCA Consent Letter	legal_entity2.pdf	73006	2		2019-02-22 16:02:10	23402	148	LegalEntityName	Legal Entity Name	0		1	2555386	156866	2019-02-22 16:11:34	Entity Legal Info	text	72.515625	71.94140625	62.4219131469727	12.75	1	3053114	legal_entity2.pdf	application/pdf
01-01-1910	71838	FATCA Consent Letter	legal_entity2.pdf	73006	2		2019-02-22 16:02:10	23402	75	AsofDateDateofReporting	As of Date (Date of Reporting)	1		0	2555386	156862	2019-02-22 16:11:34	Signature Fields	datetime	72.515625	86.578125	57.5999908447266	12.75	1	3053114	legal_entity2.pdf	application/pdf"""

d1 = d.split("\n")
# print(len(d1))
d1 = [x.split("\t") for x in d1]

y = """         value,
                d.id as document_id,
                dt.name as document_type_name,
                dv.version_name as document_name,
                dv.id as document_version_id,
                dv.version as document_version,
                dv.redacted_version as document_redacted_version,
                dv.uploaded as last_uploaded,
                dv.document_types_data_set_schema_id as document_types_data_set_schema_id,
                dses.field_id as field_id,
                f.code as field_code,
                f.name as display,
                f.is_document_specific as is_document_specific,
                f.entity_data_name as entity_data_name,
                f.is_editable as is_editable,
                dv.data_set_id as data_set_id,
                dse.id as data_set_element_id,
                dse.last_updated as last_modified,
                fg.name as field_group_name,
                it.type as type,
                osf.offset_left as offset_left,
                osf.offset_top as offset_top,
                osf.width as width,
                osf.height as height,
                osf.page as page,
                dv.file_id as file_id,
                fi.display_name as file_name,
                fi.mime_type as file_mime_type,
                f.order_in_group,"""

y1 = y.split('\n')
y2 = [x.strip().split()[-1][:-1] for x in y1]

# print(y2)
# print(len(y1))

from itertools import izip
from pprint import pprint as pp
rows = []
for x in d1:
	rows.append(dict(izip(y2, x)))
import json
print(json.dumps(rows))