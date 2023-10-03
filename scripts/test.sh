#!/usr/bin/env bash

set -euxo pipefail

poetry run pytest app/tests
