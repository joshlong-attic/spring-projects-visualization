#!/usr/bin/env python3
import urllib.request, json, os


def fetch_json(s):
    with urllib.request.urlopen(s) as f:
        d = f.read()
        return json.loads(str(d, 'utf-8'))


def fetch_projects():
    return fetch_json('http://localhost:8080/project_metadata/projects')


def fetch_project(project_id):
    return fetch_json('http://localhost:8080/project_metadata/%s' % project_id)


projects = fetch_projects()
project_json_rows = []

for p in projects:
    project = fetch_project(p)
    labels = [l['label'] for l in project['projectLabels']]
    row = ''' { "project" : "%s", "labels" : [ %s ] } ''' % (p, ','.join(['"%s"' % x for x in labels]))
    row = row.strip()
    project_json_rows.append(row)

print( ','.join(project_json_rows))
