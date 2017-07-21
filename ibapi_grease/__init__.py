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

from .lock import install_nonlocking_connection
from .log import silence_ibapi_logging

class PatchInstaller(object):
    """
    Patch installer which uses the Borg pattern to only run once.
    """

    __state = {} # Borg pattern

    def __init__(self):
        self.__dict__ = self.__state
        self.installed = getattr(self, 'installed', False)

    def __call__(self):
        """
        Disables locking and logging in ibapi.
        """
        if self.installed:
            return

        install_nonlocking_connection()
        silence_ibapi_logging()

        self.installed = True

patch_all = PatchInstaller()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
