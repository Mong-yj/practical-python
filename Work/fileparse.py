#!/usr/bin/env python3
# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(file, types=None, silence_errors=False, delimiter=',', select=None, has_headers=True):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    rows = csv.reader(file, delimiter=delimiter)

    if (not has_headers) and select :
        raise RuntimeError("select argument requires column headers")

    # 헤더를 읽음
    if has_headers:
        headers = next(rows)
    else:
        headers = []

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
            r_count = 1
            row_new = []
            for func, val in zip(types, row):
                try: r = func(val)
                except Exception as e:
                    if silence_errors:
                        pass
                    else:
                        print("Row %d: Couldn's convert"%r_count, row)
                        print("Row %d: Reason"%r_count,e)
                row_new.append(r)
                r_count += 1
            row = row_new

        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records


