from flask import request, url_for
from werkzeug.routing import BuildError


def slice_jobs(jobs, initial_position, amount):
    return jobs[initial_position : initial_position + amount]


def get_job(jobs, id_):
    for job in jobs:
        if job["id"] == id_:
            return job


def get_int_from_args(field_name, default_value):
    try:
        value = int(request.args.get(field_name, default_value))
    except (ValueError, TypeError):
        value = default_value
    return value


def build_jobs_urls(jobs):
    for job in jobs:
        try:
            job["url"] = url_for("client.job", index=job["id"])
        except BuildError:
            break
