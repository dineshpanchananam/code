from itertools import chain, groupby
from operator import itemgetter
from collections import defaultdict
import json

rows = []
with open('c.json') as f:
    rows = json.loads(f.read())

# print(sorted(rows[0].keys()))

class Cls:
    @classmethod
    def from_sql(Cls, res, source=None, documents=None, in_process_document=None):

        '''
        ## from_sql
        '''

        return Cls(res.get('field_id', None), res.get('display', None),
                   res.get('data_set_element_id', None), res.get('value', None),
                   res.get('type', None), res.get('offset_left', None),
                   res.get('offset_top', None), res.get('width', None),
                   res.get('height', None), res.get('page', None),
                   res.get('font_size', None), res.get('datetime_format', None),
                   res.get('last_modified'), source, documents, in_process_document, res.get('field_group_name', None),
                   res.get('field_code', None),
                   res.get('is_editable', 1),
                   res.get('order_in_group', None),
                   res.get('entity_data_name', None))

    def __init__(self, field_id=None, display=None, data_set_element_id=None,
                 value=None, input_type=None, offset_left=None, offset_top=None,
                 width=None, height=None, page=None, font_size=None,
                 datetime_format=None, last_modified=None, source=None, documents=None, in_process_document=None,
                 field_group_name=None, field_code=None, is_editable=1, order_in_group=None, entity_data_name=None):
        '''
        ## __init__
        '''
        self._display = display
        self._field_id = field_id
        self._data_set_element_id = data_set_element_id
        self._value = value
        self._input_type = input_type
        self._offset_left = offset_left
        self._offset_top = offset_top
        self._width = width
        self._height = height
        self._page = page
        self._font_size = font_size
        self._datetime_format = datetime_format
        self._last_modified = last_modified
        self._source = source
        self._documents = documents
        self._in_process_document = in_process_document
        self._field_group_name = field_group_name
        self._is_editable = is_editable
        self._field_code = field_code
        self._order_in_group = order_in_group
        self._entity_data_name = entity_data_name

def for_entity():
        """
        ## for_entity
        """
  
        form_rows = []
        non_redacted_rows = []
        redacted_rows = rows
        in_process_non_redacted_rows = []
        in_process_redacted_rows = []

        doc_rows = chain(non_redacted_rows, redacted_rows)
        in_process_doc_rows = chain(in_process_non_redacted_rows, in_process_redacted_rows)
        field_id_key = itemgetter('field_id')
        doc_id_key = itemgetter('document_id')

        doc_fields_dict = defaultdict(list)
        in_process_fields_dict = defaultdict(list)
        maxfunc = lambda r: int(r['document_version'] * 10) + (r['document_redacted_version'] or 0)

        # Deal with redacted versions for cases where there is no nonredacted version with the same major number
        # In this case, we pick the highest redacted version as a possible source for that field
        for field_id, field_rows in groupby(sorted(doc_rows, key=field_id_key), key=field_id_key):
            for doc_id, field_doc_rows in groupby(sorted(field_rows, key=doc_id_key), key=doc_id_key):
                p = list(field_doc_rows)
                print('#', len(p))
                doc_fields_dict[field_id].append(max(p, key=maxfunc))

        print(map(len, doc_fields_dict.values()))
        # Determine the in processing sources using the same logic
        for field_id, field_rows in groupby(sorted(in_process_doc_rows, key=field_id_key), key=field_id_key):
            for doc_id, field_doc_rows in groupby(sorted(field_rows, key=doc_id_key), key=doc_id_key):
                in_process_fields_dict[field_id].append(max(field_doc_rows, key=maxfunc))

        # Convert form fields to dict
        form_fields_dict = dict((r['field_id'], r) for r in form_rows)

        # Determine the current, historic and in-processing sources for each field
        fields = []
        for field_id, doc_rows in doc_fields_dict.items():
            sorted_rows = sorted(doc_rows, key=itemgetter('last_uploaded'), reverse=True)

            latest_doc_row = sorted_rows[0]
            value_row = None
            current_source = None
            historic_sources = None

            # Check if each editable field has a more recent value in forms data, and if so, use it
            if latest_doc_row['is_editable'] and field_id in form_fields_dict \
                and form_fields_dict[field_id]['last_modified'] > latest_doc_row['last_uploaded']:
                value_row = form_fields_dict[field_id]
                current_source = None
                historic_sources = sorted_rows
            else:
                value_row = latest_doc_row
                current_source = latest_doc_row
                historic_sources = sorted_rows[1:]

            processing_source = None
            processing_sources = in_process_fields_dict.get(field_id)
            if processing_sources:
                latest_processing_source = max(processing_sources, key=itemgetter('last_uploaded'))
                # Processing sources are considered only if they can possibly update entity data
                last_modified = value_row.get('last_uploaded') or value_row['last_modified']
                if latest_processing_source['last_uploaded'] > last_modified:
                    processing_source = latest_processing_source
            fields.append(Cls.from_sql(
                    value_row,
                    DataSource.from_sql(current_source) if current_source else None,
                    [HistoricalDocument.from_sql(hs, match=(hs['value'] == value_row['value'])) for hs in
                     historic_sources],
                    InProcessDocument.from_sql(processing_source) if processing_source else None))

        # Process form fields (editable) with no matching document sources. They have no historic sources either
        for field_id, row in form_fields_dict.items():
            if field_id not in doc_fields_dict:
                fields.append(Cls.from_sql(row))

        return fields




