# Copyright 2017 QuantRocket - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pkgutil
import ibapi

def noop(*args, **kwargs):
    """
    Do nothing.
    """
    return

def silence_ibapi_logging(levels=["DEBUG", "INFO"]):
    """
    Silences the excessive ibapi logging to the root logger.
    """
    levels = levels or ["DEBUG", "INFO"]

    for level in levels:
        if level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            raise ValueError("unknown log level: {0}".format(level))

    for _, module_name, _ in pkgutil.iter_modules(ibapi.__path__):
        module = __import__("ibapi.{0}".format(module_name), fromlist="ibapi")
        if not hasattr(module, "logging"):
            continue

        for level in levels:
            setattr(module.logging, level.lower(), noop)
