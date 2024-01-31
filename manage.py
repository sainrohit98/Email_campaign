#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import redis
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    redis_client = redis.Redis(host='localhost', port=6379)
    try:
        redis_client.ping()
        print("Redis connection successful!")
    except redis.ConnectionError as e:
        print("Error connecting to Redis:", e)
    main()