class DataSource(object):
    '''
    # DataSource : Most recent document that was scraped or in process
    '''

    def __init__(self, file_mime_type, document_name, file_id, offset_left, offset_top, width, height, page,
                 document_version_id, file_name, document_type_name, last_uploaded, value=None, document_version=None, document_redacted_version=None):
        '''
        ## __init__
        '''

        self._file_mime_type = file_mime_type
        self._document_name = document_name
        self._file_id = file_id
        self._offset_left = offset_left
        self._offset_top = offset_top
        self._width = width
        self._height = height
        self._page = page
        self._value = value
        self._document_version_id = document_version_id
        self._file_name = file_name
        self._document_type_name = document_type_name
        self._last_uploaded = last_uploaded
        self._document_version = document_version
        self._document_redacted_version = document_redacted_version

    @classmethod
    def from_sql(Cls, res):
        '''
        ## from_sql
        '''
        return Cls(res['file_mime_type'], res['document_name'], res['file_id'],
                   res['offset_left'], res['offset_top'], res['width'],
                   res['height'], res['page'], res['document_version_id'],
                   res['file_name'], res['document_type_name'],
                   res['last_uploaded'], res.get('value', None),
                   res['document_version'], res['document_redacted_version'])

    def to_bas(self):
        '''
        ## to_bas
        '''

        return {
            'file_mime_type': self._file_mime_type,
            'document_name': self._document_name,
            'file_id': self._file_id,
            'offset_left': self._offset_left,
            'offset_top': self._offset_top,
            'width': self._width,
            'height': self._height,
            'page': self._page,
            'value': self._value,
            'document_version_id': self._document_version_id,
            'file_name': self._file_name,
            'document_type_name': self._document_type_name,
            'last_uploaded': bdet.Datetime.fromPy(self._last_uploaded) if self._last_uploaded is not None else None,
            'document_version': self._document_version,
            'document_redacted_version': self._document_redacted_version,
        }


class HistoricalDocument(object):
    '''
    # HistoricalDocument : Historical Document containing matching data fields
    '''

    @classmethod
    def from_sql(Cls, res, match):
        '''
        ## from_sql
        '''

        return Cls(res['field_id'], res['value'], res['document_id'], res['document_name'], res['last_uploaded'],
                   res['file_id'], match, res['file_mime_type'], res['document_types_data_set_schema_id'],
                   res['document_version_id'], res['file_name'], res['document_type_name'],
                   res['offset_left'], res['offset_top'], res['width'], res['height'], res['page'],
                   res['document_version'], res['document_redacted_version'])

    def __init__(self, field_id, field_value, document_id, document_name, last_uploaded, file_id, match, file_mime_type,
                 document_types_data_set_schema_id, document_version_id, file_name, document_type_name,
                 offset_left, offset_top, width, height, page, document_version=None, document_redacted_version=None):
        '''
        ## __init__
        '''

        self._field_id = field_id
        self._field_value = field_value
        self._document_id = document_id
        self._document_name = document_name
        self._last_uploaded = last_uploaded
        self._file_id = file_id
        self._match = match
        self._file_mime_type = file_mime_type
        self._document_types_data_set_schema_id = document_types_data_set_schema_id
        self._document_version_id = document_version_id
        self._file_name = file_name
        self._document_type_name = document_type_name
        self._offset_left = offset_left
        self._offset_top = offset_top
        self._width = width
        self._height = height
        self._page = page
        # self._ocr_info = OCRInfo(self._offset_left, self._offset_top, self._width, self._height, self._page)
        self._document_redacted_version = document_redacted_version
        self._document_version = document_version

    def to_bas(self):
        '''
        ## to_bas
        '''

        return {
            'document_id': self._document_id,
            'document_name': self._document_name,
            'file_id': self._file_id,
            'match': self._match,
            'file_mime_type': self._file_mime_type,
            'document_types_data_set_schema_id': self._document_types_data_set_schema_id,
            'document_version_id': self._document_version_id,
            'file_name': self._file_name,
            'document_type_name': self._document_type_name,
            'last_uploaded': bdet.Datetime.fromPy(self._last_uploaded) if self._last_uploaded is not None else None,
            'field_id': self._field_id,
            'field_value': self._field_value,
            'ocr_info': self._ocr_info.to_bas() if self._ocr_info else None,
            'document_version': self._document_version,
            'document_redacted_version': self._document_redacted_version
        }

for x in for_entity():
    print x._display, x._value