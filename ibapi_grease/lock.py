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

from ibapi.connection import Connection
from ibapi import connection, client

class FakeLock(object):
    """
    This is a dummy lock to disable locking of the IB socket connection, which
    is slow and unnecessary. https://github.com/InteractiveBrokers/tws-api/issues/464
    """
    def acquire(self):
        pass

    def release(self):
        pass

class NonlockingConnection(Connection):
    def __init__(self, *args, **kwargs):
        super(NonlockingConnection, self).__init__(*args, **kwargs)
        if hasattr(self, "lock"):
            self.lock = FakeLock()

def install_nonlocking_connection():
    """
    Installs a dummy lock to disable locking of the IB socket connection, which
    is slow and unnecessary. https://github.com/InteractiveBrokers/tws-api/issues/464
    """
    connection.Connection = NonlockingConnection
    client.Connection = NonlockingConnection
