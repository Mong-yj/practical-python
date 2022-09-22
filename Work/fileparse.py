# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, types, delimiter=',', select=None, has_headers=True):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # 헤더를 읽음
        if has_headers:
            headers = next(rows)

            if select:
                columns = [headers.index(col) for col in select]
            else:
                columns = []

            records = []
            for row in rows:
                if not row:    # 데이터가 없는 행을 건너뜀
                    continue
                if columns:
                    row = [row[col] for col in columns]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                record = dict(zip(headers, row))
                records.append(record)
        else:
            records = []
            for row in rows:
                if not row:    # 데이터가 없는 행을 건너뜀
                    continue
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                record = tuple(row)
                records.append(record)

    return records


